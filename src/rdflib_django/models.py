"""
The rdflib_django implementation uses Django models to store its triples.

The underlying models are Resource centric, because rdflib-django is intended
to be used for publishing resources.
"""
import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from rdflib_django import fields


class NamedGraph(models.Model):
    """
    Models a context which represents a named graph.
    """

    identifier = fields.URIField(verbose_name=_("Identifier"), unique=True)

    class Meta:  # pylint: disable=C1001
        verbose_name = _("named graph")
        verbose_name_plural = _("named graphs")

    def __unicode__(self):
        return "{0}".format(self.identifier)


class NamespaceModel(models.Model):
    """
    A namespace definition.

    In essence, a namespace consists of a prefix and a URI. However, the namespaces in rdflib_django
    also have an extra field called '`fixed`' - this is used to mark namespaces that cannot be
    remapped such as ``xml``, ``rdf`` and ``rdfs``.
    """

    prefix = models.CharField(max_length=50, verbose_name=_("Prefix"), unique=True)
    uri = models.CharField(max_length=500, verbose_name=_("URI"), db_index=True, unique=True)
    fixed = models.BooleanField(verbose_name=_("Fixed"), editable=False, default=False)

    class Meta:  # pylint: disable=C1001
        verbose_name = _("namespace")
        verbose_name_plural = _("namespaces")

    def __unicode__(self):
        return "@prefix {0}: <{1}>".format(self.prefix, self.uri)


class URIStatement(models.Model):
    """
    Statement where the object is a URI.
    """

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4)
    subject = fields.URIField(verbose_name=_("Subject"), db_index=True)
    predicate = fields.URIField(_("Predicate"), db_index=True)
    object = fields.URIField(_("Object"), db_index=True)
    context = models.ForeignKey(NamedGraph, verbose_name=_("Context"))

    class Meta:  # pylint: disable=C1001
        unique_together = ('subject', 'predicate', 'object', 'context')

    def __unicode__(self):
        return "{0}, {1}".format(self.as_triple(), self.context.identifier)    # pylint: disable=E1101

    def as_triple(self):
        """
        Converts this predicate to a triple.
        """
        return self.subject, self.predicate, self.object


class LiteralStatement(models.Model):
    """
    Statement where the object is a literal.
    """

    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4)
    subject = fields.URIField(verbose_name=_("Subject"), db_index=True)
    predicate = fields.URIField(_("Predicate"), db_index=True)
    object = fields.LiteralField(_("Object"), db_index=True)
    context = models.ForeignKey(NamedGraph, verbose_name=_("Context"))

    class Meta:  # pylint: disable=C1001
        unique_together = ('subject', 'predicate', 'object', 'context')

    def __unicode__(self):
        return "{0}, {1}".format(self.as_triple(), self.context.identifier)    # pylint: disable=E1101

    def as_triple(self):
        """
        Converts this predicate to a triple.
        """
        return self.subject, self.predicate, self.object

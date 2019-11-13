# -*- coding: utf-8 -*-

"""Manager for Bio2BEL HSDN."""

from typing import Mapping

from tqdm import tqdm

import pybel.dsl
from bio2bel.manager.bel_manager import BELManagerMixin
from pybel import BELGraph
from .constants import MODULE_NAME
from .models import Base
from .parser import get_hsdn_df


class Manager(BELManagerMixin):
    """Disease-symptom associations."""

    module_name = MODULE_NAME
    _base = Base

    def __init__(self, *args, **kwargs):  # noqa:D107
        self.graph = make_graph()

    @classmethod
    def _get_connection(cls):
        pass

    @staticmethod
    def is_populated() -> bool:
        """Check if the Bio2BEL HSDN database is populated."""
        return True

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the Bio2BEL HSDN database."""
        return dict(
            diseases=self.count_diseases(),
            symptoms=self.count_symptoms(),
            relations=self.count_relations(),
        )

    def populate(self) -> None:
        """Populate the Bio2BEL HSDN database."""

    def count_diseases(self) -> int:
        """Count the diseases in the database."""
        return sum(
            'doid' == node.namespace
            for node in self.graph
        )

    def count_symptoms(self) -> int:
        """Count the symptoms in the database."""
        return sum(
            'meshs' == node.namespace
            for node in self.graph
        )

    def count_relations(self) -> int:
        """Count the number of relations in the database."""
        return self.graph.number_of_edges()

    def to_bel(self) -> BELGraph:
        """Convert the HSDN to BEL."""
        return self.graph


def make_graph(use_tqdm: bool = False) -> BELGraph:
    graph = BELGraph(
        name='HSDN',
        version='0.0.0',
        description='Human symptom-disease network reproduced by Himmelstein et al.',
    )
    graph.annotation_pattern['Database'] = '.*'
    graph.annotation_pattern['HSDN_COOCCURS'] = '.*'
    graph.annotation_pattern['HSDN_TDIDF_SCORE'] = '.*'

    # TODO add namespaces for DOID and MeSH to graph!

    df = get_hsdn_df()
    it = df.iterrows()
    if use_tqdm:
        it = tqdm(it, desc='HSDN to BEL', total=len(df.index))
    for _, (symptom_name, disease_name, cooccurs, tfidf_score, disease_id, symptom_id, doid_id, doid_name) in it:
        symptom = pybel.dsl.Pathology(
            namespace='mesh',
            name=symptom_name,
            identifier=symptom_id,
        )
        disease = pybel.dsl.Pathology(
            namespace='doid',
            name=doid_name,
            identifier=doid_id,
        )
        graph.add_association(
            symptom,
            disease,
            citation='24967666',
            evidence='Human Symptom-Disease Network',
            annotations={
                'Database': 'HSDN',
                'HSDN_COOCCURS': cooccurs,
                'HSDN_TFIDF_SCORE': tfidf_score,
            },
        )

    return graph

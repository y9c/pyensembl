from __future__ import absolute_import
from os.path import exists


from .common import run_multiple_genomes


<<<<<<< HEAD
@test_ensembl_releases()
=======
@run_multiple_genomes()
>>>>>>> upstream/master
def gtf_path_endswith_gtf_gz(ensembl):
    path = ensembl.gtf.gtf_path
    assert exists(path)
    assert path.endswith(".gtf.gz")

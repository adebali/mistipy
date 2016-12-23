from mistipy.mistdb_wrapper.genome import Genome, Genomes


def test_genome():
    """Tests an API call to get a genome's info"""
    version = 'GCF_000302455.1'
    genome_instance = Genome(version)
    response = genome_instance.info()
    assert isinstance(response, dict)
    assert response['version'] == version
    assert response['name'] == "Methanobacterium formicicum DSM 3637"


def test_genomes():
    '''Test genomes iterations'''
    genomeLimit = 4
    genomesInstance = Genomes()
    totalGenomes = 0
    for genome in genomesInstance.iterate(genomeLimit):
        totalGenomes += 1
    assert totalGenomes == genomeLimit


def test_genomeGenes():
    '''Test genomic gene iterations'''
    geneLimit = 4
    version = 'GCF_000302455.1'
    genome_instance = Genome(version)
    totalGenes = 0
    for gene in genome_instance.iterateGenes(geneLimit):
        totalGenes += 1
    assert totalGenes == geneLimit


def test_genomeAndGenes():
    totalGenes = 0
    for genome in Genomes().iterate(4):
        for gene in Genome(genome['version']).iterateGenes(4):
            totalGenes += 1
    assert totalGenes == 4 * 4

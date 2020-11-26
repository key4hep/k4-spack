
from spack import *
from spack.pkg.k4.Ilcsoftpackage import Key4hepPackage, k4_add_latest_commit_as_version 

class K4lcioreader(CMakePackage, Key4hepPackage):
    """LCIO reader based on PODIO and EDM4hep"""
    homepage = "https://github.com/key4hep/k4LCIOReader"
    url      = "https://github.com/key4hep/k4LCIOReader/archive/v0.1.0.tar.gz"
    git      = "https://github.com/key4hep/k4LCIOReader.git"

    maintainers = ['mirguest']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.1.0', sha256='996d1ff78c0a8a2f7f358dd4ea19f955853ad0902ee86b99c484de58c5fc2e2c')

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')


    depends_on('lcio')
    depends_on('podio')
    depends_on('edm4hep')

    def cmake_args(self):
        args = []
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        return args

# ----------------------------------------------------------------------------

from spack import *
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_version 


class Cepcsw(CMakePackage):
    """CEPC offline experiment software based on Key4hep."""

    homepage = "https://github.com/cepc/CEPCSW"
    url      = "https://github.com/cepc/CEPCSW/archive/v0.1.tar.gz"
    git      = "https://github.com/cepc/CEPCSW.git"

    maintainers = ['mirguest']


    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    k4_add_latest_commit_as_version(git)
    version('master', branch='master')

    depends_on('clhep')
    depends_on('dd4hep +geant4')
    depends_on('edm4hep')
    depends_on('k4fwcore')
    depends_on('gaudi')
    depends_on('gear')
    depends_on('lcio')
    depends_on('lccontent')
    depends_on('pandorasdk')
    depends_on('pandorapfa')
    depends_on('root')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s'%self.spec.variants['cxxstd'].value)
        if self.spec.satisfies('^gaudi@:34.99'):
            args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')

        pandorapfa_prefix = self.spec["pandorapfa"].prefix
        pandorapfa_cmake_modules = pandorapfa_prefix + "/cmakemodules"

        cmake_modules = pandorapfa_cmake_modules
        args.append('-DCMAKE_MODULE_PATH=%s'%cmake_modules)
        return args

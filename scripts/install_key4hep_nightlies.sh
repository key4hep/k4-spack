rsync -axv --inplace --delete --copy-links  --quiet -e "ssh -T  -o Compression=no -o StrictHostKeyChecking=no -o GSSAPIAuthentication=yes -o GSSAPITrustDNS=yes" ${SPACK_BUILD_USER}@${SPACK_BUILD_MACHINE}:/cvmfs/sw-nightlies.hsf.org/spackages/ /cvmfs/sw-nightlies.hsf.org/spackages/

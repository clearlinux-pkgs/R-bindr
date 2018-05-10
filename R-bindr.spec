#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bindr
Version  : 0.1.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/bindr_0.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bindr_0.1.1.tar.gz
Summary  : Parametrized Active Bindings
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
bound function accepts additional arguments.

%prep
%setup -q -c -n bindr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523290935

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523290935
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bindr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bindr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bindr/DESCRIPTION
/usr/lib64/R/library/bindr/INDEX
/usr/lib64/R/library/bindr/LICENSE
/usr/lib64/R/library/bindr/Meta/Rd.rds
/usr/lib64/R/library/bindr/Meta/features.rds
/usr/lib64/R/library/bindr/Meta/hsearch.rds
/usr/lib64/R/library/bindr/Meta/links.rds
/usr/lib64/R/library/bindr/Meta/nsInfo.rds
/usr/lib64/R/library/bindr/Meta/package.rds
/usr/lib64/R/library/bindr/NAMESPACE
/usr/lib64/R/library/bindr/NEWS.md
/usr/lib64/R/library/bindr/R/bindr
/usr/lib64/R/library/bindr/R/bindr.rdb
/usr/lib64/R/library/bindr/R/bindr.rdx
/usr/lib64/R/library/bindr/help/AnIndex
/usr/lib64/R/library/bindr/help/aliases.rds
/usr/lib64/R/library/bindr/help/bindr.rdb
/usr/lib64/R/library/bindr/help/bindr.rdx
/usr/lib64/R/library/bindr/help/paths.rds
/usr/lib64/R/library/bindr/html/00Index.html
/usr/lib64/R/library/bindr/html/R.css

Name:		texlive-zref-check
Version:	72994
Release:	1
Summary:	Flexible cross-references with contextual checks based on zref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zref-check
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an user interface for making LaTeX
cross-references flexibly, while allowing to have them checked
for consistency with the document structure as typeset.
Statements such as "above", "on the next page", "previously",
"as will be discussed", "on the previous chapter" and so on can
be given to \zcheck in free-form, and a set of "checks" can be
specified to be run against a given "label", which will result
in a warning at compilation time if any of these checks fail.
\zctarget and the zcregion environment are also defined as a
means to easily set label targets to arbitrary places in the
text which can be referred to by \zcheck.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/zref-check
%{_texmfdistdir}/tex/latex/zref-check
%doc %{_texmfdistdir}/doc/latex/zref-check

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

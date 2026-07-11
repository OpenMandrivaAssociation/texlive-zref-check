%global tl_name zref-check
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.7
Release:	%{tl_revision}.1
Summary:	Flexible cross-references with contextual checks based on zref
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zref-check
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zref-check.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides an user interface for making LaTeX cross-
references flexibly, while allowing to have them checked for consistency
with the document structure as typeset. Statements such as "above", "on
the next page", "previously", "as will be discussed", "on the previous
chapter" and so on can be given to \zcheck in free-form, and a set of
"checks" can be specified to be run against a given "label", which will
result in a warning at compilation time if any of these checks fail.
\zctarget and the zcregion environment are also defined as a means to
easily set label targets to arbitrary places in the text which can be
referred to by \zcheck.


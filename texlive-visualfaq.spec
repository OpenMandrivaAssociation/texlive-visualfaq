%global tl_name visualfaq
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A Visual LaTeX FAQ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/visualfaq
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Having trouble finding the answer to a LaTeX question? The Visual LaTeX
FAQ is an innovative new search interface that presents over a hundred
typeset samples of frequently requested document formatting. Simply
click on a hyperlinked piece of text and the Visual LaTeX FAQ will send
your Web browser to the appropriate page in the TeX FAQ.


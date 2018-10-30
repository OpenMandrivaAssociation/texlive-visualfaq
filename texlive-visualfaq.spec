Name:		texlive-visualfaq
Version:	20180303
Release:	2
Summary:	A Visual LaTeX FAQ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/visualFAQ
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/visualfaq.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Having trouble finding the answer to a LaTeX question? The
Visual LaTeX FAQ is an innovative new search interface that
presents over a hundred typeset samples of frequently requested
document formatting. Simply click on a hyperlinked piece of
text and the Visual LaTeX FAQ will send your Web browser to the
appropriate page in the UK TeX FAQ.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/visualfaq

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

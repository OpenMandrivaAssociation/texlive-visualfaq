# revision 19677
# category Package
# catalog-ctan /info/visualFAQ
# catalog-date 2010-08-05 13:03:35 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-visualfaq
Version:	20100805
Release:	5
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
%doc %{_texmfdistdir}/doc/latex/visualfaq/README
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/README
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/anotherarticle.pdf
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/book-montage.png
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/fuzzytext.png
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/labelgraph.pdf
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/lorem-ipsum-logo.png
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/musixtex.png
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/visfaq-html.png
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/visualFAQ.ind
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/visualFAQ.ind2
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/visualFAQ.out
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/visualFAQ.tex
%doc %{_texmfdistdir}/doc/latex/visualfaq/source/watermark.pdf
%doc %{_texmfdistdir}/doc/latex/visualfaq/troubleshoot-vlf.pdf
%doc %{_texmfdistdir}/doc/latex/visualfaq/visualFAQ.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}

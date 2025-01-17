Name:		texlive-ethiop-t1
Version:	15878
Release:	2
Summary:	Type 1 versions of Amharic fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/ethiop
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop-t1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop-t1.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These fonts are drop-in Adobe type 1 replacements for the fonts
of the ethiop package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/ethiop-t1/ethiop.map
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/etha10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/etha6.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/etha7.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/etha8.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab11.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab12.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab14.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab18.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab24.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab36.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethab9.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethas10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb11.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb12.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb14.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb18.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb24.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb36.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethasb9.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethatt10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethb10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethb6.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethb7.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethb8.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb11.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb12.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb14.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb18.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb24.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb36.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbb9.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbs10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb10.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb11.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb12.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb14.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb18.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb24.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb36.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbsb9.pfb
%{_texmfdistdir}/fonts/type1/public/ethiop-t1/ethbtt10.pfb
%doc %{_texmfdistdir}/doc/latex/ethiop-t1/COPYING
%doc %{_texmfdistdir}/doc/latex/ethiop-t1/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}

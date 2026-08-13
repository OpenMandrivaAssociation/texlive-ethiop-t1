%global tl_name ethiop-t1
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Type 1 versions of Amharic fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/ps-type1/ethiop
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop-t1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ethiop-t1.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These fonts are drop-in Adobe type 1 replacements for the fonts of the
ethiop package.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ethiop-t1:
MixedMap ethiop.map
TL_DROPIN_EOF

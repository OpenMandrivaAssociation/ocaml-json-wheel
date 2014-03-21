%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for parsing JSON
Name:		ocaml-json-wheel
Version:	1.0.6
Release:	7
License:	BSD
Group:		Development/Other
Url:		http://martin.jambon.free.fr/json-wheel.html
Source0:	http://martin.jambon.free.fr/json-wheel-%{version}.tar.bz2
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-pcre-devel
BuildRequires:	pkgconfig(libpcre)

%description
JSON library for OCaml following RFC 4627.

If you use this library, consider installing ocaml-json-static, the
syntax extension to the language which makes using JSON much easier.

%files
%doc LICENSE
%dir %{_libdir}/ocaml/json-wheel
%{_libdir}/ocaml/json-wheel/META
%{_libdir}/ocaml/json-wheel/*.cma
%{_libdir}/ocaml/json-wheel/*.cmi
%{_bindir}/jsoncat

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE Changes README html
%{_libdir}/ocaml/json-wheel/*.a
%{_libdir}/ocaml/json-wheel/*.cmxa
%{_libdir}/ocaml/json-wheel/*.cmx
%{_libdir}/ocaml/json-wheel/*.mli
%{_libdir}/ocaml/json-wheel/*.ml

#----------------------------------------------------------------------------

%prep
%setup -q -n json-wheel-%{version}

%build
make
strip jsoncat

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p %{buildroot}%{_bindir}

make BINDIR=%{buildroot}%{_bindir} install

# Remove *.cmo and *.o files.  These aren't needed for
# anything because they are included in the *.cma/*.a.
rm %{buildroot}%{_libdir}/ocaml/json-wheel/*.cmo
rm %{buildroot}%{_libdir}/ocaml/json-wheel/*.o




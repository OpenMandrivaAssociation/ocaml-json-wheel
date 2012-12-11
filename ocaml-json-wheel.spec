Name:           ocaml-json-wheel
Version:        1.0.6
Release:        6
Summary:        OCaml library for parsing JSON
License:        BSD
Group:          Development/Other
URL:            http://martin.jambon.free.fr/json-wheel.html
Source0:        http://martin.jambon.free.fr/json-wheel-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  pcre-devel

%description
JSON library for OCaml following RFC 4627.

If you use this library, consider installing ocaml-json-static, the
syntax extension to the language which makes using JSON much easier.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n json-wheel-%{version}

%build
make
strip jsoncat

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p %{buildroot}%{_bindir}

make BINDIR=%{buildroot}%{_bindir} install

# Remove *.cmo and *.o files.  These aren't needed for
# anything because they are included in the *.cma/*.a.
rm %{buildroot}%{_libdir}/ocaml/json-wheel/*.cmo
rm %{buildroot}%{_libdir}/ocaml/json-wheel/*.o

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE
%dir %{_libdir}/ocaml/json-wheel
%{_libdir}/ocaml/json-wheel/META
%{_libdir}/ocaml/json-wheel/*.cma
%{_libdir}/ocaml/json-wheel/*.cmi
%{_bindir}/jsoncat

%files devel
%defattr(-,root,root)
%doc LICENSE Changes README html
%{_libdir}/ocaml/json-wheel/*.a
%{_libdir}/ocaml/json-wheel/*.cmxa
%{_libdir}/ocaml/json-wheel/*.cmx
%{_libdir}/ocaml/json-wheel/*.mli
%{_libdir}/ocaml/json-wheel/*.ml



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 1.0.6-6
+ Revision: 797734
- Rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - relink against libpcre.so.1

* Mon Sep 14 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.6-4mdv2011.0
+ Revision: 440725
- rebuild

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.6-3mdv2010.0
+ Revision: 390244
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.6-2mdv2010.0
+ Revision: 385276
- increm rel nb

* Tue Jan 27 2009 Florent Monnier <blue_prawn@mandriva.org> 1.0.6-1mdv2009.1
+ Revision: 334587
- import ocaml-json-wheel


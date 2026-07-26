%define upstream_name 	 XML-PYX
Name:		perl-%{upstream_name}
Version:	0.07
Release:	6

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-PYX 
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-PYX-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch: 	noarch

%description
%{upstream_name} perl module

%prep
%setup -q  -n %{upstream_name}-%{version}

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%files 
%doc README MANIFEST 
%{perl_vendorlib}/XML/*
%{_mandir}/*/*
%{_bindir}/*

%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 401855
- rebuild using %0.07 Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-10mdv2009.0
+ Revision: 258878
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-9mdv2009.0
+ Revision: 246777
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.07-7mdv2008.1
+ Revision: 136367
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.07-7mdv2007.0
+ Revision: 73519
-Fix Build
- import perl-XML-PYX-0.07-6mdk

* Thu Jul 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.07-6mdk
- rebuild


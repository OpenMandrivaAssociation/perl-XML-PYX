%define module 	XML-PYX
%define version 0.07
%define release %mkrel 10

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Url:		http://search.cpan.org/dist/%{module} 
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
Requires: 	perl 
BuildRequires:	perl(XML::Parser)
BuildRequires:  perl-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch: 	noarch

%description
%{module} perl module


%prep
%setup -q  -n %{module}-%{version}

%build

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT

make PREFIX=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST 
%{perl_vendorlib}/XML/*
%{_mandir}/*/*
%_bindir/*




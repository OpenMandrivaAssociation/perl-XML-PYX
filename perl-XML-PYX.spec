%define upstream_name 	 XML-PYX
%define upstream_version 0.07

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name} 
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(XML::Parser)
Buildarch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
Requires: 	perl 

%description
%{upstream_name} perl module


%prep
%setup -q  -n %{upstream_name}-%{upstream_version}

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

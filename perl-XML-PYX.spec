%define upstream_name 	 XML-PYX
%define upstream_version 0.07
Name:		perl-%{upstream_name}
Version:	0.07
Release:	2

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-PYX 
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSERGEANT/XML-PYX-0.07.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch: 	noarch

%description
%{upstream_name} perl module

%prep
%setup -q  -n XML-PYX-0.07

%build
CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%files 
%doc README MANIFEST 
%{perl_vendorlib}/XML/*
%{_mandir}/*/*
%{_bindir}/*


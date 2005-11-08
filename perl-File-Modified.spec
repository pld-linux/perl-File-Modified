#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Modified
Summary:	File::Modified - checks intelligently if files have changed
Summary(pl):	File::Modified - inteligentne sprawdzanie, czy pliki uleg³y zmianie
Name:		perl-File-Modified
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	271a991b96ccbdaeb7098272c9f97d51
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Modified module is intended as a simple method for programs to
detect whether configuration files (or modules they rely on) have
changed. There are currently two methods of change detection
implemented, mtime and MD5. The MD5 method will fall back to use
timestamps if the Digest::MD5 module cannot be loaded.

There is another module, File::Signature, which has many similar
features, so if this module doesn't do what you need, maybe
File::Signature does. There also is quite some overlap between the two
modules, code wise.

%description -l pl
Modu³ Modified ma s³u¿yæ programom za prost± metodê sprawdzania czy
pliki konfiguracyjne (lub modu³y na których polegaj±) siê zmieni³y.
Aktualnie s± zaimplementowane dwie metody sprawdzania zmian: mtime i
MD5. Metoda MD5 bêdzie dzia³aæ jako mtime je¶li modu³ Digest::MD5
bêdzie niedostêpny.

Istnieje inny modu³ - File::Signature - maj±cy wiele podobnych cech,
wiêc je¶li ten modu³ nie jest tym co potrzeba, mo¿e File::Signature
jest. Modu³y te pokrywaj± siê czê¶ciowo tak¿e pod wzglêdem kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}

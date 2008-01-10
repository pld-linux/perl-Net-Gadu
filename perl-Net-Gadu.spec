#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Gadu Perl module - interface for libgadu.so library
Summary(pl.UTF-8):	Moduł Perla Net::Gadu - interfejs do biblioteki libgadu.so
Name:		perl-Net-Gadu
Version:	1.5
Release:	1
License:	LGPL
Vendor:		Marcin Krzyzanowski
Group:		Development/Languages/Perl
Source0:	http://www.hakore.com/perl/Net-Gadu-%{version}.tar.gz
# Source0-md5:	d6ce1c16095f79e1050491193f8556f2
URL:		http://www.hakore.com/perl/perlgadu.html
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	libgadu-devel >= 1:20020807
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Gadu module is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library (a part
of Ekg project - http://dev.null.pl/ekg/).

%description -l pl.UTF-8
Moduł Net::Gadu pozwala na zastosowanie w swoich skryptach komunikacji
bazującej na protokole Gadu-Gadu. Wykorzystuje bibliotekę libgadu.so,
ktora jest częścią projektu Ekg (http://dev.null.pl/ekg/).

%prep
%setup -q -n Net-Gadu-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ex/ex1 example.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README example.pl contrib
%dir %{perl_vendorarch}/auto/Net/Gadu
%{perl_vendorarch}/auto/Net/Gadu/autosplit.ix
%{perl_vendorarch}/auto/Net/Gadu/Gadu.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Gadu/Gadu.so
%{perl_vendorarch}/Net/Gadu.pm
%{_mandir}/man3/Net::Gadu.3pm*

#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Net::Gadu Perl module - interface for libgadu.so library
Summary(pl):	Modu³ Perla Net::Gadu - interfejs do biblioteki libgadu.so
Name:		perl-Net-Gadu
Version:	0.9
Release:	4
# not mentioned in package, confirmed on IRC
License:	GPL
Vendor:		Marcin Krzyzanowski
Group:		Development/Languages/Perl
Source0:	http://krzak.linux.net.pl/perl/Net-Gadu-%{version}.tar.gz
# Source0-md5:	fab8dd4f0441794181eb0dad7c9ede8e
URL:		http://krzak.linux.net.pl/perl/perlgadu.html
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	libgadu-devel >= 1:20020807
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Gadu module is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library (a part
of Ekg project - http://dev.null.pl/ekg/).

%description -l pl
Modu³ Net::Gadu pozwala na zastosowanie w swoich skryptach komunikacji
bazuj±cej na protokole Gadu-Gadu. Wykorzystuje bibliotekê libgadu.so,
ktora jest czê¶ci± projektu Ekg (http://dev.null.pl/ekg/).

%prep
%setup -q -n Net-Gadu-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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

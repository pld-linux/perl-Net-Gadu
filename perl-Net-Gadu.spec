%include	/usr/lib/rpm/macros.perl
Summary:	Net::Gadu module - interface for libgadu.so library
Summary(pl):	Modu³ Net::Gadu - interfejs do biblioteki libgadu.so
Name:		perl-Net-Gadu
Version:	0.7
Release:	1	
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://krzak.linux.net.pl/perl/Net-Gadu-%{version}.tar.gz
URL:		http://krzak.linux.net.pl/perl/perlgadu.html
BuildRequires:	perl >= 5.6.1
BuildRequires:	libgadu-devel >= 0.9.0.20020605
Requires:	libgadu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::Gadu module is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library (a part
of Ekg project - http://dev.null.pl/ekg/).

%description -l pl
Modu³ Net::Gadu pozwala na zastosowanie w swoich skryptach komunikacji
bazuj±cej na protokole Gadu-Gadu. Wykorzystuje biblioteke libgadu.so
ktora jest czescia projektu Ekg (http://dev.null.pl/ekg/).

%prep
%setup -q -n Net-Gadu-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/doc
install ex/ex1 example.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_sitearch}/auto/Net/Gadu
%{perl_sitearch}/auto/Net/Gadu/*
%{perl_sitearch}/Net/Gadu.pm
%{_mandir}/man3/Net::Gadu.3pm.gz
%doc Changes README example.pl contrib

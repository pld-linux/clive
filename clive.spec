#
# TODO: fix patches and send upstream or abandon them
#
Summary:	Video extraction utility for YouTube and Google Video
Summary(hu.UTF-8):	Videó letöltő a YouTube és a Google Video oldalakról
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube i Google Video
Name:		clive
Version:	2.2.28
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/clive/downloads/list
Source0:	http://downloads.sourceforge.net/clive/%{name}-%{version}.tar.gz
# Source0-md5:	85e6acbe8e6d1398993d32ea2140c560
URL:		http://clive.sourceforge.net/
#Patch0: %{name}-delfi.patch
#Patch1: %{name}-reporter.patch
#Patch2: %{name}-spz.patch
BuildRequires:	perl-tools-pod >= 1:5.8.9
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(URI::Escape) >= 3.29
Requires:	perl-BerkeleyDB >= 0.34
Requires:	perl-Class-Singleton >= 1.4
Requires:	perl-Config-Tiny >= 2.12
Requires:	perl-Digest-SHA >= 5.45
Requires:	perl-Getopt-ArgvFile >= 1.11
Requires:	perl-HTML-TokeParser-Simple >= 2.37
Requires:	perl-IO-Pager >= 0.05
Requires:	perl-WWW-Curl >= 4.0.5
Requires:	perl-XML-Simple >= 2.18
Requires:	perl-base >= 1:5.8.0
Requires:	perl-version >= 0.77
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clive is a video extraction tool for user-uploaded video hosts such as
Youtube, Google Video, Dailymotion, Guba and Metacafe. It can be
chained with 3rd party tools for subsequent video re-encoding and
playing.

%description -l hu.UTF-8
clive egy videó letöltő eszköz felhasználó által feltöltött videó
oldalakhoz, úgymint a YouTube, Google Video, Dailymotion, Guba és
Metacafe. Külső eszközökkel összekapcsolható, videó újrakódolásához és
lejátszásához.

%description -l pl.UTF-8
clive to działający z linii poleceń program do wydobywania filmów z
serwisów YouTube, Google Video i Dailymotion. Obsługuje wyciąganie
osadzonych filmów i może być używany wraz z zewnętrznym koderem (np.
ffmpegiem) do przekodowywania wyciągniętych filmów do innych formatów
(np. AVI, MPEG, flv).

%prep
%setup -q
#%%patch0 -p1
#%%patch1 -p1
#%%patch2 -p1

%build
pod2man bin/clive > clive.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{perl_vendorlib}/clive}
install bin/%{name} $RPM_BUILD_ROOT%{_bindir}
cp -a clive.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a lib/clive/* $RPM_BUILD_ROOT%{perl_vendorlib}/clive

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/clive
%{perl_vendorlib}/clive
%{_mandir}/man1/clive.1*

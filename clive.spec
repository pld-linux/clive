%include	/usr/lib/rpm/macros.perl
Summary:	Video extraction utility for YouTube and Google Video
Summary(hu.UTF-8):	Videó letöltő a YouTube és a Google Video oldalakról
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube i Google Video
Name:		clive
Version:	2.1.14
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://clive.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	ce55bb3b7cfeb679cb457e8a82d78bf3
URL:		http://clive.sourceforge.net/
Patch0:		%{name}-delfi.patch
#Patch1:		%{name}-reporter.patch
#Patch2:	%{name}-spz.patch
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sed >= 4.0
Requires:	perl-BerkeleyDB >= 0.34
Requires:	perl-Config-Tiny >= 2.12
Requires:	perl-HTML-TokeParser-Simple >= 2.37
Requires:	perl-IO-Pager >= 0.05
Requires:	perl-WWW-Curl >= 4.0.5
Requires:	perl-XML-Simple >= 2.18
Requires:	perl-base >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clive is a video extraction tool for user-uploaded video hosts such as
Youtube, Google Video, Dailymotion, Guba and Metacafe. It can be
chained with 3rd party tools for subsequent video re-encoding and
playing and playing.

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
%{__sed} -i -e '1s,#.*perl,#!%{__perl},' clive
%patch0 -p1
##patch1 -p1
#%%patch2 -p1

%build
pod2man clive > clive.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a clive.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES
%attr(755,root,root) %{_bindir}/clive
%{_mandir}/man1/clive.1*

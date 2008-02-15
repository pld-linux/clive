Summary:	Video extraction utility for YouTube and Google Video
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube i Google Video
Name:		clive
Version:	0.4.5
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.gna.org/clive/0.4/src/%{name}-%{version}.tar.gz
# Source0-md5:	d0780d82589975f6226e8974cf737d37
Patch0:		%{name}-setup.patch
Patch1:		%{name}-delfi.patch
Patch2:		%{name}-spz.patch
URL:		http://home.gna.org/clive/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python-urlgrabber >= 2.9.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clive is a command line program that extracts videos from YouTube,
Google Video and Dailymotion websites. It supports embedded video
extraction, and can be used with an external encoder (e.g. ffmpeg) to
re-encode the extracted videos to different video formats (e.g. AVI,
MPEG, flv).

%description -l pl.UTF-8
clive to działający z linii poleceń program do wydobywania filmów z
serwisów YouTube, Google Video i Dailymotion. Obsługuje wyciąganie
osadzonych filmów i może być używany zewnętrznym koderem (np.
ffmpegiem) do przekodowywania wyciągniętych filmów do innych formatów
(np. AVI, MPEG, flv).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/clive
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/clive-*.egg-info
%{_mandir}/man1/clive.1*

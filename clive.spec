Summary:	Video extraction utility for YouTube and Google Video
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube i Google Video
Name:		clive
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.gna.org/clive/0.2/src/%{name}-%{version}.tar.gz
# Source0-md5:	6ba51c2a4f9748079409da39fe5f6b96
URL:		http://home.gna.org/clive/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
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

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

python setup.py install \
        --optimize=2 \
        --root=$RPM_BUILD_ROOT

gzip -d man/*.gz
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/clive.1*

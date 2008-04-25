Summary:	Video extraction utility for YouTube and Google Video
Summary(pl.UTF-8):	Narzędzie do wydobywania filmów z YouTube i Google Video
Name:		clive
Version:	0.4.10
Release:	0.12
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/clive/%{name}-%{version}.tar.bz2
# Source0-md5:	f6aec28af6b7794e2c4c833d80c8284a
Patch0:		%{name}-setup.patch
Patch1:		%{name}-delfi.patch
Patch2:		%{name}-spz.patch
URL:		http://home.gna.org/clive/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python >= 2.4
Requires:	python-feedparser >= 3.3
Requires:	python-snack >= 0.51
Requires:	python-urlgrabber >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clive is a video extraction tool for user-uploaded video hosts such as Youtube,
Google Video, Dailymotion, Guba and Metacafe. It can be chained with 3rd party
tools for subsequent video re-encoding and playing and playing.

%description -l pl.UTF-8
clive to działający z linii poleceń program do wydobywania filmów z
serwisów YouTube, Google Video i Dailymotion. Obsługuje wyciąganie
osadzonych filmów i może być używany zewnętrznym koderem (np.
ffmpegiem) do przekodowywania wyciągniętych filmów do innych formatów
(np. AVI, MPEG, flv).

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

#rm -rf src/clive/{urlgrabber,feedparser,newt}

%{__sed} -i -e 's,\(SUBDIRS = \)urlgrabber feedparser newt,\1,' src/clive/Makefile.am
rm -f configure aclocal.m4
%{__sed} -i -e 's,\(from\|import\) clive.\(newt\|urlgrabber\),\1 \2,' src/clive/*.py
%{__sed} -i -e 's,from clive\.feedparser ,,' src/clive/*.py
%{__sed} -i -e 's,\(import\) clive\.feedparser\.,\1 ,' src/clive/*.py


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--host=%{_arch}-pld-linux \
	--build=%{_arch}-pld-linux \
	--without-newt
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/clive
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]

%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/clive-*.egg-info
%endif
%{_mandir}/man1/clive.1*

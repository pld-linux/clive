Summary:	Video extraction utility for YouTube and Google Video
Name:		clive
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.gna.org/clive/0.2/src/%{name}-%{version}.tar.gz
# Source0-md5:	c95efbae806eca1cce4120552bfdd1b8
URL:		http://home.gna.org/clive/
BuildRequires:	python-devel >= 2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clive is a command line program that extracts videos from YouTube,
Google Video and Dailymotion websites. It supports embedded video
extraction, and can be used with an external encoder (e.g. ffmpeg) to
re-encode the extracted videos to different video formats (e.g. avi,
mpeg, flv).

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

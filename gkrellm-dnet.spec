Summary:	dnet monitor plugin for gkrellm
Summary(pl):	Plugin gkrellm z monitorem dnet
Name:		gkrelldnet
Version:	0.14.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gkrelldnet/%{name}-%{version}.tar.gz
# Source0-md5:	37336d08cccd280fea0cfdc7744ebd32
URL:		http://gkrelldnet.sourceforge.net/
BuildRequires:	gkrellm-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	gkrellm >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A GKrellM plugin which lets you monitor your dnet progress.

%description -l pl
Plugin GKrellM pozwalaj±cy monitorowaæ swoje postêpy w dnet.

%prep
%setup -q -n gkrelldnet

%build
# typo - two different variables for optflags
%{__make} \
	CC="%{__cc}" \
	DBGFLAGS="%{rpmcflags}" \
	DGBFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D gkrelldnet.so  $RPM_BUILD_ROOT%{_libdir}/gkrellm2/plugins/gkrelldnet.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO FAQ
%attr(755,root,root) %{_libdir}/gkrellm2/plugins/gkrelldnet.so

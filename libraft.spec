
Summary: C implementation of the Raft consensus protocol
Name: libraft
Version: 0.9.17
Release: 1%{?dist}
License: LGPLv3
URL: https://github.com/canonical/raft

Source0: https://github.com/canonical/raft/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool

%description
Fully asynchronous C implementation of the Raft consensus protocol.

%package devel
Summary: Development libraries for libraft
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libraft

%prep
%setup -q -n raft-%{version}

%build
autoreconf -i
%configure
%make_build

%install
make DESTDIR=${RPM_BUILD_ROOT} LIBDIR=%{_lib} install

%files
%{_libdir}/%{name}.so*
%exclude %{_libdir}/%{name}.a
%exclude %{_libdir}/%{name}.la

%files devel
%{_libdir}/pkgconfig/raft.pc
%{_includedir}/raft.h
%{_includedir}/raft/

%changelog
* Sun Apr 05 2020 Jan Pazdziora <adelton@fedoraproject.org> - 0.9.17-1
- Initial packaging.

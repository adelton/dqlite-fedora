
Summary: Cooperative multithreading library
Name: libco
Version: 20
Release: 1%{?dist}
License: ISC
URL: https://byuu.org/projects/libco

Source0: https://github.com/canonical/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: autoconf

%description
libco is a cooperative multithreading library written in C89.
Although cooperative multithreading is limited to a single CPU core,
it scales substantially better than preemptive multithreading.
For applications that need 100,000 or more context switches per second,
the kernel overhead involved in preemptive multithreading can end up
becoming the bottleneck in the application. libco can easily scale
to 10,000,000 or more context switches per second.
Ideal use cases include servers (HTTP, RDBMS) and emulators (CPU cores, etc.)

%package devel
Summary: Development libraries for libco
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for libco

%prep
%setup -q

%build
%set_build_flags
%make_build LIBDIR=%{_lib}

%install
make DESTDIR=${RPM_BUILD_ROOT} LIBDIR=%{_lib} install

%files
%{_libdir}/%{name}.so*
%exclude %{_libdir}/%{name}.a

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h

%changelog
* Sun Apr 05 2020 Jan Pazdziora <adelton@fedoraproject.org> - 20-1
- Initial packaging.

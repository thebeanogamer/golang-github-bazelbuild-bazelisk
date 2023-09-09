# Generated by go2rpm 1.9.0
%bcond_without check

# https://github.com/bazelbuild/bazelisk
%global goipath         github.com/bazelbuild/bazelisk
Version:                1.18.0

%gometa -f

%global common_description %{expand:
A user-friendly launcher for Bazel.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           bazelisk
Release:        %autorelease
Summary:        A user-friendly launcher for Bazel

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/bazelisk %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check

# httputil tests are intermittent (https://github.com/bazelbuild/bazelisk/issues/496)
%ifarch x86_64 arm64
%gocheck -d httputil
%else
# Upstream only support x86 and arm64, as that's all Bazel is built for
# Bazelisk actually works fine on any Golang-supported arch, but the tests don't understand this
%gocheck -d core -d httputil
%endif
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog

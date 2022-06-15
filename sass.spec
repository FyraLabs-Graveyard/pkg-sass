# https://file.coffee/u/Gz5mMFn8_KItLQ.jpg
%global debug_package %{nil}
%global __os_install_post %{nil}
%define _build_id_links none
%define version 1.52.1

Name: sass
Version: %{version}
Release: 4%{?dist}
Summary: The reference implementation of Sass, written in Dart
License: MIT
URL: https://sass-lang.com/dart-sass

Source0: https://github.com/sass/dart-sass/archive/refs/tags/%{version}.tar.gz

BuildRequires: dart

%description
Dart Sass is the primary implementation of Sass, which means it gets new features before any other implementation. It's fast, easy to install, and it compiles to pure JavaScript which makes it easy to integrate into modern web development workflows.

%prep
%setup -q -n dart-sass-%{version}
dart pub get

%build
dart compile exe ./bin/sass.dart -o sass

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 sass %{buildroot}%{_bindir}/sass

%files
%{_bindir}/sass
%license LICENSE
%doc README.md
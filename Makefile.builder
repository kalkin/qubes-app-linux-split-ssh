ifeq ($(PACKAGE_SET),dom0)
  RPM_SPEC_FILES := rpm_spec/ssh-split-dom0.spec
else ifeq ($(PACKAGE_SET),vm)
  RPM_SPEC_FILES := rpm_spec/ssh-split.spec
endif

# vim: filetype=make


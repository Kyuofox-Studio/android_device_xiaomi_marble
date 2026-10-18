#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    (
        'vendor/etc/camera/marble_enhance_motiontuning.xml',
        'vendor/etc/camera/marble_motiontuning.xml',
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    'vendor/etc/camera/pureView_parameter.xml': blob_fixup()
        .regex_replace(r'=([0-9]+)>', r'="\1">'),
    'vendor/etc/init/init.embmssl_server.rc': blob_fixup()
        .regex_replace('.*interface.*\n', ''),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace('.+dolby.+\n', ''),
    'vendor/lib64/hw/vendor.xiaomi.sensor.citsensorservice@2.0-impl.so': blob_fixup()
        .binary_regex_replace(
            b'_ZN13DisplayConfig10ClientImpl13ClientImplGetENSt3__112basic_string'
            b'IcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPNS_14ConfigCallbackE',
            b'_ZN13DisplayConfig10ClientImpl4InitENSt3__112basic_string'
            b'IcNS1_11char_traitsIcEENS1_9allocatorIcEEEEPNS_14ConfigCallbackE'
            + b'\x00' * 10,
        ),
}  # fmt: skip

module = ExtractUtilsModule(
    'marble',
    'xiaomi',
    blob_fixups=blob_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

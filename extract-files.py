#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from os import path

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
    'vendor/etc/media_codecs_c2_audio.xml': blob_fixup()
        .regex_replace('.+media_codecs_dolby_audio.+\n', ''),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace('.+dolby.+\n', ''),
    (
        'vendor/bin/hw/android.hardware.security.keymint-service-qti',
        'vendor/lib64/libqtikeymint.so',
    ): blob_fixup()
        .add_needed('android.hardware.security.rkp-V3-ndk.so'),
    'vendor/lib64/libcamximageformatutils.so': blob_fixup()
        .replace_needed(
            'vendor.qti.hardware.display.config-V2-ndk_platform.so',
            'vendor.qti.hardware.display.config-V2-ndk.so',
        ),
}  # fmt: skip

module = ExtractUtilsModule(
    'marble',
    'xiaomi',
    blob_fixups=blob_fixups,
)

if path.isfile(path.join(module.device_path, 'proprietary-firmware.txt')):
    module.add_firmware_proprietary_file()

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()

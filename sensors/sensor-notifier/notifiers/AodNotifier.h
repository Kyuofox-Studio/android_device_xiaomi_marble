//
// SPDX-FileCopyrightText: The LineageOS Project
// SPDX-License-Identifier: Apache-2.0
//

#pragma once

#include <unordered_set>

#include "SensorNotifier.h"

class AodNotifier : public SensorNotifier {
  public:
    AodNotifier(sp<ISensorManager> manager);
    ~AodNotifier();
    inline static std::unordered_set<__u32> activeDisplays{};

  protected:
    void notify();
};

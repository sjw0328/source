# -*- coding: utf-8 -*-
#
# OMEGA X — AI-Driven Windows Latency & Responsiveness Control
#
# Copyright (C) 2026  서주원 (Seo Juwon)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Source code: https://github.com/sjw0328/source
# See the LICENSE file distributed with this source.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
r"""
================================================================================
 OMEGA X v3 — AI-Driven Windows Latency & Responsiveness Control
================================================================================

 이 파일 하나가 앱 전체다(약 15,930줄). 아래 지도를 먼저 읽고 들어갈 것.

 ┌──────────────────────────────────────────────────────────────────────────┐
 │ 지도 갱신법 — 코드를 크게 고쳤으면 아래를 실행해 줄번호를 다시 뽑는다.   │
 │   python -c "import ast,io;s=io.open('dsafg.py',encoding='utf-8').read(); │
 │   [print('%5d-%5d %s'%(n.lineno,n.end_lineno,n.name))                     │
 │    for n in ast.parse(s).body if hasattr(n,'name')]"                      │
 └──────────────────────────────────────────────────────────────────────────┘


 ■ 0. 전체 지도 (줄번호는 대략치 — ±20줄)
 ────────────────────────────────────────────────────────────────────────────
      1 ~   290   이 헤더(FILE MAP)
    293 ~   433   import · 자동 업데이트 활성 조건(UPDATE_ENABLED) · 저장소 상수
    434 ~   469   C{} 색상 팔레트 — 라이트. ★C 는 객체 교체 금지(전역이 참조)★
    470 ~   596   C_DARK 다크 팔레트 · _detect_system_theme · apply_theme ·
                내장 앱 아이콘(APP_ICON_SET · 16~128px) · apply_window_icon
    597 ~   686   버전 단일 진실원(SSOT) — version.txt 강제, 폴백 금지
    687 ~  1640   UpdateChecker — GitHub Releases 무인 업데이트
   1641 ~  2692   TRANSLATIONS{} — EN/KO 각 386키
   2693 ~  2748   I18n 클래스 · Windows UI 언어 감지
   2749 ~  2837   ★AppSettings★ — settings.json 영속(언어·테마·자동화 토글)
                전역 SETTINGS, 그 뒤 I18N/t() 정의
   2838 ~  3012   Windows API 계층 — _sig(ctypes 시그니처) · 최소권한 마스크
                (_open_proc/_close) · RtlGetVersion · _query_cpu_sets(P/E코어)
   3013 ~  3173   상수 블록 — SYSTEM_WHITELIST / SAFE_KEYWORDS /
                NO_DEGRADE_KEYWORDS / RAM_WARN·RAM_CRITICAL / COOLDOWNS
                · 앱 분류 서명(GAME_SIGS · DEV · CREATIVE · BROWSER · OFFICE)
   3174 ~  3227   관리자 권한 — is_admin · UAC 승격 (자동 승격 안 함)
   3228 ~  3307   ErrorLogger · install_global_exception_handler
   3308 ~  3339   파일 저장 유틸
   3340 ~  3384   _DelayScheduler(SCHED) — threading.Timer 전량 대체
   3385 ~  3494   get_foreground_info(0.5s 캐시) · record_perf · proc_is_idle ·
                is_safe_to_modify · is_target(강등 대상 판정 단일 진입점)
   3495 ~  3763   WinPerfCounters — PDH 성능 카운터 수집 스레드
   3764 ~  4116   ThermalMonitor — CPU 온도 관측(PDH 열 구역, 읽기 전용)
                ※못 읽는 PC 가 많다. ok=False 면 UI 에서 항목을 숨긴다.
   4117 ~  4366   ★EcoQoSLedger(ECO)★ — EcoQoS 를 건 프로세스 단일 장부.
                적용/해제/재시도/디스크 영속(크래시 후 다음 실행에서 해제).
   4367 ~  4678   ThermalGovernor — 온도가 높으면 CPU 최대 속도를 단계적
                으로 낮췄다 되돌린다(powercfg PROCTHROTTLEMAX) ·
                auto_thermal_threshold(기준 온도 추정) · thermal_threshold
   4679 ~  4832   _GlobalProcCache + psutil.process_iter 몽키패치 · ppid_map
   4833 ~  4998   ForegroundTracker(FG) — 포그라운드 '프로세스 트리' 보호
   4999 ~  5156   Observer(2.5s 스냅샷) · _median · compute_lpi
   5157 ~  6331   AICore(12특징 소프트맥스) · PolicyEngine · SafetyGuard
   6332 ~  6744   LatencyOptimizer — 구형 액션(스레드 부스트·IO·EcoQoS 등)
   6745 ~  7400   ModernOptimizer — 신형 Windows API 액션(CPU Sets·메모리
                우선순위·타이머 하이재킹 차단·GPU 큐 우선순위)
   7401 ~  9515   ★CoreMode★ — Lite/Hard 연속 최적화 + 측정 + AI 점수(PIS)
                (이 파일에서 가장 자주 손대는 클래스)
   9516 ~  9959   subprocess_run · CleanupEngine · HealthAnalyzer ·
                ★StartupManager(백업/복원 — DeleteValue 전에 반드시 백업)★ ·
                ProcessManager
   9960 ~ 10440   자동화 매니저 — AutoOptimizer · GameAutoDetect ·
                Scheduler · BatterySaver · RamLeakDetector
  10441 ~ 10711   SessionHistory(원자적 JSON) · ReportGenerator(HTML/CSV)
  10712 ~ 15580   OmegaGUI — CustomTkinter UI (4,869줄)
                _confirm(파괴적 액션 공통 관문) · _rebuild_ui(테마 전환) ·
                _update_process_rows(검색·정렬)
  15581 ~ 15930   부팅 경로 — 로딩화면 · 동의 게이트(_require_user_consent) ·
                _run_post_update_selftest · main()


 ■ 1. 부팅 순서 (main 까지 실제로 무슨 일이 일어나는가)
 ────────────────────────────────────────────────────────────────────────────
   import 단계
     └ APP_VERSION = _detect_app_version()
         version.txt 를 못 읽거나 형식이 깨지면 여기서 RuntimeError.
         조용한 폴백은 금지다 — 옛 버전이 정상인 척 위장해 업데이트
         desync 를 만들기 때문. 앱이 안 뜨는 게 맞는 동작이다.
     └ WIN_MAJOR/MINOR/BUILD = RtlGetVersion()  → IS_WIN11 / IS_WIN11_22H2
     └ P_CORE_SETS, E_CORE_SETS = _query_cpu_sets() → IS_HYBRID
     └ psutil.process_iter 를 _patched_process_iter 로 몽키패치
   main()
     └ _show_loading_screen()      로딩 창
     └ _require_user_consent()     EULA 동의(거절 시 종료)
     └ PROC_CACHE.warm_async()     프로세스 목록 첫 워크를 백그라운드로
     └ 인스턴스 생성: WinPerfCounters → Observer → AICore → PolicyEngine
                      → SafetyGuard → LatencyOptimizer → CoreMode
     └ OmegaGUI(root, ...) → _build_skeleton() → _start_background()
     └ root.mainloop()


 ■ 2. AI 점수(PIS)가 만들어지는 경로 — 가장 자주 손대는 곳
 ────────────────────────────────────────────────────────────────────────────
   CoreMode.start_continuous(mode)
     └ _baseline_full = _measure_full()          세션 시작 기준선
     └ _cont_loop() 스레드 시작 (Lite 3s / Hard 4s, 첫 3사이클은 1.5s)
          └ _run_cycle(mode)
               ├ HOLDOUT_EVERY(40) 사이클마다 → _run_holdout_cycle()
               │    최적화를 전부 풀고 1초간 '대조군' 측정
               │    → _holdout_samples 에 적재(최대 5개)
               ├ FG.refresh() → _release_fg_tree()   포그라운드 트리 해제
               ├ 액션 실행 (아래 3번 참조)
               ├ current_full = _measure_full()
               ├ ref = _pis_reference()      홀드아웃 중앙값(없으면 baseline)
               ├ pis = _compute_pis(ref, current_full)
               └ status_cb(stats) → _ui_queue → _ui_pump(200ms)
               └ _sample_ui_data(1s, 별도 스레드) → _ui_data → 갱신 콜백
                                  → _apply_improve_stats() → 화면 갱신

   _measure_full() 이 재는 것
     cpu_pct       _sample_sys_cpu()  전용 cpu_times 스냅샷(구간 오염 없음)
     ram_used_mb   virtual_memory()
     bg_cpu_pct    _sample_bg_cpu()   상위 40개 + 직전 표본 pid 만
                                      (OMEGA X 자신은 제외 → self_cpu_pct)
                                      cpu_times 델타 직접 측정,
                                      FG.is_protected 로 포그라운드 트리 제외
     cpu_queue     PDH \System\Processor Queue Length
     disk_busy     PDH \PhysicalDisk(_Total)\% Idle Time 의 반전
     hard_faults   PDH \Memory\Pages Input/sec   ← 하드 폴트만
     pdh_ok        PDH 수집이 살아있는지

   _compute_pis() 규칙 (50 = 변화 없음)
     · 전 컴포넌트를 '상대 변화율(%)'로 계산 — 코어 수·RAM 용량 무관
     · 측정 불가하거나 양쪽이 상시 0 인 컴포넌트는 0점이 아니라 '제외'
       (0점으로 넣으면 가중치만 잡아먹고 점수를 50 으로 끌어내린다)
     · 남은 컴포넌트로 가중치 재정규화 → 신뢰도 감쇠 0.6+0.4*(측정수/5)
     · 기본 가중치 memory .30 / bg_cpu .30 / responsive .18 /
                   disk .10 / thrashing .12

   ★건드리면 안 되는 원칙★
     점수·개선% 에 '액션을 몇 개 실행했는가', '프로필을 감지했는가'
     같은 항목을 다시 넣지 말 것. 과거에 그게 들어 있어서 시스템이
     나빠져도 점수가 55점 밑으로 못 내려갔다. 앱이 자기 성능 악화를
     구조적으로 볼 수 없게 만드는 최악의 결함이다. 실측만 쓴다.


 ■ 3. 최적화 액션 목록 (누가 무엇을 하는가)
 ────────────────────────────────────────────────────────────────────────────
   LatencyOptimizer (구형)
     thread_burst        포그라운드 프로세스 ABOVE_NORMAL 지속 부스트
     io_priority_boost   포그라운드 IO 우선순위 High (20초 레이트리밋)
     bg_throttle         백그라운드 우선순위 강등
     apply_ecoqos        백그라운드 EcoQoS(저클럭/E코어)
     timer_burst         timeBeginPeriod(1) — 참조계수 1:1 페어링 필수
     idle_cleanup        EmptyWorkingSet (RAM 경고 이상일 때만)
     mmcss_register      ※정직한 no-op. AvSetMmThreadCharacteristics 는
                          '호출한 스레드'를 등록하므로 게임이 아니라
                          OMEGA X 워커가 등록됐다. 효과 0 이라 비활성.
     affinity_hint       ※no-op. 전 스레드를 코어0 으로 몰아 오히려 경합.

   ModernOptimizer (신형 — 부작용이 작고 되돌리기가 확실함)
     set_cpu_set_preference / apply_core_split
                         하이브리드 CPU 에서 FG=P코어 / BG=E코어 소프트힌트
                         (IS_HYBRID=False 면 실행 안 됨. 정상)
     lower_bg_memory_priority
                         EmptyWorkingSet 대체. 페이지를 뺏지 않고
                         '부족하면 여기부터 회수하라'고 표시만 → 하드폴트 0
     block_timer_hijack  Win11 PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION
     gpu_priority_boost  D3DKMTSetProcessSchedulingPriorityClass (게임/크리에이티브)
     set_self_efficiency 최소화 시 자기 자신을 EcoQoS 로

   UsagePredictor (PREDICT) — 앱 전환 패턴을 세어 다음에 쓸 앱을 예측.
     로딩 중인 앱을 미리 준비하는 데만 쓴다. app_patterns.json 에 영속.

   ActionLearner (LEARN) — 액션별 무작위 보류로 이 PC 에서의 효과를
     측정하고, 효과 없는 액션은 스스로 중단한다. learned.json 에 영속.
     판정의 귀결(계속 실행 / 실행 중단 / 번갈아 시험)은 학습 카드에
     그대로 적는다 — 판정만 보여주고 동작을 안 적으면 반쪽이다.

   ActivityLog (ACTLOG) — 실행 기록. 실행(run)/실패(fail)/건너뜀(skip)/
     사이클 요약(cycle)을 남긴다. 메모리 400줄 + activity.log(512KB 회전).
     화면은 '실제로 실행한 작업' 카드(정지 후에도 남음, 복사 가능).

   ThermalGovernor (온도 기반 — 기본 꺼짐, 설정에서 켬)
     최대 프로세서 상태 100→90→80→70% 단계 조정(powercfg).
     되돌리기 경로 3중: guard.record / thermal_cap.json / _on_closing.

   CoreMode 자체 액션
     _trim_bg_processes / _compact_standby /
     _pause_bg_services / _disable_gamedvr / _set_power_high /
     _throttle_bg_cpu / _apply_ecoqos_bulk

   모든 되돌릴 수 있는 변경은 SafetyGuard.record(action, target, restore_fn)
   에 등록된다. 앱 종료 시 _on_closing → rollback_all() 로 전부 원복.


 ■ 4. 이 파일에서 반드시 지켜야 할 함정 목록
 ────────────────────────────────────────────────────────────────────────────
  (1) ★OmegaGUI 는 ctk.CTk 를 상속하지 않는다★
  (2) ★_GlobalProcCache._FULL_ATTRS 에 "ppid" 를 넣지 말 것★
  (3) ★psutil 의 Windows status 는 "running" / "stopped" 뿐이다★
  (4) ★PDH 카운터 선택★
  (5) ★SAFE_KEYWORDS 와 NO_DEGRADE_KEYWORDS 는 다르다★
  (6) ★OpenProcess 는 최소 권한으로★
  (7) ★ctypes argtypes/restype 을 반드시 선언★
  (8) ★threading.Timer 를 새로 만들지 말 것★
  (9) ★워커 스레드에서 Tk 를 직접 건드리지 말 것★
  (10) ★속성명 _root 금지★
  (11) ★빌드 시 version.txt 를 반드시 번들에 포함★
  (12) ★C(색상 팔레트) 딕셔너리 객체를 교체하지 말 것★
  (13) ★위젯 색은 생성 시점에 굳는다★
  (14) ★되돌릴 수 없는 액션은 반드시 _confirm() 을 거칠 것★
  (15) ★StartupManager.disable 은 백업 없이 지우지 말 것★
  (16) ★사용자 설정은 SETTINGS(AppSettings)로만 저장★
  (17) ★온도로 건드려도 되는 것은 딱 하나★
  (18) ★EcoQoS 해제는 ControlMask=0 / StateMask=0★
  (19) ★상대 변화율은 분모가 작으면 거짓말을 한다★
  (20) ★Tk 스레드에서는 아무것도 재지 말 것★
  (21) ★'몇 % 빨라졌나' 는 정직하게 답할 수 없는 질문이다★
  (22) ★대조군은 반드시 '같은 시간대'에 있어야 한다★
  (23) ★학습은 '가끔 하지 않아야' 성립한다★
  (24) ★예측은 '이미 시작된 것'을 앞당기는 데만 쓴다★
  (25) ★'안 하는 것'과 '새로 안 거는 것'은 다르다 — 학습기의 전제★
  (26) ★판정은 같은 시간대끼리 비교해서만 낸다★
  (27) ★모르는 원래값을 추측해서 되돌리지 말 것★
  (28) ★EcoQoS 를 거는 곳이 셋이면 푸는 곳도 셋이어야 한다★
  (29) ★고정 앵커로 전/후를 비교하면 오래 켤수록 반드시 '차이 없음'★
  (30) ★데드밴드는 '작은 변화' 를 거를 뿐 '남의 탓' 을 못 거른다★
  (31) ★적응형 기준값은 저장하지 않으면 매 실행 죽는다★
  (32) ★액션이 안 걸린 사이클은 표본이 아니다 — 버리지도 말고 세지도 말 것★
  (33) ★해제 대기열은 '읽고 지우기' 로 만들지 말 것★
  (34) ★그룹 재배정은 assign 과 색인 기준을 맞출 것★
  (35) ★'검증할 수 없다' 를 '검증했다' 로 적지 말 것★
  (36) ★검증한 파일과 실행할 파일은 같은 파일이 아니다★
  (37) ★코드 서명은 업데이터가 확인하지 않으면 절반만 한 것이다★
  (38) ★실행만 적는 로그는 없는 로그와 같다★
  (39) ★예외를 삼키는 것은 괜찮다. 삼킨 사실이 안 남는 것이 문제다★
  (40) ★선정 기준과 측정 기준이 모순되면 판정은 영원히 0 이다★
  (41) ★데드밴드를 산포로 잡으면 표본을 모을수록 손해다★
  (42) ★비교군은 라벨이 아니라 상태로 정한다★

  ※ 상세는 docs/ARCHITECTURE.md 에 있다. 이 절은 색인이다 — 새 함정을
    추가할 때는 여기 한 줄, 그 문서에 항목 하나를 같이 적는다.
    번호는 다시 쓰지 않는다(폐기해도 번호는 비워둘 것).

 ■ 4-1. CoreMode(7401~9513) 내부 지도
 ────────────────────────────────────────────────────────────────────────────
   측정        _measure_ram_used / _sample_bg_cpu / _sample_sys_cpu /
               _measure_full
   점수        PIS_WEIGHTS / _rel_drop / _compute_pis
   대조군      HOLDOUT_EVERY / _release_all_soft / _run_holdout_cycle /
               _pis_reference / _build_stats_snapshot
   액션        _trim_bg_processes / _throttle_bg_cpu / _restore_all_nice /
               _set_ecoqos / _apply_ecoqos_bulk / _release_fg_tree /
               _revert_ecoqos_all / _disable_gamedvr / _pause_bg_services /
               _set_power_high / _restore_power_scheme /
               _compact_standby / _flush_dns / _enable_privilege
   1회 실행    run_lite / run_hard
   연속 모드   start_continuous / stop_continuous / _cont_loop /
               _detect_profile / _run_cycle      ← 사이클 본체
   정리        _prune_timers / _trim_system_cache


 ■ 5. 모드 정의
 ────────────────────────────────────────────────────────────────────────────
   Lite Core   가벼운 액션, 완전 되돌림. 사이클 3초.
   Hard Core   프로필별 심층 튜닝(게임/크리에이티브/개발/브라우저).
               사이클 4초. admin 권장.
   두 모드 모두 '연속 토글' 방식이며, 중지 시 EcoQoS·우선순위·전원계획을
   전부 원복한다.


 ■ 6. 색상 팔레트 (3색만)
 ────────────────────────────────────────────────────────────────────────────
   흰색 #FFFFFF 배경 / 검정 #1A1A1A 텍스트 / 파랑 #0066FF 강조
   전부 아래 C{} 딕셔너리 한 곳에만 정의된다. 색을 바꾸려면 거기만 고칠 것.
================================================================================
"""

# ─── Lazy imports (deferred to first use) ─────────────────────────────
import os
import re
import sys
import time
import math
import threading
import ctypes
import json
import platform
from ctypes import wintypes
from datetime import datetime, timedelta
from pathlib import Path
from collections import deque, defaultdict

# Heavy imports (still needed at top, but minimal)
import customtkinter as ctk
import psutil

# Auto-update system imports
# 업데이트 로직은 PyInstaller 로 빌드된 EXE 에서만 동작한다.
# python 스크립트로 실행 중일 때는 교체 대상이 python.exe 가 되므로 비활성.
try:
    import requests
    from packaging import version as pkg_version
    _UPDATE_DEPS_OK = True
except ImportError:
    _UPDATE_DEPS_OK = False

# 업데이트는 PyInstaller 로 빌드된 EXE 에서만 동작한다.
# (python 스크립트로 실행 중이면 설치 대상이 모호하므로 비활성)
# 개발 중 업데이트 흐름을 시험하려면 환경변수 OMEGA_FORCE_UPDATE=1 을 설정.
UPDATE_ENABLED = _UPDATE_DEPS_OK and (
    bool(getattr(sys, "frozen", False))
    or os.environ.get("OMEGA_FORCE_UPDATE") == "1"
)

GITHUB_REPO = "sjw0328/Lite"
# 포터블 EXE 우선 (Setup은 별도 설치 흐름)
UPDATE_PORTABLE_NAMES = ("OMEGA_X.exe", "OMEGA_X_LITE.exe")


# ══════════════════════════════════════════════════════════════════════
# DIAGNOSTICS — 삼킨 예외를 세는 곳 (PATCH27)
# ══════════════════════════════════════════════════════════════════════
# 이 파일에는 예외를 삼키는 자리가 270곳 넘게 있다. 대부분은 없애면 안
# 되는 것들이다 — 열거와 접근 사이에 프로세스가 죽고(NoSuchProcess),
# PPL 은 관리자여도 못 열고(AccessDenied), 위젯이 파괴된 뒤 타이머가 한
# 번 더 돈다(TclError). 이건 정상 동작이지 오류가 아니다.
#
# ★문제는 삼키는 것이 아니라 삼킨 사실이 안 남는 것이었다★
# 그래서 이 둘을 구별할 방법이 없었다:
#   (a) 정상 — 프로세스 하나가 죽어서 건너뜀 (사이클당 두어 번)
#   (b) 고장 — API 이름이 틀려 273곳이 전부 실패 (사이클당 수백 번)
# 화면에는 둘 다 '아무 일도 안 일어남' 으로 보인다. 패치20 의 flip_done
# 유실과 패치23 의 캐리오버가 정확히 이렇게 몇 주를 버텼다.
#
# 설계 원칙
#  · 동작을 바꾸지 않는다. 여전히 삼킨다. 세기만 한다.
#  · 예외 경로에서 불린다 = 뜨거운 루프에서 초당 수백 번 불릴 수 있다.
#    그래서 사이트당 상세는 DETAIL_N 회까지만 남기고 이후는 카운터만.
#  · 진단이 앱을 죽이면 진단이 없느니만 못하다. q() 자체는 절대 던지지
#    않는다 — 이 파일에서 유일하게 정당한 조용한 삼킴이 그 한 곳이다.
#  · 줄번호는 저장하지 않고 예외의 트레이스백에서 읽는다. 코드가 밀려도
#    안 틀린다(사이트 ID 를 줄번호로 만들면 다음 패치에 전부 거짓말이 된다).
class Diagnostics:
    DETAIL_N = 3          # 사이트당 상세(줄번호·메시지)는 처음 이만큼만
    MAX_SITES = 600       # 사이트 폭발 방지(정상이면 300 안쪽)

    def __init__(self):
        self._lk = threading.RLock()
        self._sites = {}
        self._t0 = time.time()

    def q(self, site, exc):
        """삼킨 예외 하나를 기록한다. 절대 예외를 던지지 않는다."""
        try:
            kind = type(exc).__name__
            with self._lk:
                d = self._sites.get(site)
                if d is None:
                    if len(self._sites) >= self.MAX_SITES:
                        return
                    d = self._sites[site] = {"n": 0, "kinds": {}, "line": 0,
                                             "msg": "", "last": 0.0}
                d["n"] += 1
                d["last"] = time.time()
                d["kinds"][kind] = d["kinds"].get(kind, 0) + 1
                if d["n"] <= self.DETAIL_N:
                    tb = getattr(exc, "__traceback__", None)
                    while tb is not None and tb.tb_next is not None:
                        tb = tb.tb_next
                    if tb is not None:
                        d["line"] = tb.tb_lineno
                    d["msg"] = str(exc)[:120]
        except Exception:
            # ★여기만은 조용해야 한다★ 진단이 앱을 멈추면 안 된다.
            pass

    def total(self):
        with self._lk:
            return sum(d["n"] for d in self._sites.values())

    def rows(self):
        """많이 삼킨 순서. (사이트, 횟수, 종류문자열, 줄, 메시지)"""
        with self._lk:
            items = [(k, dict(v)) for k, v in self._sites.items()]
        out = []
        for k, v in items:
            kinds = ", ".join("%s x%d" % (a, b) for a, b in
                              sorted(v["kinds"].items(), key=lambda x: -x[1])[:3])
            out.append((k, v["n"], kinds, v["line"], v["msg"]))
        out.sort(key=lambda r: -r[1])
        return out

    def text(self, top=60):
        rows = self.rows()
        mins = max(1.0, (time.time() - self._t0) / 60.0)
        head = ["OMEGA X diagnostics",
                "uptime %.1f min | swallowed %d at %d sites | rate %.1f/min"
                % (mins, self.total(), len(rows), self.total() / mins),
                "-" * 72]
        for site, n, kinds, line, msg in rows[:top]:
            head.append("%6d  %-44s L%-6d %s" % (n, site[:44], line, kinds))
            if msg:
                head.append("        %s" % msg[:100])
        if not rows:
            head.append("(none)")
        return "\n".join(head)

    def reset(self):
        with self._lk:
            self._sites.clear()
            self._t0 = time.time()


DIAG = Diagnostics()


# ============================================================================
# COLOR PALETTE — White + Black + Blue only
# ============================================================================
C = {
    "bg":           "#FFFFFF",
    "panel":        "#F8F9FA",
    "card":         "#FFFFFF",
    "border":       "#E5E7EB",
    "border_soft":  "#F0F1F3",
    "sidebar":      "#FAFBFC",
    "sidebar_hov":  "#F0F7FF",
    "sidebar_act":  "#E6F0FF",

    "text":         "#1A1A1A",
    "text_2":       "#4B5563",
    "text_3":       "#9CA3AF",
    "text_4":       "#D1D5DB",

    "blue":         "#0066FF",
    "blue_dark":    "#0052CC",
    "blue_light":   "#E6F0FF",
    "blue_subtle":  "#F0F7FF",
    "blue_pale":    "#F5F9FF",

    "btn_primary":   "#0066FF",
    "btn_primary_h": "#0052CC",
    "btn_sec":       "#F0F7FF",
    "btn_sec_h":     "#E6F0FF",
    "btn_danger":    "#FFE5E5",
    "btn_danger_h":  "#FFCCCC",
    "danger_text":   "#DC2626",
    "warn_text":     "#F59E0B",
}

# ─── 다크 팔레트 ────────────────────────────────────────────────────
# ★C 는 객체를 바꾸지 말 것★ — 파일 전역이 C["key"] 로 참조하므로
# 새 딕셔너리를 대입하면 이미 만들어진 참조가 옛 색을 계속 본다.
# apply_theme() 은 C.clear() + C.update() 로 내용만 갈아끼운다.
C_LIGHT = dict(C)
C_DARK = {
    "bg":           "#14161A",
    "panel":        "#1C1F26",
    "card":         "#1A1D23",
    "border":       "#2C313A",
    "border_soft":  "#22262E",
    "sidebar":      "#101216",
    "sidebar_hov":  "#1B2430",
    "sidebar_act":  "#16233A",

    "text":         "#F3F4F6",
    "text_2":       "#C0C6D0",
    "text_3":       "#8A93A0",
    "text_4":       "#4A515C",

    "blue":         "#4C93FF",
    "blue_dark":    "#2C6FD1",
    "blue_light":   "#1B2942",
    "blue_subtle":  "#16202F",
    "blue_pale":    "#131A26",

    "btn_primary":   "#3B8BFF",
    "btn_primary_h": "#2C6FD1",
    "btn_sec":       "#1B2430",
    "btn_sec_h":     "#22303F",
    "btn_danger":    "#3A1D1D",
    "btn_danger_h":  "#4A2424",
    "danger_text":   "#F87171",
    "warn_text":     "#FBBF24",
}


def _detect_system_theme():
    """Windows 앱 테마 설정(AppsUseLightTheme)을 읽는다."""
    try:
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        val, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return "light" if val else "dark"
    except Exception:
        return "light"


def apply_theme(mode):
    """mode: "light" | "dark" | "system". 실제 적용된 모드를 반환."""
    resolved = _detect_system_theme() if mode == "system" else mode
    if resolved not in ("light", "dark"):
        resolved = "light"
    C.clear()
    C.update(C_DARK if resolved == "dark" else C_LIGHT)
    try:
        ctk.set_appearance_mode(resolved)
    except Exception as _dx:
        DIAG.q("module.apply_theme#0", _dx)
    return resolved


# ─── 창 아이콘 ──────────────────────────────────────────────────────
# 소스 파일 하나만 배포해도 아이콘이 나오도록 64x64 PNG 를 내장한다.
# (없으면 작업표시줄·Alt+Tab 에 Tk 기본 깃털 아이콘이 뜬다.)
# ★패치33 — 아이콘 다중 해상도★ 한 장을 늘려 쓰면 16px 자리에서
#   Ω 가 뭉개진다. 크기별로 따로 그렸다 — 128/48/32 는 안티에일리어싱,
#   16 은 픽셀을 손으로 찍은 것(이 크기에서 축소 알고리즘은 무조건 뭉갠다).
#   32색 팔레트 PNG — RGBA 로 두면 128px 한 장이 base64 8KB 다.
#   인스톨러용 .ico 는 여기서 못 만든다 — omega_x.ico 를 따로 둔다.
APP_ICON_128_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAAflBMVEUAZv/+/v8AAAAAXP8Tcf/W5v8Af/80hP9tp/9Cjf9Rlf+Muf8AZv8AVf8AZv8AZv+20/8AAP8AZv+oyv8ne/8AZ//g7P/H3f+bw/8AZf8A//97sP8AZ/9gn/8AP/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACkwNv8AAAAIHRSTlP+/wD///8C//////+uA1DM/wGJ//8p////GwH/Zv8EANFxeUkAAAQHSURBVHja1VvZeqsgEB5lc981SZv2/R/zkHQzCApInJz/ol8vAvPLrDIOxArKN/lnvHZFDQFRF101yo15qcoDRfxNehdU9oxFN36LMBHgPI6rAp6IovqSoicguVU1PBl19XgIMwKf8aWAA1BcYq4h0PK4goNQxbxVCbzxuIPD0P0xgN/nL+BAFL8MAEX+jUHZ/hE4Xv7fGdwJHKr/mR38ECiPs/9HXyi/CPC3C6DgIl3vRqA83gB+DfFGAEkBP0oAqYEai0AtdQAc7wDuMVkSqPEI1JJAPAIiRmkDHSaBThLw1ACRAKASP/976aCF0Us40DQ5N4xFEow15ySl4EVihKu7eBD5KVrglAtwp3CFzl06iwxg7hw6qN3EZ020iiZzo+BmgSQ9RZs4peRJLkOGPrJCPzyHQhJZI3nC40MfOaCHwIdABIucwERQBiSLnJEFZECSyAMJwZUfjoGv/FAMfPQf1A6GaAeGAASM/nfKk1QMg0iT3Bih2X4F5KakcysAyHdpAtSUpPKdSiCpdtvzoFYfhAxn7U/3piadAhp9siFDE1wJ5N3JubQO+77nCOhyv2ktyBMxLVfQoBbI6OoDEcpC2iHVyN9cw8IdgUal27UOGQJGZOYTWpeh29cRiPDT5tJyPIuTxUaT7copkBkyz9y2UIKnDoT/Nip1EcQH7I15x9L5Lr2/O6sBpCcBTKBx2IQ0AYyA7jjGhQ5oABsUhy02+JLb8v3VKflQKkC35UqV+EF2e2HjtIVqhR5+qAbisxuB8+5grFZjbq6sBpH3//EE0G0A3Quw4wB6JMTPBejZEL0eQK+I0GtC/KoY/b0A/c0I/d3wBd6Ose8H8G9I0O+I8G/JDPeEhsAmwt8TGm5K9Wegv9bfe1OquytmDseV77+wZ9ZdAE1nYf9tuaZfsFKZnJ7RL1g8l7DPHt4dEzKDymCtulFKMSn/YSdb6SDSOTLxUJyt9UTJQ+TqRfawkV1vn0C+3iQ9mxMSofl6OzWn28nMokdr9IJ0u4u1GRasemR6BssCRoet4uRks4khv0w2SyfHasa+F2bbYF0tT4jlRwLaANfYrW2ck5+tDmy7qUEICKvixcWAnGxQv8lkt3RyTb62NmBrP+svqsLfkm09aD1B2T2GIcs3+53A0gwNWZ5aWMG0XSNvngEzZiO6eQaNRY1O0n7lFKYmW1ucra1lvW5tralG7h9K6rHx2aLz2hoQv6n9ItDhEuigwiVQwYhLYIQW1Qjq9gU+bMb+tJtjjTfcUNy/rkf+vD/mHG/AgfNXGPFAH3KROsAa8+H8NQad8Ee98Ifd4vZwQyza+bgf/sDjnQHqyOfRQ69lizv2+/mag89HjX7fx+txht+vW8PvGOP//wCepDQaIqu4BwAAAABJRU5ErkJggg=="
)
APP_ICON_48_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAMAAABg3Am1AAAAflBMVEUAZv/9/f8AXP8AAABBjf+JuP8AVv9spv8zhP8AZP8AZ/8le/8AZv8adP9+sf+31P/Y6P+oy/9Slv8Af/+Zwv/F3P8AZ//h7v9gnv8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABdYziPAAAAIHRSTlP+//8A//8G//8vjf/P////////Av//Ev//AAAAAAAAANuK/WwAAAGMSURBVHjalVZbloMgDI2hiIKIaK3d/0oHCygvHbkfek7eCQkBCCEtIT0f4BYD73+CBPZfy+EBeLtrgPn08AxDb4ThubyB0YDlAxX4LEB4jQIn0EMVeig4QAQphNz/uQvI6o+S6akxmDSTmUpBnDYBqMT7EPHbJPjeaiBtMlCsk7/TQOZlJk2pzXwHu9DAzgmozlTU1LRTjtBdaKzeIPrzcC7XsoOX5c6BOZwt7VVygbqQoiuDLsZkjT2jnim/E1v4vkrbJTinCvNVZXG0plK6dTzi1SmLlC6uTtuFlAbrUiuFVA72IrUzWJUqqHJqO6ZCTC6i6aa311J/lTvc1qPRIc22S167aHzUwRbqnxHa4oHxFrai+R1iSzL81WETP2aiwMZxpEzFAVgXilHDZDIUl1M49e+4vTy6rIdPFoZl8wjPdI1ZNms/n8dVkrX2AVdXGVOj2dK5g9SFSlrvdeC8f1Ge1C69v/FAdjwheQBet4F4/cqqXopVa3dol9rFvtQ/HSoeJx/7OKl8/vwB/TINGgHW8PIAAAAASUVORK5CYII="
)
APP_ICON_32_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAflBMVEUAZv/7/f8AW/+exf9ppf8AAAAAWf8AZ/82hf9Tlv+Kuf+myv8Vcf8le//i7v8AZf8AZ/8AZ/9Cjf+81/97sP8AYv8AY/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADu5rBCAAAAIHRSTlP+/////wAK1f////////87fID///9BEgAAAAAAAAAAAE1i/ksAAAD3SURBVHjahVMHDoMwDHScDQmjtP3/UxvsQhaCk5A4+zzBoI02q4UL2CW5NBj9uXSTZNYG9AduMKcMcAsDa0kR+clYoWgAo5LbJlUsJKU7SPGHDNgXQzeJE5PD3i8q9AqKH1wIbqAcbYIhh3GyoU4RyrSsCFUCnyzjGYNjoh7bCtlC+qoGhcTMY5VwF+w7cpnvTchK8O5LvCvBK1m2LNgSfWG3J3WMqfpNkU0oJvyO9X9Ac0x5aSOW/0X0yqszijpOBuXKqRnUWEOPDyXEfzkNPaZm7DUaSvCSoa6o5SEY50wntbDc38UC31u/Tac3P52enh+O9+H8fw66B1ftwCDtAAAAAElFTkSuQmCC"
)
APP_ICON_16_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAflBMVEUAZv8AAAD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADT6BLuAAAAIHRSTlP/AP8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEHeujQAAABBSURBVHjajY9BDgAgCMOm/3+0OLYE5GIPKDUgYD2AQUigcAUaFjsoIhNGCj3yvMI5zZ8YPeImATf1t1kyRp/LdQ5N9gCZEwN1xQAAAABJRU5ErkJggg=="
)

# 큰 것부터. Tk 8.6 은 iconphoto 에 여러 장을 받아 자리별로 골라 쓴다.
APP_ICON_SET = (APP_ICON_128_B64, APP_ICON_48_B64,
                APP_ICON_32_B64, APP_ICON_16_B64)
# 하위 호환 — 예전 이름으로 참조하는 곳이 있을 수 있다.
APP_ICON_B64 = APP_ICON_128_B64


def apply_window_icon(win):
    """Toplevel/Tk 창에 앱 아이콘을 건다. 실패해도 앱은 계속 돈다."""
    try:
        import tkinter as _tk
        imgs = []
        for _d in APP_ICON_SET:      # 큰 것부터 — 자리에 맞는 크기를 Tk 가 고른다
            try:
                imgs.append(_tk.PhotoImage(master=win, data=_d))
            except Exception as _dx:
                DIAG.q("module.apply_window_icon#1", _dx)
        if not imgs:
            return
        # 참조를 창에 붙여두지 않으면 GC 되어 아이콘이 사라진다.
        win._omega_icon = imgs
        win.iconphoto(True, *imgs)
    except Exception as _dx:
        DIAG.q("module.apply_window_icon#0", _dx)


# ============================================================================
# CONSTANTS
# ============================================================================
APP_NAME = "OMEGA X"

# ─── 라이선스 (GPL-3.0-or-later) ───────────────────────────────────
# GPL 제5조·제3조 5항(d)는 프로그램이 대화형으로 동작할 때
# '적절한 법적 고지(Appropriate Legal Notices)'를 표시할 것을 요구한다.
# = 저작권 표시 + 무보증 고지 + 재배포 조건 안내 + 라이선스 사본 위치.
# 아래 값을 설정 화면 라이선스 카드와 사용 동의 화면에서 함께 노출한다.
# ※GPL 은 상업적 이용을 금지하지 않는다. '비상업 전용' 문구를 다시
#   넣으면 라이선스 자체와 모순되므로 절대 추가하지 말 것.
LICENSE_ID     = "GPL-3.0-or-later"
COPYRIGHT_LINE = "Copyright (C) 2026  서주원 (Seo Juwon) / OMEGA SYSTEMS"
LICENSE_URL    = "https://www.gnu.org/licenses/gpl-3.0.html"
SOURCE_URL     = "https://github.com/sjw0328/source"
# 최초 실행 시 표시하는 사용 동의/면책 고지의 버전.
# 고지 내용을 의미있게 바꾸면 이 값을 올려 재동의를 받는다.
EULA_VERSION = "4"

def _is_valid_version_string(v):
    """버전 문자열이 'x.y' 또는 'x.y.z' (각 부분 숫자) 형식인지 검증.
    'v1.0' 같은 접두사는 호출 전에 제거되어 있어야 한다.
    이상한 값(빈 문자열, 'None', 깨진 BOM 잔재 등)을 버전으로
    오인하지 않도록 형식 자체를 막는다."""
    if not isinstance(v, str):
        return False
    v = v.strip()
    if not v:
        return False
    parts = v.split(".")
    if len(parts) < 2 or len(parts) > 4:
        return False
    return all(p.isdigit() for p in parts)


def _detect_app_version():
    """버전 단일 출처(version.txt)에서 읽는다. ★ 단일 진실원(SSOT) ★

    setup.iss 도 같은 version.txt 를 읽으므로, 이 파일 한 줄만 고치면
    EXE 가 창에 표시하는 버전 == 인스톨러 버전 이 되어 desync 가 불가능하다.

    설계 원칙 (대표님 요구사항):
      - 빌드되든 소스로 실행되든, 버전은 '오직 version.txt' 에서만 온다.
      - version.txt 를 못 읽거나 형식이 깨졌으면 폴백하지 않고 '즉시 실패'.
        조용한 폴백/하드코딩 기본값은 옛 버전을 정상으로 위장시켜
        desync 를 만들기 때문에 절대 금지한다.
      - 실패 시 raise -> 앱이 실행되지 않음. 그래야 대표님이 즉시 안다.

    PyInstaller 빌드 시 version.txt 를 반드시 번들에 포함할 것:
        --add-data "version.txt;."   (build_exe.bat / .spec 양쪽 모두)
    """
    base = getattr(sys, "_MEIPASS", None)
    frozen = bool(getattr(sys, "frozen", False))

    if frozen:
        # 번들(EXE) 상태: _MEIPASS 안의 version.txt '만' 신뢰원으로 인정.
        # 설치 폴더에 굴러다니는 옛 version.txt 를 절대 읽지 않는다.
        if not base:
            raise RuntimeError(
                "frozen 상태인데 _MEIPASS 가 없습니다. 번들이 손상되었습니다."
            )
        candidate = os.path.join(base, "version.txt")
        try:
            with open(candidate, encoding="utf-8-sig") as f:
                v = f.read().strip()
        except OSError as e:
            raise RuntimeError(
                "번들된 version.txt 를 읽지 못했습니다. PyInstaller 빌드 시 "
                "--add-data \"version.txt;.\" 가 누락되었습니다. (" + str(e) + ")"
            )
    else:
        # 소스 실행(개발 중): 스크립트 옆 version.txt 만 허용.
        try:
            here = os.path.dirname(os.path.abspath(__file__))
        except Exception:
            here = os.getcwd()
        candidate = os.path.join(here, "version.txt")
        try:
            with open(candidate, encoding="utf-8-sig") as f:
                v = f.read().strip()
        except OSError as e:
            raise RuntimeError(
                "version.txt 를 찾을 수 없습니다. dsafg.py 와 같은 폴더에 "
                "version.txt (예: 한 줄에 1.0.4) 를 두십시오. (" + str(e) + ")"
            )

    # 형식 검증: 빈 값/깨진 값을 버전으로 오인하지 않는다.
    v_clean = v.lstrip("vV").strip()
    if not _is_valid_version_string(v_clean):
        raise RuntimeError(
            "version.txt 의 내용이 올바른 버전 형식이 아닙니다: " + repr(v)
            + "  (예: 1.0.4 처럼 숫자와 점으로만 작성하십시오.)"
        )
    return v_clean


# version.txt 가 없거나 깨졌으면 여기서 RuntimeError 가 발생하여
# 모듈 import 단계에서 앱이 멈춘다 = 잘못된 버전으로 실행되는 일이 없다.
APP_VERSION = _detect_app_version()

GITHUB_API_HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": f"OMEGA-X-Updater/{APP_VERSION}",
}


# ============================================================================
# AUTO-UPDATE CHECKER (GitHub Releases)
# ============================================================================
class UpdateChecker:
    """GitHub Releases 기반 자동 업데이트 (무인 설치 버전).

    동작: 최신 Release 확인 -> 인스톨러(.exe) %TEMP% 다운로드 ->
          /SILENT 무인 설치 -> 인스톨러가 파일 교체 + 앱 재시작.
    PowerShell 미사용. 모든 단계를 %TEMP%\\omega_update.log 에 기록한다.

    설치 결과 판정(nonce 방식):
      - 업데이트 시작 시 1회용 nonce 를 생성해 pending 파일에 저장하고,
        인스톨러에 /UPDATENONCE=<nonce> 로 전달한다.
      - 인스톨러는 설치 완료(ssDone) 시 done 파일에 동일 nonce 를 기록한다.
      - 재시작 후 두 nonce 가 일치하면 성공으로 판정한다.
      => 같은 버전으로 테스트해도(1.0.3 -> 1.0.3) 정확히 판정된다.
    """

    # /releases/latest 는 pre-release 를 무시한다(404 위험).
    # /releases 목록을 받아 최신 릴리스를 직접 고른다.
    GITHUB_API_RELEASES = f"https://api.github.com/repos/{GITHUB_REPO}/releases"

    # 무인 설치 인자. /SILENT 는 진행바만 표시(클릭 불필요).
    SILENT_ARGS = "/SILENT /SUPPRESSMSGBOXES /NORESTART"

    # PATCH25_RELEASE_GATE: 마지막 실패 사유. 로그와 별개로 UI 가 읽을 수 있게 남긴다.
    #   ""=없음 / no_digest / tampered / unsigned / wrong_signer
    _last_error = ""

    # ----- 진단 로그 -----
    @staticmethod
    def _log_path():
        import tempfile
        # UI 안내 문자열(update_log_hint)과 반드시 동일한 파일명을 사용한다.
        return os.path.join(tempfile.gettempdir(), "omega_update.log")

    @staticmethod
    def _log(msg):
        """업데이트 전 과정을 로그 파일에 남긴다. 절대 예외를 던지지 않는다."""
        try:
            import datetime
            p = UpdateChecker._log_path()
            mode = "a"
            try:
                if os.path.isfile(p) and os.path.getsize(p) > 65536:
                    mode = "w"
            except OSError as _dx:
                DIAG.q("UpdateChecker._log#0", _dx)
            with open(p, mode, encoding="utf-8") as f:
                f.write(f"[{datetime.datetime.now():%Y-%m-%d %H:%M:%S}] {msg}\n")
        except Exception as _dx:
            DIAG.q("UpdateChecker._log#1", _dx)
        try:
            print(f"[Update] {msg}")
        except Exception as _dx:
            DIAG.q("UpdateChecker._log#2", _dx)

    # ----- 버전 정규화 -----
    @staticmethod
    def _normalize_version(v):
        """v1.0 / V1.1 / 1.0.0-beta 등 -> 비교용 'x.y.z'."""
        v = str(v).strip().lstrip("vV").strip()
        v = v.split("-")[0].split("+")[0]
        if not v:
            return "0.0.0"
        parts = [p if p.isdigit() else "0" for p in v.split(".")[:3]]
        while len(parts) < 3:
            parts.append("0")
        return ".".join(parts)

    @staticmethod
    def _force_mode():
        """OMEGA_FORCE_UPDATE=1 이면 버전이 같거나 낮아도 업데이트로 취급(테스트용)."""
        return os.environ.get("OMEGA_FORCE_UPDATE") == "1"

    # ----- 보안: 다운로드 URL 검증 -----
    @staticmethod
    def _is_trusted_download_url(url):
        u = str(url or "")
        if not u.startswith("https://"):
            return False
        trusted = (
            f"https://github.com/{GITHUB_REPO}/",
            "https://objects.githubusercontent.com/",
            f"https://api.github.com/repos/{GITHUB_REPO}/",
        )
        return any(u.startswith(p) for p in trusted)

    # ----- 다운로드 파일 검증 -----
    @staticmethod
    def _validate_pe(path):
        try:
            with open(path, "rb") as f:
                return f.read(2) == b"MZ"
        except OSError:
            return False

    @staticmethod
    def _verify_sha256(path, expected):
        """파일의 SHA-256 이 expected 와 일치하면 True.
        expected 는 'sha256:<hex>' 또는 순수 hex 둘 다 허용.
        sha256 이 아닌 알고리즘이 지정되면(드묾) 검증을 통과시키지 않고
        호출부가 '다이제스트 없음'처럼 처리하도록 None 이 아닌 False 대신
        관대하게 True 를 주지 않는다 → 안전 우선."""
        try:
            import hashlib
            exp = str(expected or "").strip().lower()
            if ":" in exp:
                algo, _, hexpart = exp.partition(":")
                if algo != "sha256":
                    # ★PATCH25 fail-closed★ 예전에는 여기서 True 를 돌려줬다.
                    # '검증할 수 없다' 를 '검증했다' 로 바꿔 읽는 것이라,
                    # GitHub 가 다이제스트 알고리즘을 하나만 바꿔도 무결성
                    # 검사가 통째로 무력화된다. 모르면 거부한다.
                    UpdateChecker._log(
                        f"지원하지 않는 다이제스트 알고리즘({algo}) - 검증 불가로 거부")
                    return False
                exp = hexpart.strip()
            if not re.fullmatch(r"[0-9a-f]{64}", exp or ""):
                # 형식이 SHA-256 hex 가 아니면 대조 자체가 성립하지 않는다.
                UpdateChecker._log("다이제스트 형식이 SHA-256 hex 가 아님 - 거부")
                return False
            h = hashlib.sha256()
            with open(path, "rb") as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b""):
                    h.update(chunk)
            actual = h.hexdigest().lower()
            ok = (actual == exp)
            if not ok:
                UpdateChecker._log(f"해시 기대 {exp[:16]}… / 실제 {actual[:16]}…")
            return ok
        except Exception as e:
            UpdateChecker._log(f"SHA-256 검증 예외: {e}")
            return False

    # ----- PATCH25_RELEASE_GATE: 다이제스트 폴백 해석 -----
    # GitHub 가 asset.digest 를 안 줄 경우에 대비한 2·3순위 경로.
    #   1순위  asset.digest            (현재 GitHub 가 항상 제공)
    #   2순위  같은 릴리스의 SHA256SUMS / <파일명>.sha256 자산
    #   3순위  릴리스 본문(body)의 64자리 hex
    # ★한계를 분명히 해둔다★ 셋 다 같은 GitHub 계정 아래 있으므로,
    #   이 검증은 '전송 중 변조·CDN 오염·자산 바꿔치기' 만 막는다.
    #   계정 자체가 털린 경우는 못 막는다. 그건 코드 서명의 몫이다
    #   (아래 _verify_authenticode / REQUIRE_SIGNED_INSTALLER).
    @staticmethod
    def _resolve_digest(chosen, rel):
        d = str(chosen.get("digest") or "").strip()
        if d:
            return d
        asset_name = str(chosen.get("name") or "")
        # 2순위: 체크섬 자산
        try:
            for a in (rel.get("assets") or []):
                nm = str(a.get("name") or "")
                low = nm.lower()
                if not (low.endswith(".sha256") or "sha256sums" in low
                        or low.endswith(".sha256sum")):
                    continue
                url = a.get("browser_download_url", "")
                if not UpdateChecker._is_trusted_download_url(url):
                    continue
                r = requests.get(
                    url, timeout=20,
                    headers={"User-Agent": GITHUB_API_HEADERS["User-Agent"]})
                if r.status_code != 200 or len(r.content) > 65536:
                    continue
                for line in r.text.splitlines():
                    m = re.search(r"\b([0-9a-fA-F]{64})\b", line)
                    if not m:
                        continue
                    # 파일명이 같은 줄에 있으면 그 줄을, 없으면 단일 해시 파일로 본다.
                    if asset_name and asset_name.lower() in line.lower():
                        UpdateChecker._log(f"다이제스트 출처: 체크섬 자산 {nm}")
                        return "sha256:" + m.group(1).lower()
                    if line.strip() == m.group(1):
                        UpdateChecker._log(f"다이제스트 출처: 체크섬 자산 {nm}")
                        return "sha256:" + m.group(1).lower()
        except Exception as e:
            UpdateChecker._log(f"체크섬 자산 조회 실패: {e}")
        # 3순위: 릴리스 본문
        try:
            body = str(rel.get("body") or "")
            cands = re.findall(r"\b([0-9a-fA-F]{64})\b", body)
            if len(cands) == 1:
                UpdateChecker._log("다이제스트 출처: 릴리스 본문")
                return "sha256:" + cands[0].lower()
            if len(cands) > 1:
                UpdateChecker._log(
                    f"릴리스 본문에 64자리 hex 가 {len(cands)}개 - 어느 것인지 "
                    f"알 수 없어 사용하지 않음")
        except Exception as _dx:
            DIAG.q("UpdateChecker._resolve_digest#0", _dx)
        return ""

    # ----- PATCH25_RELEASE_GATE: 인스톨러 디지털 서명 검증 -----
    # 코드 서명 인증서를 붙이기 전까지 REQUIRE_SIGNED_INSTALLER 는 False 다.
    # False 이면 검증 결과를 로그에만 남기고 설치를 막지 않는다(= 지금 상태).
    # 인증서를 도입한 뒤 EXPECTED_SIGNER_CN 을 채우고 True 로 바꾸면,
    # 서명이 없거나 발행자가 다른 인스톨러는 해시가 맞아도 실행하지 않는다.
    # ★이 스위치를 켜기 전까지는 '코드 서명 도입' 이 절반만 된 것이다★
    #   서명은 SmartScreen 을 달래주지만, 업데이터가 서명을 확인하지 않으면
    #   자동 업데이트 경로는 여전히 계정 탈취에 무방비다.
    REQUIRE_SIGNED_INSTALLER = False
    EXPECTED_SIGNER_CN = ""      # 예: "Open Source Developer, Seo Juwon"

    @staticmethod
    def _verify_authenticode(path):
        """반환 (trusted: bool, subject: str, detail: str).

        WinVerifyTrust 로 체인·서명을 검증하고 서명자 CN 을 읽는다.
        실패해도 절대 예외를 던지지 않는다 — 업데이트 경로를 이 함수의
        버그로 막지 않기 위해서다.
        """
        try:
            import ctypes
            from ctypes import wintypes

            class GUID(ctypes.Structure):
                _fields_ = [("d1", ctypes.c_ulong), ("d2", ctypes.c_ushort),
                            ("d3", ctypes.c_ushort), ("d4", ctypes.c_ubyte * 8)]

            action = GUID(0x00AAC56B, 0xCD44, 0x11D0,
                          (ctypes.c_ubyte * 8)(0x8C, 0xC2, 0x00, 0xC0,
                                               0x4F, 0xC2, 0x95, 0xEE))

            class WTFI(ctypes.Structure):
                _fields_ = [("cbStruct", wintypes.DWORD),
                            ("pcwszFilePath", wintypes.LPCWSTR),
                            ("hFile", wintypes.HANDLE),
                            ("pgKnownSubject", ctypes.c_void_p)]

            class WTD(ctypes.Structure):
                _fields_ = [("cbStruct", wintypes.DWORD),
                            ("pPolicyCallbackData", ctypes.c_void_p),
                            ("pSIPClientData", ctypes.c_void_p),
                            ("dwUIChoice", wintypes.DWORD),
                            ("fdwRevocationChecks", wintypes.DWORD),
                            ("dwUnionChoice", wintypes.DWORD),
                            ("pFile", ctypes.POINTER(WTFI)),
                            ("dwStateAction", wintypes.DWORD),
                            ("hWVTStateData", wintypes.HANDLE),
                            ("pwszURLReference", wintypes.LPWSTR),
                            ("dwProvFlags", wintypes.DWORD),
                            ("dwUIContext", wintypes.DWORD),
                            ("pSignatureSettings", ctypes.c_void_p)]

            fi = WTFI(ctypes.sizeof(WTFI), os.path.abspath(path), None, None)
            wd = WTD()
            wd.cbStruct = ctypes.sizeof(WTD)
            wd.dwUIChoice = 2            # WTD_UI_NONE
            wd.fdwRevocationChecks = 0   # WTD_REVOKE_NONE — 오프라인 오탐 방지
            wd.dwUnionChoice = 1         # WTD_CHOICE_FILE
            wd.pFile = ctypes.pointer(fi)
            wd.dwStateAction = 1         # WTD_STATEACTION_VERIFY
            wd.dwProvFlags = 0x00000010  # WTD_SAFER_FLAG

            wintrust = ctypes.windll.wintrust
            wintrust.WinVerifyTrust.restype = ctypes.c_long
            hwnd = wintypes.HANDLE(-1)   # INVALID_HANDLE_VALUE = UI 없음
            rc = wintrust.WinVerifyTrust(hwnd, ctypes.byref(action),
                                         ctypes.byref(wd))
            wd.dwStateAction = 2         # WTD_STATEACTION_CLOSE
            try:
                wintrust.WinVerifyTrust(hwnd, ctypes.byref(action),
                                        ctypes.byref(wd))
            except Exception as _dx:
                DIAG.q("UpdateChecker._verify_authenticode#0", _dx)

            code = rc & 0xFFFFFFFF
            if rc != 0:
                known = {
                    0x800B0100: "서명 없음",
                    0x800B0109: "신뢰되지 않는 루트",
                    0x800B0101: "인증서 만료",
                    0x80096010: "파일이 변조됨(해시 불일치)",
                }
                return False, "", known.get(code, f"0x{code:08X}")
            return True, UpdateChecker._signer_cn(path), "OK"
        except Exception as e:
            return False, "", f"검증 예외: {e}"

    @staticmethod
    def _signer_cn(path):
        """서명자 인증서의 Subject CN. 실패하면 빈 문자열."""
        try:
            import ctypes
            from ctypes import wintypes
            crypt32 = ctypes.windll.crypt32

            CERT_QUERY_OBJECT_FILE = 1
            CERT_QUERY_CONTENT_FLAG_PKCS7_SIGNED_EMBED = 1 << 10
            CERT_QUERY_FORMAT_FLAG_BINARY = 1 << 1
            CMSG_SIGNER_INFO_PARAM = 6
            CERT_NAME_SIMPLE_DISPLAY_TYPE = 4
            X509_ASN_ENCODING = 0x1
            PKCS_7_ASN_ENCODING = 0x10010000
            ENC = X509_ASN_ENCODING | PKCS_7_ASN_ENCODING

            hstore = ctypes.c_void_p()
            hmsg = ctypes.c_void_p()
            ok = crypt32.CryptQueryObject(
                CERT_QUERY_OBJECT_FILE, ctypes.c_wchar_p(os.path.abspath(path)),
                CERT_QUERY_CONTENT_FLAG_PKCS7_SIGNED_EMBED,
                CERT_QUERY_FORMAT_FLAG_BINARY, 0,
                None, None, None,
                ctypes.byref(hstore), ctypes.byref(hmsg), None)
            if not ok:
                return ""
            try:
                size = wintypes.DWORD(0)
                if not crypt32.CryptMsgGetParam(
                        hmsg, CMSG_SIGNER_INFO_PARAM, 0, None,
                        ctypes.byref(size)) or size.value == 0:
                    return ""
                buf = ctypes.create_string_buffer(size.value)
                if not crypt32.CryptMsgGetParam(
                        hmsg, CMSG_SIGNER_INFO_PARAM, 0, buf,
                        ctypes.byref(size)):
                    return ""

                class BLOB(ctypes.Structure):
                    _fields_ = [("cbData", wintypes.DWORD),
                                ("pbData", ctypes.POINTER(ctypes.c_byte))]

                class CERT_INFO(ctypes.Structure):
                    _fields_ = [("dwVersion", wintypes.DWORD),
                                ("SerialNumber", BLOB),
                                ("_pad", ctypes.c_byte * 0)]

                # CMSG_SIGNER_INFO 의 앞 세 필드만 필요하다.
                class SIGNER_INFO_HEAD(ctypes.Structure):
                    _fields_ = [("dwVersion", wintypes.DWORD),
                                ("Issuer", BLOB),
                                ("SerialNumber", BLOB)]

                si = ctypes.cast(buf,
                                 ctypes.POINTER(SIGNER_INFO_HEAD)).contents

                class CERT_ID_INFO(ctypes.Structure):
                    _fields_ = [("Issuer", BLOB), ("SerialNumber", BLOB)]

                idinfo = CERT_ID_INFO(si.Issuer, si.SerialNumber)
                CERT_FIND_SUBJECT_CERT = 0x000B0000
                ctx = crypt32.CertFindCertificateInStore(
                    hstore, ENC, 0, CERT_FIND_SUBJECT_CERT,
                    ctypes.byref(idinfo), None)
                if not ctx:
                    return ""
                try:
                    n = crypt32.CertGetNameStringW(
                        ctx, CERT_NAME_SIMPLE_DISPLAY_TYPE, 0, None, None, 0)
                    if n <= 1:
                        return ""
                    out = ctypes.create_unicode_buffer(n)
                    crypt32.CertGetNameStringW(
                        ctx, CERT_NAME_SIMPLE_DISPLAY_TYPE, 0, None, out, n)
                    return out.value or ""
                finally:
                    try:
                        crypt32.CertFreeCertificateContext(ctx)
                    except Exception as _dx:
                        DIAG.q("UpdateChecker._signer_cn#0", _dx)
            finally:
                try:
                    crypt32.CertCloseStore(hstore, 0)
                except Exception as _dx:
                    DIAG.q("UpdateChecker._signer_cn#1", _dx)
        except Exception:
            return ""
        return ""

    @staticmethod
    def _safe_remove(path):
        try:
            if path and os.path.exists(path):
                os.remove(path)
        except OSError as _dx:
            DIAG.q("UpdateChecker._safe_remove#0", _dx)

    @staticmethod
    def _cleanup_temp_installers(keep=None):
        """%TEMP% 에 남은 'OMEGA X 업데이트용' 임시 파일만 골라 지운다.

        ★ %TEMP% 폴더 전체를 지우지 않는다 ★
        %TEMP% 에는 윈도우와 다른 모든 프로그램의 임시 파일이 들어 있어,
        통째로 지우면 다른 프로그램이 깨지거나 시스템이 불안정해진다.
        그래서 OMEGA X 가 만든 파일만 이름 패턴으로 정확히 골라낸다.

        지우는 대상 (%TEMP% 안, OMEGA X 가 만든 것만):
          - OMEGA_X_LITE_Setup*.exe       : 이전에 받아둔 인스톨러
          - OMEGA_X*Setup*.exe            : 인스톨러 이름 변형 포괄
          - OMEGA_X*Setup*.exe.* (.tmp 등): 받다 만 잔여 조각
          - omega_build_selftest.txt      : 빌드 자가검증 잔여물
        보존하는 것:
          - omega_update.log              : 진단 로그(대표님이 봐야 함)
          - omega_x_update_pending.txt    : 진행 표식(판정에 필요)
          - keep 으로 지정된 경로          : 지금 막 받아 실행할 인스톨러

        ★ 이 함수가 desync 를 막는 핵심이다 ★
        같은 버전 번호로 인스톨러를 다시 빌드해 GitHub 에 올리면,
        %TEMP% 에 같은 이름의 옛 인스톨러가 남아 있게 된다. 새로 받을 때
        그 파일이 잠겨 있거나 권한 문제로 덮어쓰기가 실패하면, 앱이
        '옛 인스톨러' 를 실행해버려 옛 버전이 다시 깔린다.
        다운로드 직전에 이 함수로 옛 인스톨러를 먼저 없애면 그 경합 자체가
        사라진다 -> 0.1% 의 desync 가능성도 차단.
        """
        import tempfile
        import glob
        keep_norm = os.path.normcase(os.path.abspath(keep)) if keep else None
        tmp = tempfile.gettempdir()
        patterns = (
            "OMEGA_X_LITE_Setup*.exe",
            "OMEGA_X*Setup*.exe",
            "OMEGA_X_LITE_Setup*.exe.*",
            "OMEGA_X*Setup*.exe.*",
            "omega_build_selftest.txt",
        )
        removed = 0
        seen = set()
        for pat in patterns:
            try:
                matches = glob.glob(os.path.join(tmp, pat))
            except Exception:
                matches = []
            for p in matches:
                ap = os.path.normcase(os.path.abspath(p))
                if ap in seen:
                    continue
                seen.add(ap)
                # 지금 실행할 인스톨러는 절대 건드리지 않는다.
                if keep_norm and ap == keep_norm:
                    continue
                # 안전장치: tmp 폴더 바깥 경로는 건너뛴다(패턴 오류 방어).
                if not ap.startswith(os.path.normcase(os.path.abspath(tmp))):
                    continue
                try:
                    os.remove(p)
                    removed += 1
                except OSError as _dx:
                    # 파일이 잠겨 있으면(인스톨러 실행 중 등) 건너뛴다.
                    # 다음 업데이트 때 다시 정리 시도된다.
                    DIAG.q("UpdateChecker._cleanup_temp_installers#0", _dx)
        if removed:
            UpdateChecker._log(
                f"%TEMP% 의 옛 OMEGA X 인스톨러/잔여물 {removed}개 정리")
        return removed

    # ----- 결과 판정용 파일 경로 -----
    @staticmethod
    def _pending_path():
        """업데이트 진행 표식. 비승격(현재 사용자)으로 쓰고 읽는다 -> %TEMP%."""
        import tempfile
        return os.path.join(tempfile.gettempdir(), "omega_x_update_pending.txt")

    @staticmethod
    def _done_path():
        """인스톨러(승격됨)가 쓰고 앱이 읽는다. 모든 사용자 공용 경로 사용.
        ProgramData 는 표준 사용자도 읽기 가능하므로 권한 토큰 차이의 영향이 없다."""
        base = os.environ.get("PROGRAMDATA") or os.environ.get(
            "ALLUSERSPROFILE") or r"C:\ProgramData"
        return os.path.join(base, "OMEGA X", "omega_x_update_done.txt")

    @staticmethod
    def _reboot_pending_path():
        """'설치는 됐지만 EXE 교체가 재부팅으로 밀린' 상태 표식. %TEMP%.
        이게 있으면 같은 버전으로 자동 재시도를 멈춰 무한 반복을 막는다."""
        import tempfile
        return os.path.join(tempfile.gettempdir(),
                            "omega_x_update_reboot_pending.txt")

    @staticmethod
    def _set_reboot_pending(target_version):
        try:
            with open(UpdateChecker._reboot_pending_path(), "w",
                      encoding="utf-8") as f:
                f.write(str(target_version or "").strip())
        except OSError as _dx:
            DIAG.q("UpdateChecker._set_reboot_pending#0", _dx)

    @staticmethod
    def _get_reboot_pending():
        try:
            p = UpdateChecker._reboot_pending_path()
            if os.path.isfile(p):
                with open(p, encoding="utf-8") as f:
                    return f.read().strip()
        except OSError as _dx:
            DIAG.q("UpdateChecker._get_reboot_pending#0", _dx)
        return ""

    @staticmethod
    def _clear_reboot_pending():
        UpdateChecker._safe_remove(UpdateChecker._reboot_pending_path())

    @staticmethod
    def _make_nonce():
        import time as _t
        import random
        return f"{int(_t.time())}{random.randint(0x100000, 0xFFFFFF):06x}"

    @staticmethod
    def _version_from_asset_name(name):
        """인스톨러 파일명에서 실제 버전 문자열을 추출한다.

        예) 'OMEGA_X_LITE_Setup_v1_0_4.exe' -> '1.0.4'
            'OMEGA_X_LITE_Setup_v1.1.0.exe' -> '1.1.0'
        파일명은 build_exe.bat 가 version.txt 로부터 자동으로 만들기
        때문에, 사람이 손으로 입력하는 릴리스 태그보다 신뢰할 수 있는
        '실제 설치될 버전' 의 출처다. 추출 실패 시 '' 를 반환한다.
        """
        import re
        nm = re.sub(r"\.exe$", "", str(name or ""), flags=re.IGNORECASE)
        # 끝쪽의  v1_0_4 / v1.1.0 / 1_0_4  형태를 우선적으로 찾는다.
        m = re.search(r"[vV]?(\d+[._]\d+(?:[._]\d+)?)\s*$", nm)
        if m is None:
            m = re.search(r"[vV](\d+[._]\d+(?:[._]\d+)?)", nm)
        if m is None:
            return ""
        ver = m.group(1).replace("_", ".")
        return ver if _is_valid_version_string(ver) else ""

    @staticmethod
    def _version_key(v):
        """버전 문자열을 비교 가능한 정수 튜플로 바꾼다. '1.0.4' -> (1,0,4).
        릴리스/자산 중 '가장 높은 버전' 을 고를 때 쓴다."""
        nv = UpdateChecker._normalize_version(v)
        parts = []
        for x in str(nv).split("."):
            try:
                parts.append(int(x))
            except ValueError:
                parts.append(0)
        return tuple(parts)

    # ----- 최신 버전 조회 -----
    @staticmethod
    def get_latest_version():
        """GitHub 의 모든 게시된(비-draft) 릴리스에서 '인스톨러' 자산을
        전부 훑어, 파일명 버전이 가장 높은 것 하나를 고른다.

        예전 코드는 '목록의 첫 릴리스 -> 그 안의 첫 .exe 자산' 을 골랐다.
        그러나 GitHub /releases 는 '버전순' 이 아니라 '생성일순' 이고,
        한 릴리스에 인스톨러를 여러 개 올리면 업로드순 첫 번째가 잡힌다.
        그래서 1.0.5 를 올려도 1.0.4 가 선택되는 일이 생긴다(대표님 증상).
        -> 릴리스/자산 순서에 일절 의존하지 않고, 모든 인스톨러 중에서
           '파일명 버전이 최대' 인 것을 고른다. 무엇을 어디에 올리든 항상
           가장 높은 버전이 정확히 선택된다.
        성공: dict(version,url,notes,filename,is_setup) / 실패: None.
        """
        if not UPDATE_ENABLED:
            UpdateChecker._log("UPDATE_ENABLED=False - 빌드된 EXE 가 아님")
            return None
        try:
            UpdateChecker._log(f"릴리스 목록 요청: {UpdateChecker.GITHUB_API_RELEASES}")
            r = requests.get(UpdateChecker.GITHUB_API_RELEASES,
                             headers=GITHUB_API_HEADERS, timeout=12)
            UpdateChecker._log(f"HTTP {r.status_code}")
            if r.status_code == 403:
                UpdateChecker._log("403 - GitHub API 사용량 초과(시간당 60회)")
                return None
            if r.status_code != 200:
                UpdateChecker._log(f"API 실패 HTTP {r.status_code} - 저장소명 확인")
                return None
            releases = r.json()
            if not isinstance(releases, list) or not releases:
                UpdateChecker._log("릴리스가 하나도 없음")
                return None

            # 모든 비-draft 릴리스 x 모든 자산 을 훑어 인스톨러를 수집하고,
            # 파일명 버전이 가장 높은 것을 고른다.
            best = None     # (버전키, 버전str, asset, release)
            seen = 0
            for rel in releases:
                if rel.get("draft", False):
                    continue
                for a in (rel.get("assets", []) or []):
                    nm = a.get("name") or ""
                    low = nm.lower()
                    if not (low.endswith(".exe")
                            and ("setup" in low or "install" in low)):
                        continue
                    seen += 1
                    url = a.get("browser_download_url", "")
                    if not UpdateChecker._is_trusted_download_url(url):
                        UpdateChecker._log(f"신뢰할 수 없는 URL 무시: {url}")
                        continue
                    fv = UpdateChecker._version_from_asset_name(nm)
                    if not fv:
                        UpdateChecker._log(f"파일명에서 버전을 못 읽어 무시: {nm}")
                        continue
                    key = UpdateChecker._version_key(fv)
                    if best is None or key > best[0]:
                        best = (key, fv, a, rel)

            if best is None:
                UpdateChecker._log(
                    f"인스톨러를 찾지 못함(.exe + 이름에 'setup'/'install' + "
                    f"파일명에 버전 + 신뢰 URL). 검사한 후보 {seen}개. "
                    f"build_exe.bat 가 만든 Setup 인스톨러를 릴리스에 올려야 함.")
                return None

            _, resolved_ver, chosen, rel = best
            asset_name = chosen.get("name", "OMEGA_X_LITE_Setup.exe")
            tag_ver = (rel.get("tag_name") or "").lstrip("vV").strip()
            UpdateChecker._log(
                f"인스톨러 선택: {asset_name} "
                f"(버전 {resolved_ver}, 릴리스 태그 {tag_ver or '?'})")
            if (tag_ver and UpdateChecker._normalize_version(tag_ver)
                    != UpdateChecker._normalize_version(resolved_ver)):
                UpdateChecker._log(
                    f"[주의] 릴리스 태그({tag_ver}) != 인스톨러 파일명 "
                    f"버전({resolved_ver}). 파일명 버전을 사용합니다.")
            UpdateChecker._log(f"확정된 최신 버전: {resolved_ver}")

            return {
                "version": resolved_ver,
                "url": chosen.get("browser_download_url", ""),
                "notes": rel.get("body", "") or "",
                "filename": asset_name,
                "is_setup": True,
                # GitHub 가 자산에 대해 제공하는 무결성 다이제스트
                # (예: "sha256:abcd..."). 있으면 다운로드 후 대조한다.
                "digest": UpdateChecker._resolve_digest(chosen, rel),
            }
        except Exception as e:
            UpdateChecker._log(f"최신 버전 확인 예외: {e}")
            return None

    @staticmethod
    def has_update():
        """업데이트 존재 여부. 반환: (bool, latest_dict | None).
        OMEGA_FORCE_UPDATE=1 이면 버전 비교를 건너뛰고 유효한 릴리스를
        무조건 업데이트로 취급한다(동일 버전 테스트용)."""
        if not UPDATE_ENABLED:
            return False, None
        latest = UpdateChecker.get_latest_version()
        if not latest:
            return False, None
        if UpdateChecker._force_mode():
            UpdateChecker._log("OMEGA_FORCE_UPDATE=1 - 버전 비교 생략, 강제 업데이트")
            return True, latest
        try:
            lv = UpdateChecker._normalize_version(latest["version"])
            cv = UpdateChecker._normalize_version(APP_VERSION)
            newer = pkg_version.parse(lv) > pkg_version.parse(cv)
            UpdateChecker._log(
                f"버전 비교: 현재 {cv} vs 최신 {lv} -> "
                + ("업데이트 있음" if newer else "이미 최신"))
            if newer:
                return True, latest
        except Exception as e:
            UpdateChecker._log(f"버전 비교 예외: {e}")
        return False, None

    # ----- 재시작 후 결과 안내 -----
    @staticmethod
    def check_startup_update_message():
        """인스톨러 재시작 후 호출. 'success'/'failed'/None 반환.

        판정 순서:
          1) pending 파일 없음 -> 업데이트 시도 안 했음 -> None
          2) done 파일의 nonce 가 pending 의 nonce 와 일치 -> 'success'
          3) (nonce 불일치하더라도) 현재 APP_VERSION 이 목표 버전과 같고
             직전 버전과 다르면 -> 'success' (done 파일을 못 읽는 환경 대비)
          4) 그 외 -> 'failed'
        판정 후 pending 파일은 항상 삭제하고, 성공 시 다운로드한
        인스톨러도 정리한다.
        """
        try:
            pending = UpdateChecker._pending_path()
            if not os.path.isfile(pending):
                return None

            old_version = target_version = nonce = installer = ""
            try:
                with open(pending, encoding="utf-8") as f:
                    raw = [ln.rstrip("\r\n") for ln in f.readlines()]
                old_version = raw[0] if len(raw) > 0 else ""
                target_version = raw[1] if len(raw) > 1 else ""
                nonce = raw[2] if len(raw) > 2 else ""
                installer = raw[3] if len(raw) > 3 else ""
            except OSError as _dx:
                DIAG.q("UpdateChecker.check_startup_update_message#0", _dx)

            done_nonce = done_version = ""
            try:
                dp = UpdateChecker._done_path()
                if os.path.isfile(dp):
                    with open(dp, encoding="utf-8") as f:
                        draw = [ln.rstrip("\r\n") for ln in f.readlines()]
                    done_nonce = draw[0].strip() if len(draw) > 0 else ""
                    done_version = draw[1].strip() if len(draw) > 1 else ""
            except OSError as _dx:
                DIAG.q("UpdateChecker.check_startup_update_message#1", _dx)

            cur = str(APP_VERSION).strip()
            ncur = UpdateChecker._normalize_version(cur)
            ntar = (UpdateChecker._normalize_version(target_version)
                    if target_version else "")
            nold = (UpdateChecker._normalize_version(old_version)
                    if old_version else "")
            # nonce 일치 = 인스톨러가 끝까지(ssDone) 돌았다는 뜻일 뿐,
            # 새 EXE 가 실제로 교체됐다는 보장은 아니다.
            installer_ran = bool(nonce and done_nonce and nonce == done_nonce)
            success = False

            if installer_ran and ntar and ncur == ntar:
                # 인스톨러도 끝까지 돌았고, 재시작된 앱의 버전이 목표와
                # 실제로 일치한다 -> 진짜 성공. (같은 버전 강제 재설치 포함)
                success = True
                UpdateChecker._log(
                    f"업데이트 성공: {old_version} -> {cur} "
                    f"(목표 {target_version}, 인스톨러 보고 {done_version or '?'})")
            elif installer_ran and not ntar:
                # 목표 버전 정보가 없어 버전 검증 불가 -> nonce 로만 판정(하위호환).
                success = True
                UpdateChecker._log(
                    f"업데이트 성공(nonce 일치, 목표버전 미상): "
                    f"{old_version} -> {cur}")
            elif installer_ran and ncur != ntar:
                # ★★ 핵심 수정 ★★
                # 인스톨러는 끝까지 돌았는데(nonce 일치) 재시작된 앱 버전이
                # 목표와 다르다 = 새 EXE 가 실제로는 교체되지 않았다.
                # 이걸 '성공' 이라 말하던 것이 대표님이 본 거짓 "업데이트 완료"
                # 토스트의 정체다. 절대 성공으로 처리하지 않는다.
                success = False
                UpdateChecker._log(
                    f"[업데이트 실패] 인스톨러는 완료됐으나 EXE 가 교체되지 "
                    f"않음. 직전 {old_version}, 목표 {target_version}, 현재 {cur}. "
                    f"원인 후보: (1) 파일 잠금으로 '재부팅 후 교체' 대기, "
                    f"(2) 앱 실행 폴더와 설치 폴더 불일치. "
                    f"Windows 재부팅 후 버전을 다시 확인하세요.")
                # 같은 버전으로 또 자동 시도해봤자 똑같이 밀린다. 표식을 남겨
                # 재부팅 전까지는 자동 재설치를 멈추고 재부팅 안내만 한다.
                UpdateChecker._set_reboot_pending(target_version)
            elif ntar and ncur == ntar and nold and ncur != nold:
                # done 파일을 못 읽는 환경 대비: 버전이 목표로 바뀌었으면 성공.
                success = True
                UpdateChecker._log(
                    f"업데이트 성공(버전 일치): {old_version} -> {cur}")
            else:
                UpdateChecker._log(
                    f"업데이트 실패: 직전 {old_version}, 목표 {target_version}, "
                    f"현재 {cur}, nonce(pending/done)={nonce}/{done_nonce}")

            # 성공했으면(버전이 실제로 목표가 됨) 재부팅 대기 표식 해제.
            if success:
                UpdateChecker._clear_reboot_pending()
            # pending 은 항상 정리(현재 사용자 %TEMP% 라 삭제 가능).
            UpdateChecker._safe_remove(pending)
            # ★ 업데이트가 끝났으므로(성공/실패 무관) %TEMP% 에 남은
            # OMEGA X 인스톨러 잔재를 모두 정리한다. 다음 업데이트가
            # 깨끗한 상태에서 시작되도록 보장한다. omega_update.log 와
            # 다른 프로그램 파일은 건드리지 않는다.
            UpdateChecker._cleanup_temp_installers()
            if success and installer:
                UpdateChecker._safe_remove(installer)
            return "success" if success else "failed"
        except Exception as e:
            UpdateChecker._log(f"결과 판정 예외: {e}")
            return None

    # ----- 다운로드 -----
    @staticmethod
    def download_update(url, filename=None, progress_cb=None, expected_digest=None):
        """인스톨러를 %TEMP% 에 다운로드. 성공: 경로 / 실패: None.
        expected_digest 가 주어지면(예: 'sha256:...') 다운로드한 파일의
        SHA-256 과 대조해 불일치 시 파일을 지우고 실패로 처리한다.
        GitHub 계정/자산이 탈취돼 변조된 EXE 가 올라온 경우를 막는다."""
        import tempfile
        if not UpdateChecker._is_trusted_download_url(url):
            UpdateChecker._log("신뢰할 수 없는 다운로드 URL")
            return None
        try:
            safe = os.path.basename(filename or "OMEGA_X_LITE_Setup.exe")
            if not safe.lower().endswith(".exe"):
                safe = "OMEGA_X_LITE_Setup.exe"
            dest = os.path.join(tempfile.gettempdir(), safe)
            # ★ desync 차단 ★ 받기 전에 %TEMP% 의 옛 OMEGA X 인스톨러를
            # 먼저 치운다. 같은 파일명의 옛 인스톨러가 남아 있으면 새 파일
            # 덮어쓰기가 실패할 수 있고, 그 경우 옛 버전이 실행되어 desync 가
            # 난다. dest(지금 받을 파일)는 keep 으로 지정해 보존한다.
            UpdateChecker._cleanup_temp_installers(keep=dest)
            UpdateChecker._safe_remove(dest)  # 혹시 남은 동일 경로 파일 제거
            UpdateChecker._log(f"다운로드 시작 -> {dest}")

            r = requests.get(url, stream=True, timeout=120,
                             headers={"User-Agent": GITHUB_API_HEADERS["User-Agent"]})
            if r.status_code != 200:
                UpdateChecker._log(f"다운로드 HTTP {r.status_code}")
                return None
            total = int(r.headers.get("content-length") or 0)
            done = 0
            with open(dest, "wb") as f:
                for chunk in r.iter_content(chunk_size=65536):
                    if not chunk:
                        continue
                    f.write(chunk)
                    done += len(chunk)
                    if progress_cb and total > 0:
                        progress_cb(done, total)

            if total > 0 and done != total:
                UpdateChecker._log(f"다운로드 불완전: {done}/{total}")
                UpdateChecker._safe_remove(dest)
                return None
            if done < 512 * 1024 or not UpdateChecker._validate_pe(dest):
                UpdateChecker._log(f"손상된 파일: {done} bytes")
                UpdateChecker._safe_remove(dest)
                return None
            # ── 무결성 검증: 다이제스트가 제공되면 SHA-256 을 대조한다 ──
            if expected_digest:
                if not UpdateChecker._verify_sha256(dest, expected_digest):
                    UpdateChecker._log("SHA-256 불일치 - 변조 의심, 설치 중단")
                    UpdateChecker._safe_remove(dest)
                    return None
                UpdateChecker._log("SHA-256 검증 통과")
            else:
                # ★PATCH25★ 예전에는 여기서 로그만 남기고 그대로 /SILENT
                # 관리자 권한 설치까지 갔다. 검증 못 한 35MB EXE 를 UAC 승격
                # 상태로 실행하는 것이라, 업데이트 채널이 곧 실행 경로가 된다.
                # GitHub Releases API 는 모든 자산에 sha256 다이제스트를
                # 붙여주므로(실측 확인) 여기서 막아도 정상 경로는 안 막힌다.
                UpdateChecker._log(
                    "다이제스트를 구하지 못함 - 설치 거부. "
                    "릴리스 페이지에서 직접 내려받아 설치할 것.")
                UpdateChecker._last_error = "no_digest"
                UpdateChecker._safe_remove(dest)
                return None
            UpdateChecker._log(f"다운로드 완료: {done} bytes")
            return dest
        except Exception as e:
            UpdateChecker._log(f"다운로드 예외: {e}")
            return None

    # ----- 설치 적용 (핵심) -----
    @staticmethod
    def apply_downloaded_update(new_exe, target_version=None,
                                expected_digest=None, **kwargs):
        """다운로드한 인스톨러를 무인(/SILENT)으로 실행하고 앱을 종료한다.

        인스톨러(Inno Setup)가 PrepareToInstall 에서 실행 중인 앱을
        taskkill 하고, 파일을 교체한 뒤 [Run] 으로 앱을 재시작한다.
        설치 완료 시 done 파일에 nonce 를 기록하므로, 재시작 후
        check_startup_update_message() 가 성공/실패를 정확히 판정한다.
        성공 시 반환하지 않음(os._exit). 실패 시에만 False 반환."""
        try:
            if not new_exe or not os.path.isfile(new_exe):
                UpdateChecker._log("설치 파일을 찾을 수 없음")
                return False

            # ── PATCH25_RELEASE_GATE: 실행 직전 재검증 (TOCTOU) ──
            # 다운로드 시점 검증과 ShellExecute 사이에는 최소 수 초의 틈이
            # 있고, 그 사이 파일은 %TEMP% 에 그냥 놓여 있다. 같은 사용자로
            # 도는 다른 프로세스면 얼마든지 바꿔칠 수 있다. 검증한 파일과
            # 지금 실행할 파일이 같은 파일인지 여기서 한 번 더 확인한다.
            # 35MB 해싱은 0.2초 안쪽이라 비용이 없다시피 하다.
            if not expected_digest:
                UpdateChecker._log("다이제스트 없이 설치 요청됨 - 거부")
                UpdateChecker._last_error = "no_digest"
                return False
            if not UpdateChecker._verify_sha256(new_exe, expected_digest):
                UpdateChecker._log(
                    "실행 직전 해시 불일치 - 다운로드 후 파일이 바뀌었다. 중단")
                UpdateChecker._last_error = "tampered"
                UpdateChecker._safe_remove(new_exe)
                return False

            # ── PATCH25_RELEASE_GATE: 디지털 서명 확인 ──
            signed, signer, detail = UpdateChecker._verify_authenticode(new_exe)
            UpdateChecker._log(
                f"서명 검증: {'통과' if signed else '실패'} "
                f"({detail}) 서명자=[{signer or '-'}]")
            if UpdateChecker.REQUIRE_SIGNED_INSTALLER:
                want = (UpdateChecker.EXPECTED_SIGNER_CN or "").strip()
                if not signed:
                    UpdateChecker._log("서명 필수 설정인데 서명 검증 실패 - 중단")
                    UpdateChecker._last_error = "unsigned"
                    return False
                if want and signer.strip() != want:
                    UpdateChecker._log(
                        f"서명자 불일치 (기대 [{want}]) - 중단")
                    UpdateChecker._last_error = "wrong_signer"
                    return False

            # 이전 시도의 잔여 표식 제거.
            UpdateChecker._safe_remove(UpdateChecker._pending_path())
            UpdateChecker._safe_remove(UpdateChecker._done_path())

            nonce = UpdateChecker._make_nonce()
            tgt = str(target_version or "").strip()
            try:
                with open(UpdateChecker._pending_path(), "w",
                          encoding="utf-8") as f:
                    f.write(str(APP_VERSION).strip() + "\n")
                    f.write(tgt + "\n")
                    f.write(nonce + "\n")
                    f.write(os.path.abspath(new_exe) + "\n")
            except OSError as e:
                UpdateChecker._log(f"pending 파일 기록 실패: {e}")

            # ShellExecute 는 requireAdministrator/PrivilegesRequired=admin
            # 인스톨러도 740 에러 없이 실행하며 UAC 를 정상 표시한다.
            # /SILENT 무인 설치 + /UPDATENONCE 로 결과 판정용 nonce 전달.
            import ctypes
            # ★★ /DIR — 설치 폴더를 '지금 실행 중인 EXE 의 폴더' 로 못박는다 ★★
            # 이게 없으면 인스톨러는 DefaultDirName(C:\Program Files\OMEGA X)
            # 이나 레지스트리에 기록된 옛 경로에 설치한다. 앱이 그와 다른
            # 폴더에서 돌고 있으면(포터블 실행, 옛 설치 경로 등) 새 EXE 는
            # 엉뚱한 폴더에 깔리고, 사용자가 보던 앱은 옛 버전 그대로 남는다.
            # = "업데이트 완료라는데 버전이 안 바뀜". /DIR 로 현재 EXE 폴더를
            # 직접 지정해 그 desync 를 원천 차단한다.
            try:
                app_dir = os.path.dirname(os.path.abspath(sys.executable))
            except Exception:
                app_dir = ""
            dir_arg = f' /DIR="{app_dir}"' if app_dir else ""
            params = (f"{UpdateChecker.SILENT_ARGS}{dir_arg} "
                      f"/UPDATENONCE={nonce}")
            UpdateChecker._log(
                f"무인 설치 실행: {new_exe}  "
                f"설치폴더={app_dir or '(인스톨러 기본값)'}  args=[{params}]")
            rc = ctypes.windll.shell32.ShellExecuteW(
                None, "open", os.path.abspath(new_exe), params, None, 1)
            if rc <= 32:
                UpdateChecker._log(f"인스톨러 실행 실패 (ShellExecute={rc})")
                UpdateChecker._safe_remove(UpdateChecker._pending_path())
                return False
        except Exception as e:
            UpdateChecker._log(f"업데이트 적용 예외: {e}")
            UpdateChecker._safe_remove(UpdateChecker._pending_path())
            return False

        UpdateChecker._log("인스톨러 실행됨 - 앱 종료(인스톨러가 교체/재시작 처리)")
        try:
            time.sleep(1.0)
        except Exception as _dx:
            DIAG.q("UpdateChecker.apply_downloaded_update#0", _dx)
        os._exit(0)

    # ----- 하위 호환 래퍼 -----
    @staticmethod
    def download_and_install(url, filename=None, is_setup=True,
                             progress_cb=None, target_version=None,
                             expected_digest=None):
        path = UpdateChecker.download_update(
            url, filename, progress_cb, expected_digest=expected_digest)
        if not path:
            return False
        return UpdateChecker.apply_downloaded_update(
            path, target_version=target_version,
            expected_digest=expected_digest)


# ============================================================================
# I18N — Korean / English translations
# ============================================================================
TRANSLATIONS = {
    "en": {
        # Sidebar
        "nav_home":       "Home",
        "nav_ai_core":    "Auto Boost",
        "nav_optimizer":  "PC Boost",
        "nav_storage":    "Storage",
        "nav_apps":       "Apps & Tasks",
        "nav_health":     "Health",
        "nav_reports":    "Reports",
        "nav_settings":   "Settings",
        "sidebar_active": "● Active",
        "sidebar_loading":"● Loading...",

        # Common
        "back":            "Back",
        "refresh":         "Refresh",
        "cancel":          "Cancel",
        "ok":              "OK",
        "running":         "Running...",
        "save":            "Save",
        "download":        "Download",
        "view":            "View",
        "open":            "Open",
        "manage":          "Manage",
        "loading":         "Loading...",
        "complete":        "Complete",
        "error":           "Error",
        "scanning":        "Scanning...",
        "cleaning":        "Cleaning...",
        "optimizing":      "Boosting the app you're using...",

        # Home
        "home_hero_title":     "Auto Boost",
        "home_hero_subtitle":  "Speeds things up, and shows you how much",
        "home_hero_open":      "  Open Auto Boost  ",
        "home_ram_label":      "RAM in use",
        "home_cpu_label":      "CPU usage",
        "thermal_label":       "CPU temp",
        "thermal_auto_title":  "Ease off when it gets hot",
        "thermal_auto_desc":   "Caps the CPU's maximum speed in steps while it's too hot, then puts it back. Costs some performance while it's on.",
        "thermal_threshold_lbl": "Step in above",
        "thermal_capped":      "Max CPU speed limited to {pct}%",
        "thermal_cap_none":    "No limit",
        "thermal_cap_blocked": "Can't change the power plan on this PC",
        "thermal_cap_restored": "Cooled down \u2014 speed limit removed",
        "thermal_state":       "Right now",
        "thermal_auto_c":      "auto",
        "thermal_unavailable": "Can't read the temperature on this PC",
        "thermal_warm":        "Running a bit warm",
        "thermal_source":      "Read via",
        "settings_thermal_title": "Thermal",
        "settings_thermal_desc":  "Shows the CPU temperature, and \u2014 if you turn it on below \u2014 eases the CPU's maximum speed down while it's too hot. It never touches fan speed, power limits or voltage: those are vendor-only controls and getting them wrong can't be undone in software.",
        "home_health_check":   "🩺  Health Check",
        "home_health_desc":    "Run system analysis",
        "home_active_apps":    "📦  Active Apps",
        "home_apps_desc":      "Manage running processes",
        "home_storage":        "💾  Storage",
        "home_storage_desc":   "Free up disk space",
        "home_pc_boost":       "🚀  PC Boost",
        "home_boost_desc":     "Speed up the app you're using",
        "home_ai_core_card":   "⚡  Auto Boost",
        "home_ai_core_desc":   "Keeps speeding things up while you work",
        "home_ai_status":      "🧠  AI Optimizer Status",
        "home_state":          "State",
        "home_lpi":            "Response",
        "home_cycles":         "Cycles",
        "home_actions":        "Actions",
        "home_recs":           "💡  Recommendations",
        "home_running_well":   "✓  System running optimally",
        "home_ai_monitoring":  "AI is monitoring...",

        # AI Core
        "ai_subtitle":         "One tap. Real numbers, measured.",
        # 상태 표시 — 예전엔 AI 내부 상태값(IDLE/WORK/GAME)이 그대로 화면에
        # 나갔고 "LPI" 라는 내부 지표명도 노출됐다.
        "state_idle":          "Idle",
        "state_work":          "Working",
        "state_multitask":     "Multitasking",
        "state_stutter":       "Stuttering",
        "state_game":          "Gaming",
        "state_creative":      "Creating",
        "status_header":       "● {state} · Response {lpi}",
        "status_header_run":   "● {mode} running · Response {lpi}",
        "mode_name_lite":      "Safe Boost",
        "mode_name_hard":      "Max Boost",
        "ai_lite_title":       "⚡  Safe Boost",
        "ai_lite_desc":        "Gentle speed-up — safe, and everything goes back to normal",
        "ai_lite_badge":       "BASIC",
        "ai_lite_run":         "▶  Run Safe Boost",
        "ai_hard_title":       "🔥  Max Boost",
        "ai_hard_desc":        "Full power — deeper tuning that adapts to the app you're using",
        "ai_hard_badge":       "ADVANCED",
        "ai_hard_run":         "▶  Run Max Boost",
        "ai_initial":          "Click a button above to start.",
        "ai_running":          "  Running {mode} CORE",
        "ai_complete":         "✓  {mode} Complete",
        "ai_actions_done":     "  {count} things done · every number here is measured",
        "ai_ram_freed":        "RAM Freed",
        "ai_cpu_lower":        "CPU Lower",
        "ai_ram_before":       "RAM Before",
        "ai_ram_after":        "RAM After",
        "ai_detected":         "Detected app",
        "ai_active_profile":   "Active profile",

        # Lite Core actions list (FREE — limited)
        "lite_a1":  "Gives the app you're using more CPU time",
        "lite_a2":  "Frees up memory when it starts running low",
        "lite_a3":  "Stops background apps from hogging the CPU",
        "lite_a4":  "Lowers the power background apps use",
        "lite_a5":  "✗  App detection, disk and sound priority — Max Boost only",

        # Hard Core actions list (full)
        "hard_a1":  "🎯  Works out what you're doing (gaming / working / creating)",
        "hard_a2":  "🎮  Gaming: storage and sound first, full power",
        "hard_a3":  "🎨  Creating: rendering first, smooth audio",
        "hard_a4":  "💼  Working: balanced sharing with power saving",
        "hard_a5":  "💾  Frees memory more aggressively",
        "hard_a6":  "🔋  Puts every background app into low-power mode (Win11)",
        "hard_a8":  "⏸  Pauses Windows features you don't need right now",
        "hard_a9":  "🚫  Turns off Windows' automatic game recording",

        # Optimizer
        "opt_subtitle":        "Makes the app you're using respond faster",
        "opt_profile":         "Optimization Profile",
        "opt_active":          "Active Optimizations",
        "opt_quick":           "Boost right now",
        "opt_quick_desc":      "Gives the app on screen a one-time speed boost.",
        "opt_quick_btn":       "⚡  Boost the app I'm using",
        "opt_thread_title":    "Prioritize the app I'm using",
        "opt_thread_desc":     "Briefly puts the app on screen ahead of everything else",
        "opt_io_title":        "Faster file access",
        "opt_io_desc":         "Lets the app you're using reach the drive first",
        "opt_throttle_title":  "Slow down unused apps",
        "opt_throttle_desc":   "Briefly pushes apps you're not looking at to the back",
        "opt_mmcss_title":     "Smoother sound and video",
        "opt_mmcss_desc":      "Tells Windows to keep audio and video from stuttering",
        "opt_eco_title":       "Power saving for unused apps",
        "opt_eco_desc":        "Cuts the power and CPU that background apps use (Win11 22H2+)",
        "opt_timer_title":     "Fastest response",
        "opt_timer_desc":      "⚠ Uses about 15% more battery — for gaming only",
        "opt_aff_title":       "Use the fast cores",
        "opt_aff_desc":        "Only on CPUs that mix fast and power-saving cores (Intel 12th gen+)",
        "opt_unavailable":     "Unavailable",
        "opt_na":              "N/A",
        "opt_honest_note":     "ℹ  These are short nudges to Windows, and every one of them is undone automatically. You'll feel it most in how quickly things respond. Benchmark scores barely move — usually under 2%.",

        # Storage
        "storage_subtitle":    "Free up disk space safely",
        "storage_drive":       "System Drive",
        "storage_used":        "{pct}% used",
        "storage_tools":       "Cleanup Tools",
        "storage_scan":        "🔍  Scan Junk Files",
        "storage_recycle":     "🗑  Empty Recycle Bin",
        "storage_initial":     "Click 'Scan' to see what can be cleaned.",
        "storage_files_label": "{count} files",
        "storage_recycle_bin": "Recycle Bin",
        "storage_clean_btn":   "  🧹  Clean Up ({size})  ",
        "storage_cleaned":     "✓ Cleaned {count} files ({size})",

        # Apps
        "apps_subtitle":       "Manage running processes and startup apps",
        "apps_running":        "Running Processes",
        "apps_startup":        "Startup Apps",
        "apps_col_process":    "Process",
        "apps_col_cpu":        "CPU%",
        "apps_col_ram":        "RAM%",
        "apps_col_threads":    "Threads",
        "apps_col_status":     "Status",
        "apps_col_actions":    "Actions",
        "apps_btn_boost":      "Boost",
        "apps_btn_throttle":   "Throttle",
        "apps_btn_end":        "End",
        "apps_btn_disable":    "Disable",
        "apps_critical":       "Critical",

        # Health
        "health_subtitle":     "Comprehensive system analysis",
        "health_overall":      "out of 100 — {status}",
        "health_components":   "Component Health",
        "health_issues":       "Issues Detected",
        "health_recs":         "Recommendations",
        "health_status_excellent": "Excellent",
        "health_status_good":     "Good",
        "health_status_fair":     "Fair",
        "health_status_poor":     "Poor",

        # Reports
        "reports_subtitle":    "Export reports for analysis",
        "reports_health_title":"System Health Report",
        "reports_health_desc": "HTML report with health score, top processes, recommendations",
        "reports_perf_title":  "Performance History",
        "reports_perf_desc":   "CPU, memory and response speed over time (CSV)",
        "reports_startup_title":"Startup Apps Report",
        "reports_startup_desc":"HTML list of auto-start apps with safety assessments",

        # Settings
        "settings_subtitle":   "App settings and information",
        "settings_about":      "About OMEGA X",
        "settings_ai_brag":    "🧠  Small but smart: everything is worked out on your own PC in under a millisecond. Nothing is sent to a server, and we don't collect how you use it. (The app only reaches the internet to check for updates.)",
        "settings_log_label":  "Error log",
        "settings_version":    "Version",
        "settings_windows":    "Windows",
        "settings_mode":       "Mode",
        "settings_hybrid":     "Fast + power-saving cores",
        "settings_logical":    "CPU threads",
        "settings_ui_frame":   "UI frame time",
        "settings_physical":   "CPU cores",
        "settings_admin":      "Admin",
        "settings_yes":        "Yes",
        "settings_no":         "No",
        "settings_language":   "Language / 언어",
        "settings_lang_kr":    "한국어",
        "settings_lang_en":    "English",
        "settings_check_update": "Check for updates",
        "settings_auto":       "Auto Optimizer",
        "update_title":        "OMEGA X Update",
        "update_new_version":  "A new version is available",
        "update_version_line": "Current: v{current}  →  Latest: v{latest}",
        "update_notes_label":  "Release notes",
        "update_notes_empty":  "No release notes",
        "update_now":          "Update now",
        "update_later":        "Later",
        "update_downloading":  "Downloading...",
        "update_retry":        "Retry",
        "update_failed":       "Update failed. Check your connection and try again.",
        "update_setup_hint":   "This release uses the installer. Setup will run after download.",
        "update_checking":     "Checking for updates...",
        "update_none":         "You are on the latest version.",
        "update_reboot_pending":"Update is ready. Please restart your PC to finish it.",
        "update_check_failed": "Could not check for updates.",
        "update_applying":     "Installing update...",
        "update_restarting":   "Restarting OMEGA X in a moment...",
        "update_success_toast":"Update complete. You are on the latest version.",
        "update_log_hint":     "Details: %TEMP%\\omega_update.log",
        "settings_auto_loop":  "Auto-Optimization Loop",
        "settings_auto_desc":  "Keeps tuning your PC in the background",
        "settings_auto_what":  "What it does, automatically:",
        "auto_what_1":  "🧠  Detects what you're doing (gaming, work, browsing, idle)",
        "auto_what_2":  "⚡  Briefly gives the app you're using more CPU (every few seconds)",
        "auto_what_3":  "🔋  Holds back background apps that eat CPU (put back automatically)",
        "auto_what_4":  "💾  Trims sleeping app memory when RAM is full",
        "auto_what_5":  "🎵  Asks Windows to favor games and audio when they're in front",
        "auto_what_6":  "📊  Measures how fast your PC responds, every 6 seconds",
        "auto_what_safe":"Every action is brief (0.15–1.5 seconds) and undoes itself. Windows' own system programs are protected and never touched.",
        "settings_safety":     "Safety",
        # Smart Automation (new)
        "auto_section":        "Smart Automation",
        "auto_section_desc":   "Set-and-forget features that work in the background.",
        "auto_game_title":     "🎮  Game Auto-Boost",
        "auto_game_desc":      "When you start a game, Max Boost turns on by itself. It stops when you close the game.",
        "auto_battery_title":  "🔋  Battery Saver Mode",
        "auto_battery_desc":   "Cuts the power unused apps draw when the laptop runs on battery.",
        "auto_sched_title":    "⏰  Scheduled Cleanup",
        "auto_sched_desc":     "Run optimizations at preset times (e.g., 3 AM daily cleanup).",
        "auto_sched_add":      "Add Schedule",
        "auto_sched_none":     "No schedules set. Add one to start.",
        "auto_sched_at":       "Daily at {time}",
        "auto_sched_task_cleanup": "Temp file cleanup",
        "auto_sched_task_trim":    "Free up memory",
        "auto_sched_task_hard":    "5 minutes of Max Boost",
        "auto_sched_remove":   "Remove",
        "auto_last_action":    "Last action",
        "auto_last_none":      "Not run yet",
        "settings_rollback_desc": "Roll back all active modifications.",
        "settings_rollback":   "↩  Rollback All Changes",
        "settings_disclosure": "ℹ  About what this app can and can't do:\n\nOMEGA X makes your PC feel quicker — less input lag, smoother windows, steadier frames — by changing how Windows shares the CPU with the app you're using.\n\nEvery number shown (memory freed, CPU change) is measured before and after, on your machine.\n\nBenchmark scores are a different matter: tools like this barely move them, usually under 2%. Any app claiming a 25% benchmark gain is not telling you the truth. We'd rather be honest.",

        # Toasts
        "toast_optimized":     "✓ Boosted the app you're using",
        "toast_profile":       "Profile: {prof}",
        "toast_rolled_back":   "✓ Rolled back {n} changes",
        "toast_lang_changed":  "✓ Language changed",
        "toast_health_saved":  "✓ Health report saved to Desktop",
        "toast_perf_saved":    "✓ Performance CSV saved",
        "toast_startup_saved": "✓ Startup report saved",
        "toast_disabled":      "✓ Disabled: {name}",
        "toast_failed":        "× Failed: {name}",
        "toast_profile_switched":"⚡ {app} detected → {profile} mode applied",

        # RAM Leak Detector
        "leak_card_title":     "🔍  Memory Leak Monitor",
        "leak_subtitle":       "Finds apps whose memory keeps growing and never comes back.",
        "leak_no_alerts":      "✓ No leaks detected — {n} processes monitored.",
        "leak_severity_warn":  "Watch",
        "leak_severity_danger":"Warning",
        "leak_severity_critical":"Critical",
        "leak_growth":         "+{mb} MB / last {min} min",
        "leak_action_restart": "Restart recommended",
        "leak_disabled":       "Leak detector disabled.",

        # Session History
        "history_title":       "📅  Session History",
        "history_summary":     "Last 30 days summary",
        "history_total_ram":   "Total RAM freed",
        "history_total_cycles":"Total cycles",
        "history_avg_pis":     "Avg AI score",
        "history_sessions":    "Sessions",
        "history_recent":      "Recent sessions",
        "history_none":        "No history yet. Start Safe or Max Boost and it'll show up here.",
        "history_export":      "📥  Export CSV",
        "history_session_row": "{date} {start}~{end} · {mode} · {cycles} cycles · {ram}MB freed · AI {pis}",
        "toast_history_csv":   "✓ Session history CSV saved to Desktop",

        # Welcome dialog (first run only)
        "welcome_title":       "Welcome to OMEGA X",
        "welcome_subtitle":    "Makes Windows respond faster — and shows you the numbers",
        "welcome_step1_title": "1.  Pick a mode",
        "welcome_step1_desc":  "Open Auto Boost and pick Safe or Max. Both keep running and adjust to whatever you're doing.",
        "welcome_step2_title": "2.  Watch real metrics",
        "welcome_step2_desc":  "The score, the memory freed, the mode in use — all of it is measured on your PC. No made-up numbers.",
        "welcome_step3_title": "3.  Set and forget",
        "welcome_step3_desc":  "In Settings → Smart automation you can turn on auto-boost for games, battery saving, and scheduled cleanups.",
        "welcome_get_started": "Get Started",
        "welcome_dont_show":   "Don't show again",

        # Quit confirmation (when Core is running)
        "quit_title":          "Quit OMEGA X?",
        "quit_running":        "{mode} is currently running. Stop and quit?",
        "quit_yes":            "Stop & Quit",
        "quit_no":             "Cancel",

        # Running progress (cumulative stats + log)
        "running_ram_freed":   "Memory recovered",
        "running_procs_handled":"Processes optimized",
        "running_files_cleaned":"Files cleaned",
        "running_steps_done":  "Steps completed",
        "running_action_log":  "What's happening now:",

        # Continuous mode (toggle on/off)
        "ai_lite_run_start":   "▶  Start Safe Boost",
        "ai_lite_run_stop":    "■  Stop Safe Boost",
        "ai_hard_run_start":   "▶  Start Max Boost",
        "ai_hard_run_stop":    "■  Stop Max Boost",
        "ai_status_idle":      "Click a button above to start continuous optimization.",
        "ai_status_running":   "● {mode} running — cycle {n}",
        "ai_improve_title":    "AI Performance Score",
        "ai_improve_ram":      "Free memory",
        "ai_improve_cpu":      "OMEGA X itself",
        "ai_improve_freed":    "Memory reclaimed",
        "ai_improve_cycles":   "Cycles run",
        "unit_cores":          "cores",
        "learn_title":         "What it learned on this PC",
        "learn_desc":          "Each action is skipped at random now and then, so its effect can be compared against not doing it. Actions that don't help are dropped.",
        "learn_helps":         "helps",
        "learn_neutral":       "no difference \u2014 stopped",
        "learn_hurts":         "made it worse \u2014 stopped",
        "learn_learning":      "still measuring",
        "learn_samples":       "{on} on / {off} off",
        "learn_none":          "Nothing measured yet \u2014 run Lite or Hard Core for a while",
        "learn_reset":         "Forget what was learned",
        "learn_policy_note":   "What is learned only changes whether these actions run \u2014 nothing else. Helps = keep running it. No difference / made it worse = stop running it, and retest it later.",
        "learn_pol_keep":      "keeps running",
        "learn_pol_stop":      "stopped running",
        "learn_pol_test":      "trying both ways",
        "learn_now_on":        "on now",
        "learn_now_off":       "held now",
        "ui_copy_diag":        "Copy diagnostics",
        "ui_diag_copied":      "Diagnostics copied to clipboard",
        "act_title":           "What it actually did",
        "act_desc":            "Every action taken, and every action skipped with the reason why. It includes the names of programs that were running. Kept on this PC only, in activity.log \u2014 'Clear log' deletes the file.",
        "act_none":            "Nothing recorded yet \u2014 start Lite or Hard Core.",
        "act_copy":            "Copy log",
        "act_open":            "Open log folder",
        "act_clear":           "Clear log",
        "act_copied":          "Log copied to clipboard",
        "act_cleared":         "Log cleared",
        "act_lines":           "{n} lines \u00b7 newest last",
        "act_r_learn_hold":    "held back to measure",
        "act_r_not_due":       "not due this cycle",
        "act_r_ram_ok":        "memory was fine",
        "act_r_os_unsupported":"not supported on this Windows",
        "act_r_no_hybrid_cpu": "no P/E core CPU",
        "act_skipped_head":    "skipped:",
        "predict_title":       "What you'll probably open next",
        "predict_line":        "{app} \u2014 {pct}% ({n} switches learned)",
        "predict_none":        "Not enough yet \u2014 it learns as you switch apps",
        "predict_prewarm":     "Getting ready for {app} ({pct}% likely next)",
        "predict_toggle":      "Learn which apps I use",
        "predict_privacy":     "Only the program name and the time are kept, on this PC. Turning this off deletes the file.",
        "effect_idle":         "Not started yet",
        "effect_collecting":   "Measuring \u2014 {n} of {need} apps, {c} in the comparison group",
        "effect_none":         "No measurable difference from the comparison group",
        "effect_control_blocked": "Comparison group unavailable \u2014 {u} apps could not be released from energy-save mode, so there is nothing clean to compare against",
        "effect_unmeasurable": "Can't tell from CPU here \u2014 the apps we slowed were already using almost none ({h} cores; we'd need {f} to see a change)",
        "effect_scope_note":   "This measures one thing only: background CPU freed by the energy-save step. It says nothing about the foreground boost, scheduler hints, GPU queue, disk priority or power plan.",
        "effect_better":       "Removed {d} cores of load ({nt} apps vs {nc} left alone)",
        "effect_worse":        "Load went up by {d} cores ({nt} apps vs {nc} left alone)",
        "ai_baseline_note":    "The score combines 8 things we measure: memory, how long tasks wait for the CPU, load from unused apps, drive activity, memory shortage, how quickly the PC responds, whether the right mode was picked, and how much was actually done. RAM and CPU figures are averages for this session.",
        "pis_score_label":     "Apps eased off",
        "pis_score_avg":       "Background load",
        "pis_factor_dominant": "Load we removed",
        "pis_tier_excellent":  "Excellent — clearly faster than with it off",
        "pis_tier_good":       "Good — noticeably faster",
        "pis_tier_stable":     "No change — there's nothing to speed up right now",
        "pis_tier_minor":      "Slightly worse — a little slower than with it off",
        "pis_tier_idle":       "Worse — it was better with this turned off",
        "pis_tier_nodata":     "Measuring — give it a moment",
        "pis_comp_memory":     "Memory",
        "pis_comp_cpu":        "CPU",
        "pis_comp_bg_cpu":     "Unused app load",
        "pis_comp_responsive": "Responsiveness",
        "pis_comp_disk":       "Disk activity",
        "pis_comp_thrashing":  "Memory shortage",
        "pis_comp_smart_match":"Right mode picked",
        "pis_comp_work_done":  "Work done",

        # Friendly action labels (replaces technical terms)
        "friendly_memory_cleanup":   "Recovering memory",
        "friendly_energy_saving":    "Energy-saving for background apps",
        "friendly_cpu_balance":      "Lowering background CPU usage",
        "friendly_app_boost":        "Speeding up the active app",
        "friendly_disk_priority":    "Letting the app reach the drive first",
        "friendly_pause_services":   "Pausing Windows background tasks",
        "friendly_disable_recording":"Turning off background game recording",
        "friendly_clean_temp":       "Removing temporary files",
        "friendly_audio_priority":   "Boosting audio/video priority",
        "friendly_cpu_smart":        "Assigning CPU cores smartly",
        "friendly_power_mode":       "Switching to performance mode",
        "friendly_disk_cache":       "Clearing drive leftovers",
        "friendly_dns_flush":        "Refreshing network shortcuts",
        "friendly_memory_compact":   "Tidying up unused memory",
        "friendly_light_memory":     "Light memory cleanup",
        "friendly_bg_mem_priority":  "Moving unused apps' memory back",
        "friendly_pe_core_hint":     "Splitting fast and power-saving cores",
        "friendly_timer_guard":      "Blocking interruptions from unused apps",
        "friendly_gpu_priority":     "Graphics work first",
        "friendly_browser_tuning":   "Balancing browser resource usage",
        "profile_game":              "Gaming",
        "profile_creative":          "Creative",
        "profile_dev":               "Working",
        "profile_browser":           "Multitask",
        "profile_office":            "Working",
        "profile_general":           "Auto",
        "ui_refresh":                "↻  Refresh",
        "ui_copy_sysinfo":           "📋  Copy System Info",
        "toast_sysinfo_copied":      "System info copied to clipboard",
        "card_license_credits":      "🛡️  License & Credits",
        "status_optimal":            "✓  System running optimally",
        "splash_init":               "Getting ready...",
        "splash_wait":               "This may take a few seconds...",
        "init_failed":               "❌ Failed to initialize.",

        # Impact summaries (right side of each row)
        "impact_ram_freed":      "{mb} MB freed",
        "impact_procs_handled":  "{count} processes",
        "impact_files":          "{count} files",
        "impact_disabled":       "Disabled",
        "impact_applied":        "Applied",
        "impact_skipped":        "Skipped",

        # ── 언어 전환 누락분 보강 ──────────────────────────────
        "admin_dlg_title":       "Administrator rights required",
        "admin_dlg_msg":         ("{mode} mode requires administrator rights.\n\n"
                                  "Restart as administrator?\n"
                                  "Choosing Yes opens the UAC prompt; once you "
                                  "approve it, {mode} mode starts automatically."),
        "admin_dlg_restart":     "Restart as administrator",
        "admin_toast_skip":      "Continuing without admin rights. Some features are limited.",
        "cancel":                "Cancel",
        "storage_found":         "Found {size} in {count} files",
        "storage_recycle_bin":   "Recycle Bin",
        "generic_error":         "Error: {msg}",
        "consent_title":         "Terms of Use",
        "consent_agree":         "Agree & Continue",
        "consent_decline":       "Decline (Exit)",
        "license_title":         "License",
        "license_body":          ("{copyright}\n\n"
                                  "OMEGA X is free software: you can redistribute it "
                                  "and/or modify it under the terms of the GNU General "
                                  "Public License as published by the Free Software "
                                  "Foundation, either version 3 of the License, or (at "
                                  "your option) any later version. There is no "
                                  "restriction on the field of use, commercial use "
                                  "included.\n\n"
                                  "This program is distributed WITHOUT ANY WARRANTY, "
                                  "without even the implied warranty of MERCHANTABILITY "
                                  "or FITNESS FOR A PARTICULAR PURPOSE. See the GNU "
                                  "General Public License for more details.\n\n"
                                  "The complete corresponding source code is available "
                                  "at the link below."),
        "license_meta":          ("Version v{version} · Python 3.14 + CustomTkinter + "
                                  "psutil\n"
                                  "Every optimization is reversible. System processes "
                                  "are protected and never terminated."),
        "license_view":          "View full licence",
        "license_source":        "Source code",

        # ── 확인 다이얼로그 / 파괴적 액션 ──────────────────────
        "ui_confirm":            "Confirm",
        "confirm_kill_title":    "End this process?",
        "confirm_kill_msg":      ("{name} (PID {pid}) will be terminated immediately.\n\n"
                                  "Any unsaved work in that program is lost. This cannot be undone."),
        "confirm_startup_title": "Disable this startup item?",
        "confirm_startup_msg":   ("{name} will be removed from Windows startup.\n\n"
                                  "A backup is kept, so you can restore it from the list below at any time."),
        "confirm_clean_title":   "Delete temporary files?",
        "confirm_clean_msg":     ("Files older than 24 hours in the scanned folders will be deleted permanently — they do NOT go to the Recycle Bin.\n\n"
                                  "Close your browser first: deleting its cache while it is running can corrupt it."),
        "confirm_recycle_title": "Empty the Recycle Bin?",
        "confirm_recycle_msg":   "{count} items ({size}) will be deleted permanently. This cannot be undone, and OMEGA X cannot bring them back.",
        "recycle_already_empty": "The Recycle Bin is already empty.",

        # ── 프로세스 표 ────────────────────────────────────────
        "apps_col_pid":          "PID",
        "apps_search_ph":        "Search by name",
        "apps_no_match":         "No process matches that search.",

        # ── 시작프로그램 ──────────────────────────────────────
        "startup_none":          "No startup items found.",
        "startup_disabled_card": "Disabled by OMEGA X",
        "startup_restore":       "Restore",
        "startup_none_disabled": "Nothing disabled yet. Items you disable can be restored here.",
        "toast_restored":        "Restored: {name}",
        "toast_restore_failed":  "Could not restore {name}",

        # ── 테마 ──────────────────────────────────────────────
        "settings_theme":        "Theme",
        "theme_light":           "Light",
        "theme_dark":            "Dark",
        "theme_system":          "Match Windows",

        # ── 정리 결과 (영문 하드코딩이던 것) ────────────────────
        "toast_cleaned":         "Cleaned {count} files ({size})",
        "toast_scan_error":      "Scan failed: {msg}",
        "toast_clean_error":     "Cleanup failed: {msg}",
    },

    "ko": {
        # Sidebar
        "nav_home":       "홈",
        "nav_ai_core":    "자동 부스트",
        "nav_optimizer":  "PC 부스트",
        "nav_storage":    "저장소",
        "nav_apps":       "앱 및 작업",
        "nav_health":     "시스템 상태",
        "nav_reports":    "보고서",
        "nav_settings":   "설정",
        "sidebar_active": "● 활성",
        "sidebar_loading":"● 로드 중...",

        # Common
        "back":            "뒤로",
        "refresh":         "새로고침",
        "cancel":          "취소",
        "ok":              "확인",
        "running":         "실행 중...",
        "save":            "저장",
        "download":        "다운로드",
        "view":            "보기",
        "open":            "열기",
        "manage":          "관리",
        "loading":         "로딩 중...",
        "complete":        "완료",
        "error":           "오류",
        "scanning":        "스캔 중...",
        "cleaning":        "정리 중...",
        "optimizing":      "지금 쓰는 앱 부스트 중...",

        # Home
        "home_hero_title":     "자동 부스트",
        "home_hero_subtitle":  "빠르게 만들고, 얼마나 빨라졌는지 보여줍니다",
        "home_hero_open":      "  자동 부스트 열기  ",
        "home_ram_label":      "RAM 사용량",
        "home_cpu_label":      "CPU 사용량",
        "thermal_label":       "CPU 온도",
        "thermal_auto_title":  "뜨거우면 스스로 속도 낮추기",
        "thermal_auto_desc":   "온도가 높은 동안 CPU 최대 속도를 단계적으로 낮췄다가 식으면 되돌립니다. 켜져 있는 동안은 성능이 조금 줄어요.",
        "thermal_threshold_lbl": "개입 기준 온도",
        "thermal_capped":      "CPU 최대 속도를 {pct}% 로 제한 중",
        "thermal_cap_none":    "제한 없음",
        "thermal_cap_blocked": "이 PC에서는 전원 설정을 바꿀 수 없어요",
        "thermal_cap_restored": "온도가 내려가 제한을 풀었어요",
        "thermal_state":       "지금 상태",
        "thermal_auto_c":      "자동",
        "thermal_unavailable": "이 PC에서는 온도를 확인할 수 없어요",
        "thermal_warm":        "온도가 조금 높아요",
        "thermal_source":      "측정 경로",
        "settings_thermal_title": "열 관리",
        "settings_thermal_desc":  "CPU 온도를 보여주고, 아래에서 켜면 뜨거운 동안 CPU 최대 속도를 낮췄다가 되돌립니다. 팬 속도\u00b7전력 한계\u00b7전압은 건드리지 않아요 \u2014 제조사 전용 영역이라 잘못 건드리면 소프트웨어로 되돌릴 수 없습니다.",
        "home_health_check":   "🩺  상태 검사",
        "home_health_desc":    "시스템 분석 실행",
        "home_active_apps":    "📦  활성 앱",
        "home_apps_desc":      "실행 중인 프로세스 관리",
        "home_storage":        "💾  저장소",
        "home_storage_desc":   "디스크 공간 확보",
        "home_pc_boost":       "🚀  PC 부스트",
        "home_boost_desc":     "지금 쓰는 앱 빠르게",
        "home_ai_core_card":   "⚡  자동 부스트",
        "home_ai_core_desc":   "쓰는 동안 계속 알아서 빠르게",
        "home_ai_status":      "🧠  AI 옵티마이저 상태",
        "home_state":          "상태",
        "home_lpi":            "반응 속도",
        "home_cycles":         "사이클",
        "home_actions":        "액션",
        "home_recs":           "💡  추천",
        "home_running_well":   "✓  시스템이 최적 상태로 작동 중",
        "home_ai_monitoring":  "AI가 모니터링 중...",

        # AI Core
        "ai_subtitle":         "버튼 하나. 실제로 측정한 숫자.",
        "state_idle":          "대기 중",
        "state_work":          "작업 중",
        "state_multitask":     "여러 작업 중",
        "state_stutter":       "버벅임 감지",
        "state_game":          "게임 중",
        "state_creative":      "창작 작업 중",
        "status_header":       "● {state} · 반응 {lpi}",
        "status_header_run":   "● {mode} 실행 중 · 반응 {lpi}",
        "mode_name_lite":      "안전 부스트",
        "mode_name_hard":      "최대 부스트",
        "ai_lite_title":       "⚡  안전 부스트",
        "ai_lite_desc":        "가볍게 빠르게 — 안전하고, 끄면 원래대로 돌아갑니다",
        "ai_lite_badge":       "기본",
        "ai_lite_run":         "▶  안전 부스트 실행",
        "ai_hard_title":       "🔥  최대 부스트",
        "ai_hard_desc":        "최대한 빠르게 — 쓰는 앱에 맞춰 더 깊이 조정합니다",
        "ai_hard_badge":       "고급",
        "ai_hard_run":         "▶  최대 부스트 실행",
        "ai_initial":          "위 버튼을 클릭하여 시작하세요.",
        "ai_running":          "  {mode} CORE 실행 중",
        "ai_complete":         "✓  {mode} 완료",
        "ai_actions_done":     "  {count}가지 작업 완료 · 모든 수치는 실제 측정값",
        "ai_ram_freed":        "RAM 회수",
        "ai_cpu_lower":        "CPU 감소",
        "ai_ram_before":       "이전 RAM",
        "ai_ram_after":        "이후 RAM",
        "ai_detected":         "감지된 앱",
        "ai_active_profile":   "적용 중인 프로필",

        # Lite Core actions list (FREE — 제한)
        "lite_a1":  "지금 쓰는 앱에 CPU를 더 많이 줍니다",
        "lite_a2":  "메모리가 부족해지면 가볍게 정리합니다",
        "lite_a3":  "안 쓰는 앱이 CPU를 덜 쓰게 합니다",
        "lite_a4":  "안 쓰는 앱의 전력 사용을 줄입니다",
        "lite_a5":  "✗  앱 자동 인식, 저장장치·소리 우선 처리는 최대 부스트에만 있습니다",

        # Hard Core actions list (풀)
        "hard_a1":  "🎯  지금 게임 중인지 작업 중인지 자동으로 알아냅니다",
        "hard_a2":  "🎮  게임할 때: 저장장치·소리를 먼저 처리하고 최대 전력으로",
        "hard_a3":  "🎨  영상·그림 작업할 때: 렌더링 우선, 소리 끊김 방지",
        "hard_a4":  "💼  문서·업무할 때: 균형 있게 나누고 전력도 아낌",
        "hard_a5":  "💾  메모리를 더 적극적으로 확보합니다",
        "hard_a6":  "🔋  안 쓰는 앱을 전부 절전 상태로 (Windows 11)",
        "hard_a8":  "⏸  당장 필요 없는 Windows 기능을 잠시 멈춥니다",
        "hard_a9":  "🚫  Windows가 몰래 하는 게임 녹화를 끕니다",

        # Optimizer
        "opt_subtitle":        "지금 쓰는 앱을 더 빠르게",
        "opt_profile":         "최적화 프로필",
        "opt_active":          "활성 최적화",
        "opt_quick":           "지금 바로 부스트",
        "opt_quick_desc":      "지금 화면에 떠 있는 앱에 한 번만 성능을 몰아줍니다.",
        "opt_quick_btn":       "⚡  지금 쓰는 앱 부스트",
        "opt_thread_title":    "지금 쓰는 앱 먼저 처리",
        "opt_thread_desc":     "화면에 떠 있는 앱을 아주 짧게 맨 앞으로 보냅니다",
        "opt_io_title":        "저장장치 먼저 쓰게 하기",
        "opt_io_desc":         "지금 쓰는 앱이 저장장치를 먼저 쓰게 합니다",
        "opt_throttle_title":  "안 쓰는 앱 잠시 늦추기",
        "opt_throttle_desc":   "화면에 없는 앱을 잠깐 뒤로 미룹니다",
        "opt_mmcss_title":     "소리·영상 끊김 방지",
        "opt_mmcss_desc":      "음악·영상·게임 소리가 끊기지 않게 Windows에 알립니다",
        "opt_eco_title":       "안 쓰는 앱 절전",
        "opt_eco_desc":        "안 쓰는 앱의 전력·CPU 사용을 줄입니다 (Windows 11 22H2 이상)",
        "opt_timer_title":     "반응 속도 최우선",
        "opt_timer_desc":      "⚠ 배터리를 약 15% 더 씁니다 — 게임할 때만 권장",
        "opt_aff_title":       "빠른 코어에 몰아주기",
        "opt_aff_desc":        "빠른 코어와 절전 코어가 섞인 CPU에서만 작동합니다 (인텔 12세대 이상)",
        "opt_unavailable":     "사용 불가",
        "opt_na":              "해당 없음",
        "opt_honest_note":     "ℹ  Windows에 아주 짧게 신호를 보내는 방식이고, 모든 변경은 자동으로 원래대로 돌아갑니다. 체감되는 건 '반응이 빨라진다'는 쪽이며, 벤치마크 점수는 거의 변하지 않습니다 — 보통 2% 미만입니다.",

        # Storage
        "storage_subtitle":    "안전하게 디스크 공간 확보",
        "storage_drive":       "시스템 드라이브",
        "storage_used":        "{pct}% 사용 중",
        "storage_tools":       "정리 도구",
        "storage_scan":        "🔍  정크 파일 스캔",
        "storage_recycle":     "🗑  휴지통 비우기",
        "storage_initial":     "정리 가능한 항목을 보려면 '스캔'을 클릭하세요.",
        "storage_files_label": "{count}개 파일",
        "storage_recycle_bin": "휴지통",
        "storage_clean_btn":   "  🧹  정리하기 ({size})  ",
        "storage_cleaned":     "✓ {count}개 파일 정리됨 ({size})",

        # Apps
        "apps_subtitle":       "실행 중 프로세스 및 시작 프로그램 관리",
        "apps_running":        "실행 중 프로세스",
        "apps_startup":        "시작 프로그램",
        "apps_col_process":    "프로세스",
        "apps_col_cpu":        "CPU%",
        "apps_col_ram":        "RAM%",
        "apps_col_threads":    "스레드",
        "apps_col_status":     "상태",
        "apps_col_actions":    "액션",
        "apps_btn_boost":      "부스트",
        "apps_btn_throttle":   "억제",
        "apps_btn_end":        "종료",
        "apps_btn_disable":    "비활성화",
        "apps_critical":       "필수",

        # Health
        "health_subtitle":     "종합 시스템 분석",
        "health_overall":      "/ 100 — {status}",
        "health_components":   "구성 요소 상태",
        "health_issues":       "감지된 문제",
        "health_recs":         "추천",
        "health_status_excellent": "최상",
        "health_status_good":     "양호",
        "health_status_fair":     "보통",
        "health_status_poor":     "주의",

        # Reports
        "reports_subtitle":    "분석용 보고서 내보내기",
        "reports_health_title":"시스템 상태 보고서",
        "reports_health_desc": "건강 점수, Top 프로세스, 추천이 포함된 HTML 보고서",
        "reports_perf_title":  "성능 이력",
        "reports_perf_desc":   "시간대별 CPU·메모리·반응 속도 기록 (CSV)",
        "reports_startup_title":"시작 프로그램 보고서",
        "reports_startup_desc":"안전성 평가가 포함된 자동 시작 앱 HTML 목록",

        # Settings
        "settings_subtitle":   "앱 설정 및 정보",
        "settings_about":      "OMEGA X 정보",
        "settings_ai_brag":    "🧠  작지만 똑똑합니다: 모든 판단을 이 PC 안에서 1000분의 1초 안에 끝냅니다. 서버로 보내는 것도, 사용 기록을 모으는 것도 없습니다. (인터넷은 업데이트 확인할 때만 씁니다.)",
        "settings_log_label":  "오류 로그",
        "settings_version":    "버전",
        "settings_windows":    "Windows",
        "settings_mode":       "모드",
        "settings_hybrid":     "빠른 코어 + 절전 코어",
        "settings_logical":    "CPU 스레드",
        "settings_ui_frame":   "화면 갱신 시간",
        "settings_physical":   "CPU 코어",
        "settings_admin":      "관리자 권한",
        "settings_yes":        "예",
        "settings_no":         "아니오",
        "settings_language":   "Language / 언어",
        "settings_lang_kr":    "한국어",
        "settings_lang_en":    "English",
        "settings_check_update": "업데이트 확인",
        "settings_auto":       "자동 옵티마이저",
        "update_title":        "OMEGA X 업데이트",
        "update_new_version":  "새 버전이 출시되었습니다",
        "update_version_line": "현재: v{current}  →  최신: v{latest}",
        "update_notes_label":  "업데이트 내용",
        "update_notes_empty":  "릴리스 노트 없음",
        "update_now":          "지금 업데이트",
        "update_later":        "나중에",
        "update_downloading":  "다운로드 중...",
        "update_retry":        "다시 시도",
        "update_failed":       "업데이트에 실패했습니다. 네트워크를 확인한 뒤 다시 시도하세요.",
        "update_setup_hint":   "설치 프로그램 버전입니다. 다운로드 후 Setup이 실행됩니다.",
        "update_checking":     "업데이트 확인 중...",
        "update_none":         "최신 버전을 사용 중입니다.",
        "update_reboot_pending":"업데이트가 준비됐습니다. PC를 재부팅하면 적용됩니다.",
        "update_check_failed": "업데이트를 확인할 수 없습니다.",
        "update_applying":     "업데이트 설치 중...",
        "update_restarting":   "잠시 후 OMEGA X가 자동으로 다시 실행됩니다.",
        "update_success_toast":"업데이트가 완료되었습니다.",
        "update_log_hint":     "자세한 내용: %TEMP%\\omega_update.log",
        "settings_auto_loop":  "자동 최적화 루프",
        "settings_auto_desc":  "백그라운드에서 계속 알아서 조정합니다",
        "settings_auto_what":  "자동으로 수행하는 작업:",
        "auto_what_1":  "🧠  지금 무엇을 하는지 감지 (게임, 작업, 브라우징, 유휴)",
        "auto_what_2":  "⚡  지금 쓰는 앱에 CPU를 짧게 더 줍니다 (몇 초마다)",
        "auto_what_3":  "🔋  CPU를 많이 쓰는 안 쓰는 앱을 억제합니다 (자동으로 원상복구)",
        "auto_what_4":  "💾  RAM 부족 시 잠자는 앱 메모리 정리",
        "auto_what_5":  "🎵  게임·음악이 앞에 있으면 Windows에 먼저 처리하라고 알립니다",
        "auto_what_6":  "📊  PC 반응 속도를 6초마다 측정합니다",
        "auto_what_safe":"모든 작업은 0.15~1.5초로 짧고 스스로 원래대로 돌아갑니다. Windows 자체 시스템 프로그램은 보호되며 절대 건드리지 않습니다.",
        "settings_safety":     "안전",
        # Smart Automation (new)
        "auto_section":        "스마트 자동화",
        "auto_section_desc":   "백그라운드에서 알아서 작동하는 기능들입니다.",
        "auto_game_title":     "🎮  게임 자동 부스트",
        "auto_game_desc":      "게임을 시작하면 최대 부스트가 알아서 켜집니다. 게임을 끄면 자동으로 멈춥니다.",
        "auto_battery_title":  "🔋  배터리 절약 모드",
        "auto_battery_desc":   "노트북이 배터리로 돌아갈 때 안 쓰는 앱의 전력 사용을 자동으로 줄입니다.",
        "auto_sched_title":    "⏰  예약 정리",
        "auto_sched_desc":     "지정한 시간에 자동 최적화 실행 (예: 매일 새벽 3시 청소).",
        "auto_sched_add":      "예약 추가",
        "auto_sched_none":     "예약 없음. 하나 추가해서 시작하세요.",
        "auto_sched_at":       "매일 {time}",
        "auto_sched_task_cleanup": "임시 파일 정리",
        "auto_sched_task_trim":    "메모리 정리",
        "auto_sched_task_hard":    "5분간 최대 부스트",
        "auto_sched_remove":   "제거",
        "auto_last_action":    "최근 작업",
        "auto_last_none":      "아직 실행 안 됨",
        "settings_rollback_desc": "활성화된 모든 변경사항을 되돌립니다.",
        "settings_rollback":   "↩  모든 변경사항 되돌리기",
        "settings_disclosure": "ℹ  이 앱이 할 수 있는 것과 없는 것:\n\nOMEGA X는 Windows가 CPU를 나눠 주는 방식을 조정해서 PC가 더 빠르게 '반응'하게 만듭니다 — 입력이 덜 밀리고, 창이 부드럽게 움직이고, 프레임이 고르게 나옵니다.\n\n화면에 보이는 모든 숫자(회수한 메모리, CPU 변화)는 이 PC에서 전·후를 직접 측정한 값입니다.\n\n다만 벤치마크 점수는 다릅니다. 이런 종류의 도구로는 거의 안 움직이고, 보통 2% 미만입니다. 벤치마크가 25% 올라간다고 하는 앱은 사실이 아닙니다. 저희는 정직한 쪽을 택했습니다.",

        # Toasts
        "toast_optimized":     "✓ 지금 쓰는 앱 부스트 완료",
        "toast_profile":       "프로필: {prof}",
        "toast_rolled_back":   "✓ {n}개 변경사항 되돌림",
        "toast_lang_changed":  "✓ 언어 변경 완료",
        "toast_health_saved":  "✓ 상태 보고서가 바탕화면에 저장됨",
        "toast_perf_saved":    "✓ 성능 CSV 저장 완료",
        "toast_startup_saved": "✓ 시작 프로그램 보고서 저장 완료",
        "toast_disabled":      "✓ 비활성화됨: {name}",
        "toast_failed":        "× 실패: {name}",
        "toast_profile_switched":"⚡ {app} 감지 → {profile} 모드 적용",

        # RAM Leak Detector
        "leak_card_title":     "🔍  메모리 누수 감지",
        "leak_subtitle":       "메모리를 계속 붙잡고 놓지 않는 앱을 찾아냅니다.",
        "leak_no_alerts":      "✓ 누수 없음 — {n}개 프로세스 모니터링 중.",
        "leak_severity_warn":  "주의",
        "leak_severity_danger":"경고",
        "leak_severity_critical":"위험",
        "leak_growth":         "+{mb} MB / 지난 {min}분",
        "leak_action_restart": "재시작 권장",
        "leak_disabled":       "누수 감지 비활성화됨.",

        # Session History
        "history_title":       "📅  세션 기록",
        "history_summary":     "최근 30일 요약",
        "history_total_ram":   "총 회수 RAM",
        "history_total_cycles":"총 사이클",
        "history_avg_pis":     "평균 AI 점수",
        "history_sessions":    "세션 수",
        "history_recent":      "최근 세션",
        "history_none":        "기록이 없습니다. 안전 또는 최대 부스트를 시작하면 여기에 쌓입니다.",
        "history_export":      "📥  CSV 내보내기",
        "history_session_row": "{date} {start}~{end} · {mode} · {cycles}사이클 · {ram}MB 회수 · AI {pis}",
        "toast_history_csv":   "✓ 세션 기록 CSV가 바탕화면에 저장됨",

        # Welcome dialog (first run only)
        "welcome_title":       "OMEGA X에 오신 것을 환영합니다",
        "welcome_subtitle":    "Windows를 더 빠르게 반응하게 만드는 도구",
        "welcome_step1_title": "1.  모드 고르기",
        "welcome_step1_desc":  "자동 부스트를 열고 안전 또는 최대를 고르세요. 둘 다 계속 돌면서 지금 하는 일에 맞춰 조정됩니다.",
        "welcome_step2_title": "2.  실측값 확인",
        "welcome_step2_desc":  "점수, 회수한 메모리, 적용 중인 모드 — 전부 이 PC에서 측정한 값입니다. 지어낸 숫자는 없습니다.",
        "welcome_step3_title": "3.  자동화 설정",
        "welcome_step3_desc":  "설정 → 스마트 자동화에서 게임 자동 부스트, 배터리 절약, 예약 정리를 켤 수 있습니다.",
        "welcome_get_started": "시작하기",
        "welcome_dont_show":   "다시 보지 않기",

        # Quit confirmation (when Core is running)
        "quit_title":          "OMEGA X 종료?",
        "quit_running":        "{mode} 실행 중입니다. 중지하고 종료할까요?",
        "quit_yes":            "중지하고 종료",
        "quit_no":             "취소",

        # Running progress (cumulative stats + log)
        "running_ram_freed":   "메모리 회수",
        "running_procs_handled":"최적화된 프로세스",
        "running_files_cleaned":"정리된 파일",
        "running_steps_done":  "완료된 단계",
        "running_action_log":  "지금 실행 중인 작업:",

        # Continuous mode (toggle on/off)
        "ai_lite_run_start":   "▶  안전 부스트 시작",
        "ai_lite_run_stop":    "■  안전 부스트 중지",
        "ai_hard_run_start":   "▶  최대 부스트 시작",
        "ai_hard_run_stop":    "■  최대 부스트 중지",
        "ai_status_idle":      "위 버튼을 클릭하여 지속 최적화를 시작하세요.",
        "ai_status_running":   "● {mode} 실행 중 — {n}번째 사이클",
        "ai_improve_title":    "AI 성능 점수",
        "ai_improve_ram":      "가용 메모리",
        "ai_improve_cpu":      "OMEGA X 자신",
        "ai_improve_freed":    "회수한 메모리",
        "ai_improve_cycles":   "실행된 사이클",
        "unit_cores":          "코어",
        "learn_title":         "이 PC에서 배운 것",
        "learn_desc":          "액션마다 가끔 일부러 건너뛰어서, 했을 때와 안 했을 때를 비교합니다. 효과가 없는 액션은 스스로 중단해요.",
        "learn_helps":         "효과 있음",
        "learn_neutral":       "차이 없음 \u2014 중단함",
        "learn_hurts":         "오히려 나빠짐 \u2014 중단함",
        "learn_learning":      "측정 중",
        "learn_samples":       "적용 {on}회 / 보류 {off}회",
        "learn_none":          "아직 잰 게 없어요 \u2014 Lite 나 Hard Core 를 잠시 돌려 주세요",
        "learn_reset":         "배운 것 지우기",
        "learn_policy_note":   "배운 결과는 위 작업의 '실행 여부'만 바꿉니다. 효과 있음 = 계속 실행, 차이 없음·나빠짐 = 실행 중단(나중에 다시 시험). 이 결과로 설정을 바꾸거나 되돌릴 수 없는 작업을 하지는 않습니다.",
        "learn_pol_keep":      "계속 실행",
        "learn_pol_stop":      "실행 중단",
        "learn_pol_test":      "번갈아 시험 중",
        "learn_now_on":        "지금 실행 중",
        "learn_now_off":       "지금 보류 중",
        "ui_copy_diag":        "진단 정보 복사",
        "ui_diag_copied":      "진단 정보를 클립보드에 복사했어요",
        "act_title":           "실제로 실행한 작업",
        "act_desc":            "실행한 작업과 건너뛴 작업을 사유까지 그대로 남깁니다. 실행 중이던 프로그램 이름이 함께 들어갑니다. 이 PC 안 activity.log 에만 저장하며, '기록 지우기'를 누르면 파일을 지웁니다.",
        "act_none":            "아직 기록이 없어요 \u2014 안전 부스트나 최대 부스트를 켜 주세요.",
        "act_copy":            "로그 복사",
        "act_open":            "로그 폴더 열기",
        "act_clear":           "기록 지우기",
        "act_copied":          "로그를 클립보드에 복사했어요",
        "act_cleared":         "기록을 지웠어요",
        "act_lines":           "{n}줄 \u00b7 최신이 아래",
        "act_r_learn_hold":    "효과 측정을 위해 보류",
        "act_r_not_due":       "이번 주기 아님",
        "act_r_ram_ok":        "메모리 여유 있음",
        "act_r_os_unsupported":"이 윈도우에서 미지원",
        "act_r_no_hybrid_cpu": "P/E 코어 CPU 아님",
        "act_skipped_head":    "건너뜀:",
        "predict_title":       "다음에 열 것 같은 앱",
        "predict_line":        "{app} \u2014 {pct}% (전환 {n}회 학습)",
        "predict_none":        "아직 근거가 부족해요 \u2014 앱을 오갈수록 배웁니다",
        "predict_prewarm":     "{app} 준비 중 ({pct}% 확률로 곧 쓸 앱)",
        "predict_toggle":      "쓰는 앱 패턴 학습",
        "predict_privacy":     "프로그램 이름과 시각만 이 PC 안에 저장해요. 끄면 파일을 지웁니다.",
        "effect_idle":         "아직 시작하지 않았어요",
        "effect_collecting":   "측정 중 \u2014 대상 {n}/{need}개, 비교군 {c}개",
        "effect_none":         "비교군과 차이 없음 \u2014 지금은 줄일 부하가 없어요",
        "effect_control_blocked": "비교군을 못 만들고 있어요 \u2014 {u}개 앱의 절전 모드 해제가 안 돼서 비교 대상이 되지 못했어요",
        "effect_unmeasurable": "CPU 로는 판정 불가 \u2014 대상 앱들이 원래 CPU 를 거의 안 써요 (현재 {h} 코어, 판정하려면 {f} 코어 필요)",
        "effect_scope_note":   "이 판정은 딱 하나만 잽니다 \u2014 절전 조치로 줄인 백그라운드 CPU. 포그라운드 부스트·스케줄러 힌트·GPU 큐·디스크 우선순위·전원 계획은 여기에 안 들어갑니다.",
        "effect_better":       "백그라운드 부하 {d} 코어 줄임 (대상 {nt}개 · 비교군 {nc}개)",
        "effect_worse":        "백그라운드 부하가 {d} 코어 늘었어요 (대상 {nt}개 · 비교군 {nc}개)",
        "ai_baseline_note":    "점수는 측정한 8가지를 합쳐 계산합니다 — 메모리, CPU 대기 시간, 안 쓰는 앱의 부하, 저장장치 사용량, 메모리 부족, PC 반응 속도, 모드 적중 여부, 실제로 처리한 작업량. RAM·CPU 수치는 이번 실행의 평균값입니다.",
        "pis_score_label":     "절전 중인 앱",
        "pis_score_avg":       "백그라운드 부하",
        "pis_factor_dominant": "우리가 줄인 부하",
        "pis_tier_excellent":  "최상 — 껐을 때보다 뚜렷하게 빨라졌습니다",
        "pis_tier_good":       "양호 — 눈에 띄게 빨라졌습니다",
        "pis_tier_stable":     "변화 없음 — 지금은 빠르게 할 게 없습니다",
        "pis_tier_minor":      "소폭 역효과 — 껐을 때보다 조금 느립니다",
        "pis_tier_idle":       "역효과 — 껐을 때가 더 나았습니다",
        "pis_tier_nodata":     "측정 중 — 잠시만 기다려 주세요",
        "pis_comp_memory":     "메모리",
        "pis_comp_cpu":        "CPU",
        "pis_comp_bg_cpu":     "안 쓰는 앱 부하",
        "pis_comp_responsive": "응답성",
        "pis_comp_disk":       "디스크 활동",
        "pis_comp_thrashing":  "메모리 부족",
        "pis_comp_smart_match":"모드 적중",
        "pis_comp_work_done":  "처리한 작업",

        # Friendly action labels (전문용어 → 초보자 친화적)
        "friendly_memory_cleanup":   "메모리 회수 중",
        "friendly_energy_saving":    "안 쓰는 앱 전력 절약",
        "friendly_cpu_balance":      "안 쓰는 앱 CPU 사용 줄이기",
        "friendly_app_boost":        "활성 앱 속도 향상",
        "friendly_disk_priority":    "앱이 저장장치를 먼저 쓰게 하기",
        "friendly_pause_services":   "Windows 뒷작업 잠시 멈춤",
        "friendly_disable_recording":"자동 게임 녹화 끄기",
        "friendly_clean_temp":       "임시 파일 삭제",
        "friendly_audio_priority":   "오디오/영상 우선 처리",
        "friendly_cpu_smart":        "CPU 코어 똑똑하게 배정",
        "friendly_power_mode":       "고성능 모드로 전환",
        "friendly_disk_cache":       "저장장치 임시 데이터 정리",
        "friendly_dns_flush":        "네트워크 주소 캐시 새로고침",
        "friendly_memory_compact":   "쓰지 않는 메모리 정리",
        "friendly_light_memory":     "가벼운 메모리 정리",
        "friendly_bg_mem_priority":  "안 쓰는 앱 메모리 뒤로 미루기",
        "friendly_pe_core_hint":     "빠른 코어와 절전 코어 나눠 쓰기",
        "friendly_timer_guard":      "안 쓰는 앱의 방해 차단",
        "friendly_gpu_priority":     "그래픽 처리 먼저 하기",
        "friendly_browser_tuning":   "브라우저 자원 균형 조정",
        "profile_game":              "게임",
        "profile_creative":          "창작",
        "profile_dev":               "작업",
        "profile_browser":           "멀티태스킹",
        "profile_office":            "작업",
        "profile_general":           "자동",
        "ui_refresh":                "↻  새로고침",
        "ui_copy_sysinfo":           "📋  시스템 정보 복사",
        "toast_sysinfo_copied":      "시스템 정보를 클립보드에 복사했습니다",
        "card_license_credits":      "🛡️  라이선스 · 만든 이",
        "status_optimal":            "✓  시스템이 정상 작동 중입니다",
        "splash_init":               "준비하는 중...",
        "splash_wait":               "몇 초 정도 걸릴 수 있습니다...",
        "init_failed":               "❌ 초기화에 실패했습니다.",

        # Impact summaries (오른쪽 표시)
        "impact_ram_freed":      "{mb} MB 회수",
        "impact_procs_handled":  "{count}개 처리",
        "impact_files":          "{count}개 파일",
        "impact_disabled":       "비활성화됨",
        "impact_applied":        "적용됨",
        "impact_skipped":        "건너뜀",

        # ── 언어 전환 누락분 보강 ──────────────────────────────
        "admin_dlg_title":       "관리자 권한 필요",
        "admin_dlg_msg":         ("{mode} 모드는 관리자 권한이 필요합니다.\n\n"
                                  "관리자 권한으로 재시작하시겠습니까?\n"
                                  "'예' 선택 시 UAC 창이 뜨고, 승인하면 자동으로 "
                                  "{mode} 모드가 시작됩니다."),
        "admin_dlg_restart":     "관리자 권한으로 재시작",
        "admin_toast_skip":      "관리자 권한 없이 진행합니다. 일부 기능이 제한됩니다.",
        "cancel":                "취소",
        "storage_found":         "{count}개 파일에서 {size} 발견",
        "storage_recycle_bin":   "휴지통",
        "generic_error":         "오류: {msg}",
        "consent_title":         "사용 동의",
        "consent_agree":         "동의하고 시작",
        "consent_decline":       "동의 안 함 (종료)",
        "license_title":         "라이선스",
        "license_body":          ("{copyright}\n\n"
                                  "OMEGA X 는 자유 소프트웨어입니다. 자유 소프트웨어 "
                                  "재단이 공표한 GNU 일반 공중 사용 허가서(GPL) 제3판 "
                                  "또는 (선택에 따라) 그 이후 판의 조건에 따라 자유롭게 "
                                  "사용·수정·재배포할 수 있습니다. 상업적 이용을 포함해 "
                                  "이용 분야에는 아무 제한이 없습니다.\n\n"
                                  "이 프로그램은 어떠한 보증도 하지 않으며, 상품성이나 "
                                  "특정 목적 적합성에 대한 묵시적 보증도 포함되지 "
                                  "않습니다. 자세한 내용은 GNU 일반 공중 사용 허가서를 "
                                  "확인하십시오.\n\n"
                                  "전체 소스 코드는 아래 링크에서 받을 수 있습니다."),
        "license_meta":          ("버전 v{version} · Python 3.14 + CustomTkinter + "
                                  "psutil\n"
                                  "모든 최적화는 되돌릴 수 있습니다. 시스템 프로세스는 "
                                  "보호되며 강제 종료하지 않습니다."),
        "license_view":          "라이선스 전문 보기",
        "license_source":        "소스 코드",

        # ── 확인 다이얼로그 / 파괴적 액션 ──────────────────────
        "ui_confirm":            "확인",
        "confirm_kill_title":    "프로세스를 종료할까요?",
        "confirm_kill_msg":      ("{name} (PID {pid}) 를 즉시 강제 종료합니다.\n\n"
                                  "저장하지 않은 작업은 사라지며, 되돌릴 수 없습니다."),
        "confirm_startup_title": "시작프로그램에서 제거할까요?",
        "confirm_startup_msg":   ("{name} 을(를) Windows 시작프로그램에서 제거합니다.\n\n"
                                  "백업을 남기므로 아래 목록에서 언제든 다시 되돌릴 수 있습니다."),
        "confirm_clean_title":   "임시 파일을 삭제할까요?",
        "confirm_clean_msg":     ("검사한 폴더에서 24시간이 지난 파일을 영구 삭제합니다. 휴지통으로 가지 않습니다.\n\n"
                                  "브라우저는 먼저 종료해 주세요. 실행 중에 캐시를 지우면 캐시가 손상될 수 있습니다."),
        "confirm_recycle_title": "휴지통을 비울까요?",
        "confirm_recycle_msg":   "{count}개 항목({size})이 영구 삭제됩니다. 되돌릴 수 없고, OMEGA X 도 복구해 드릴 수 없습니다.",
        "recycle_already_empty": "휴지통이 이미 비어 있습니다.",

        # ── 프로세스 표 ────────────────────────────────────────
        "apps_col_pid":          "PID",
        "apps_search_ph":        "이름으로 검색",
        "apps_no_match":         "검색어와 일치하는 프로세스가 없습니다.",

        # ── 시작프로그램 ──────────────────────────────────────
        "startup_none":          "등록된 시작프로그램이 없습니다.",
        "startup_disabled_card": "OMEGA X 가 제거한 항목",
        "startup_restore":       "되돌리기",
        "startup_none_disabled": "아직 제거한 항목이 없습니다. 제거한 항목은 여기서 되돌릴 수 있습니다.",
        "toast_restored":        "되돌렸습니다: {name}",
        "toast_restore_failed":  "{name} 을(를) 되돌리지 못했습니다",

        # ── 테마 ──────────────────────────────────────────────
        "settings_theme":        "테마",
        "theme_light":           "라이트",
        "theme_dark":            "다크",
        "theme_system":          "Windows 설정 따름",

        # ── 정리 결과 (영문 하드코딩이던 것) ────────────────────
        "toast_cleaned":         "{count}개 파일 정리 ({size})",
        "toast_scan_error":      "검사 실패: {msg}",
        "toast_clean_error":     "정리 실패: {msg}",
    },
}


class I18n:
    """Translation manager. Holds current language + provides t() lookup."""
    def __init__(self, default="en"):
        self.lang = default
        self._listeners = []

    def t(self, key, **kwargs):
        d = TRANSLATIONS.get(self.lang, TRANSLATIONS["en"])
        text = d.get(key, TRANSLATIONS["en"].get(key, key))
        if kwargs:
            try: return text.format(**kwargs)
            except Exception: return text
        return text

    def set_lang(self, lang):
        if lang in TRANSLATIONS and lang != self.lang:
            self.lang = lang
            for cb in self._listeners:
                try: cb()
                except Exception as _dx: DIAG.q("I18n.set_lang#0", _dx)

    def on_change(self, callback):
        self._listeners.append(callback)


def _detect_windows_language():
    """Detect Windows UI language and map to a supported translation key.

    Returns 'ko' if Windows UI language is Korean, otherwise 'en'.
    Uses GetUserDefaultUILanguage() (returns a LANGID). The lower 10 bits
    are the primary language ID — 0x12 == LANG_KOREAN.
    Falls back to Python's locale module, then to 'en'.
    """
    # Method 1: Win32 API — GetUserDefaultUILanguage (most accurate for UI lang)
    try:
        langid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
        primary_lang = langid & 0x3FF
        if primary_lang == 0x12:  # LANG_KOREAN
            return "ko"
        # Any other Windows UI language → English (only ko/en supported)
        return "en"
    except Exception as _dx:
        DIAG.q("module._detect_windows_language#0", _dx)

    # Method 2: Fallback — Python locale (in case Win32 call fails)
    try:
        import locale
        loc = locale.getdefaultlocale()[0] or ""
        if loc.lower().startswith("ko"):
            return "ko"
    except Exception as _dx:
        DIAG.q("module._detect_windows_language#1", _dx)

    return "en"


class AppSettings:
    """%APPDATA%/OMEGA_X/settings.json 에 사용자 설정을 보존한다.

    ★이게 없어서★ 언어 선택과 자동화 토글 3종이 앱을 끄면 전부
    초기화됐다. 값이 바뀔 때마다 즉시 저장한다(원자적 교체).
    """
    _DEFAULTS = {
        "lang": None,                  # None = Windows 언어 자동 감지
        "theme": "light",              # light | dark | system
        "auto_game_detect": False,
        "auto_scheduler": False,
        "auto_battery_saver": False,
        # 개입 기준 온도(℃). 0 = 자동(노트북/데스크톱 + 제조사로 추정).
        # ★코어·스레드 수로는 온도 한계를 알 수 없다★ — auto_thermal_threshold
        # 주석 참조.
        "thermal_threshold_c": 0,
        # 사용 패턴(앱 전환) 학습. 실행 파일 이름과 시각만 이 PC 안에
        # 저장한다. 끄면 즉시 수집을 멈추고 파일을 지운다.
        "ai_learn_apps": True,
        # 온도가 높을 때 CPU 최대 속도를 스스로 낮출지. 성능이 실제로
        # 줄어드는 동작이라 기본값은 꺼짐이다. 사용자가 켜야 켜진다.
        "thermal_auto_mitigate": False,
    }

    def __init__(self):
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "settings.json"
        self._lock = threading.Lock()
        self._data = dict(self._DEFAULTS)
        self.load()

    def load(self):
        try:
            if self._path.exists():
                with open(self._path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    for k in self._DEFAULTS:
                        if k in data:
                            self._data[k] = data[k]
        except Exception as _dx:
            DIAG.q("AppSettings.load#0", _dx)
        return self._data

    def get(self, key, default=None):
        return self._data.get(key, self._DEFAULTS.get(key, default))

    def set(self, key, value):
        with self._lock:
            if self._data.get(key) == value:
                return True
            self._data[key] = value
            return self._write()

    def _write(self):
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            tmp = self._path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self._data, f, ensure_ascii=False, indent=1)
            os.replace(str(tmp), str(self._path))
            return True
        except Exception:
            return False


SETTINGS = AppSettings()

# Global i18n instance — 저장된 언어가 있으면 그걸, 없으면 Windows 언어
I18N = I18n(SETTINGS.get("lang") or _detect_windows_language())
def t(key, **kwargs): return I18N.t(key, **kwargs)


# ============================================================================
# WINDOWS API
# ============================================================================
kernel32 = ctypes.windll.kernel32
ntdll    = ctypes.windll.ntdll
psapi    = ctypes.windll.psapi
user32   = ctypes.windll.user32

# ─────────────────────────────────────────────────────────────────
# ★신규★ ctypes 시그니처 명시 (x64 핸들 절단 방지)
# ─────────────────────────────────────────────────────────────────
# 기존 코드는 파일 전체에 argtypes/restype 이 하나도 없었다. ctypes 의
# 기본 restype 은 c_int(32비트)라서 x64 에서 OpenProcess/OpenThread 가
# 돌려주는 HANDLE(64비트)이 잘리고, 0x7FFFFFFF 를 넘는 값은 음수가 된다.
# 그 상태로 CloseHandle 에 넘기면 '엉뚱한 핸들'을 닫을 수 있다.
# 여기서 한 번만 제대로 선언해두면 파일 전체 호출이 안전해진다.
def _sig(dll, name, restype, *argtypes):
    try:
        fn = getattr(dll, name)
        fn.restype = restype
        if argtypes:
            fn.argtypes = list(argtypes)
        return fn
    except Exception:
        return None

_HANDLE = wintypes.HANDLE
_sig(kernel32, 'OpenProcess',      _HANDLE, wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
_sig(kernel32, 'OpenThread',       _HANDLE, wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
_sig(kernel32, 'CloseHandle',      wintypes.BOOL, _HANDLE)
_sig(kernel32, 'SetThreadPriority', wintypes.BOOL, _HANDLE, ctypes.c_int)
_sig(kernel32, 'SetPriorityClass',  wintypes.BOOL, _HANDLE, wintypes.DWORD)
_sig(kernel32, 'SetProcessInformation', wintypes.BOOL,
     _HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD)
_sig(kernel32, 'SetProcessDefaultCpuSets', wintypes.BOOL,
     _HANDLE, ctypes.c_void_p, wintypes.ULONG)
_sig(psapi,    'EmptyWorkingSet',  wintypes.BOOL, _HANDLE)
_sig(ntdll,    'NtSetInformationProcess', ctypes.c_long,
     _HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.ULONG)
_sig(ntdll,    'NtSetSystemInformation', ctypes.c_long,
     ctypes.c_int, ctypes.c_void_p, wintypes.ULONG)
try:
    _sig(ctypes.windll.gdi32, 'D3DKMTSetProcessSchedulingPriorityClass',
         ctypes.c_long, _HANDLE, ctypes.c_int)
    _sig(ctypes.windll.gdi32, 'D3DKMTGetProcessSchedulingPriorityClass',
         ctypes.c_long, _HANDLE, ctypes.c_void_p)
except Exception as _dx:
    DIAG.q("module.toplevel#0", _dx)

# ─────────────────────────────────────────────────────────────────
# ★신규★ 최소 권한 접근 마스크
# ─────────────────────────────────────────────────────────────────
# 기존 코드는 어디서나 PROCESS_ALL(0x1F0FFF, XP 시절 ALL_ACCESS)를
# 요구했다. 우선순위/IO/EcoQoS 변경엔 SET_INFORMATION 만 있으면 되는데,
# 전권을 달라고 하면 관리자 권한으로도 PPL·보호 프로세스에서 OpenProcess
# 가 그냥 실패한다 → 최적화가 '조용히 아무것도 안 하는' 상태가 된다.
# 필요한 만큼만 요구하면 성공률이 눈에 띄게 올라간다.
PROC_SET_INFO        = 0x0200   # PROCESS_SET_INFORMATION
PROC_SET_QUOTA       = 0x0100   # PROCESS_SET_QUOTA (EmptyWorkingSet)
PROC_QUERY_LIMITED   = 0x1000   # PROCESS_QUERY_LIMITED_INFORMATION
PROC_QUERY_INFO      = 0x0400   # PROCESS_QUERY_INFORMATION
# 용도별 조합
ACC_SET_PRIORITY = PROC_SET_INFO | PROC_QUERY_LIMITED
ACC_TRIM_WS      = PROC_SET_QUOTA | PROC_QUERY_INFO | PROC_QUERY_LIMITED
ACC_GPU_PRIO     = PROC_SET_INFO | PROC_QUERY_INFO | PROC_QUERY_LIMITED

def _open_proc(pid, access):
    """최소 권한 우선, 실패하면 한 단계 넓혀 재시도. 실패 시 0."""
    try:
        h = kernel32.OpenProcess(access, False, int(pid))
        if h:
            return h
        # QUERY_LIMITED 가 막히는 구형 경로 대비 1회 폴백
        h = kernel32.OpenProcess(access | PROC_QUERY_INFO, False, int(pid))
        return h or 0
    except Exception:
        return 0

def _close(h):
    try:
        if h: kernel32.CloseHandle(h)
    except Exception as _dx:
        DIAG.q("module._close#0", _dx)

def _get_windows_version():
    try:
        class OSVERSIONINFOEXW(ctypes.Structure):
            _fields_ = [
                ("dwOSVersionInfoSize", ctypes.c_ulong),
                ("dwMajorVersion",      ctypes.c_ulong),
                ("dwMinorVersion",      ctypes.c_ulong),
                ("dwBuildNumber",       ctypes.c_ulong),
                ("dwPlatformId",        ctypes.c_ulong),
                ("szCSDVersion",        ctypes.c_wchar * 128),
                ("wServicePackMajor",   ctypes.c_ushort),
                ("wServicePackMinor",   ctypes.c_ushort),
                ("wSuiteMask",          ctypes.c_ushort),
                ("wProductType",        ctypes.c_byte),
                ("wReserved",           ctypes.c_byte),
            ]
        info = OSVERSIONINFOEXW()
        info.dwOSVersionInfoSize = ctypes.sizeof(info)
        ntdll.RtlGetVersion(ctypes.byref(info))
        return info.dwMajorVersion, info.dwMinorVersion, info.dwBuildNumber
    except Exception:
        return 10, 0, 19045

WIN_MAJOR, WIN_MINOR, WIN_BUILD = _get_windows_version()
IS_WIN11      = WIN_BUILD >= 22000
IS_WIN11_22H2 = WIN_BUILD >= 22621

# ─────────────────────────────────────────────────────────────────
# CPU SET 정보 (Win10 1607+) — P코어/E코어 판별의 유일한 정확한 방법
# ─────────────────────────────────────────────────────────────────
# 기존 _is_hybrid_cpu() 는 "제조사 문자열에 intel 이 들어있고 Win11이면
# 하이브리드"로 판정했다. 11세대 이하 인텔은 하이브리드가 아닌데 True 가
# 나오고, 하이브리드 AMD(Zen5c)·ARM 은 False 가 나온다. 커널이 알려주는
# EfficiencyClass 를 직접 읽는다.
class _CPU_SET_INFO(ctypes.Structure):
    _fields_ = [
        ("Size",                 wintypes.DWORD),
        ("Type",                 wintypes.DWORD),
        ("Id",                   wintypes.DWORD),
        ("Group",                wintypes.WORD),
        ("LogicalProcessorIndex", ctypes.c_ubyte),
        ("CoreIndex",            ctypes.c_ubyte),
        ("LastLevelCacheIndex",  ctypes.c_ubyte),
        ("NumaNodeIndex",        ctypes.c_ubyte),
        ("EfficiencyClass",      ctypes.c_ubyte),
        ("AllFlags",             ctypes.c_ubyte),
        ("Reserved",             wintypes.DWORD),
        ("AllocationTag",        ctypes.c_ulonglong),
    ]


def _query_cpu_sets():
    """(p_core_ids, e_core_ids, all_ids) 반환. 실패하면 ([], [], []).

    EfficiencyClass 가 높을수록 고성능 코어다(=P코어). 값이 한 종류뿐이면
    하이브리드가 아니므로 P/E 구분 없이 전부 all_ids 로만 채운다.
    """
    try:
        fn = kernel32.GetSystemCpuSetInformation
    except Exception:
        return [], [], []
    try:
        need = wintypes.ULONG(0)
        # GetCurrentProcess() 의사 핸들은 항상 -1. ctypes 기본 int 로 넘기면
        # x64 에서 HANDLE(64비트) 로 올바르게 확장되지 않을 수 있으므로
        # c_void_p 로 명시한다.
        hproc = ctypes.c_void_p(-1)
        fn(None, 0, ctypes.byref(need), hproc, 0)
        if need.value == 0:
            return [], [], []
        buf = (ctypes.c_ubyte * need.value)()
        if not fn(buf, need.value, ctypes.byref(need), hproc, 0):
            return [], [], []

        entries = []
        off = 0
        base = ctypes.addressof(buf)
        while off + ctypes.sizeof(wintypes.DWORD) <= need.value:
            rec = _CPU_SET_INFO.from_address(base + off)
            size = rec.Size
            if size < 8 or off + size > need.value:
                break
            if rec.Type == 0:                       # CpuSetInformation
                # Parked(0x1) 코어는 대상에서 제외
                if not (rec.AllFlags & 0x1):
                    entries.append((rec.Id, rec.EfficiencyClass))
            off += size

        if not entries:
            return [], [], []
        all_ids = [e[0] for e in entries]
        classes = {e[1] for e in entries}
        if len(classes) < 2:
            return [], [], all_ids               # 하이브리드 아님
        top = max(classes)
        p_ids = [e[0] for e in entries if e[1] == top]
        e_ids = [e[0] for e in entries if e[1] != top]
        return p_ids, e_ids, all_ids
    except Exception:
        return [], [], []


P_CORE_SETS, E_CORE_SETS, ALL_CPU_SETS = _query_cpu_sets()
IS_HYBRID = bool(P_CORE_SETS and E_CORE_SETS)

CREATE_NO_WINDOW = 0x08000000

SYSTEM_WHITELIST = frozenset({
    "system", "svchost.exe", "wininit.exe", "services.exe", "csrss.exe",
    "winlogon.exe", "explorer.exe", "smss.exe", "lsass.exe", "nvcontainer.exe",
    "dwm.exe", "registry", "fontdrvhost.exe", "audiodg.exe", "spoolsv.exe",
    "taskmgr.exe", "conhost.exe", "sihost.exe", "ctfmon.exe",
    "runtimebroker.exe", "searchhost.exe", "securityhealthsystray.exe",
    "textinputhost.exe", "memory compression", "memcompression", "secure system",
    "msmpeng.exe", "mssense.exe", "securityhealthservice.exe",
})

SAFE_KEYWORDS = (
    "nvidia", "amd", "intel", "antivirus", "defender",
    "mbam", "avast", "eset", "kaspersky", "audiodg",
    "asio", "audio", "voicemeeter",
)

# ★신규★ NO_DEGRADE_KEYWORDS — SAFE_KEYWORDS 와 역할이 다르다.
#
# SAFE_KEYWORDS 는 guard.check_pid 도 함께 쓴다. 즉 여기 들어간 이름은
# '강등 금지'가 아니라 '아예 손대지 말라'가 되어 포그라운드 부스트도
# 막힌다. OBS 나 발로란트를 SAFE_KEYWORDS 에 넣으면 그 앱이 포그라운드일
# 때조차 우선순위 상향이 안 걸린다 — 정반대의 결과다.
#
# 그래서 목록을 둘로 나눈다:
#   SAFE_KEYWORDS       = 어떤 방향으로도 건드리지 않음 (시스템·백신·오디오)
#   NO_DEGRADE_KEYWORDS = 내리지만 않음. 포그라운드면 정상적으로 올려줌
#
# 부분 문자열 매칭이라 짧은 토큰은 오탐을 만든다. 실제로 "esea" 는
# "research" 에, "logi" 는 "login" 에, "intel" 은 "intellij" 에 걸린다.
# 아래 토큰은 전부 오탐 여지가 낮은 길이로만 남겼다.
NO_DEGRADE_KEYWORDS = (
    # 안티치트 — 강등하면 스터터·강제 종료·킥이 난다.
    "anticheat", "easyanticheat", "battleye", "beservice",
    "vgc.exe", "vgtray", "vanguard", "gameguard", "xigncode",
    "punkbuster", "ricochet", "faceit",
    # 입력/주변기기 — 폴링 스레드를 내리면 즉시 입력 지연으로 체감된다.
    "logitech", "lghub", "razer", "synapse", "corsair", "icue",
    "steelseries", "wooting", "hidfind",
    # 오버레이/캡처 — 프레임 파이프라인에 직접 낀다.
    "obs64", "obs32", "streamlabs", "rtsshooks", "rtss.exe",
    "afterburner",
    # 게임 런처/오버레이 — 게임과 같은 프레임 경로를 공유한다.
    "steamwebhelper", "gameoverlayui",
)

# ★신규★ 자기 자신 보호
# 기존엔 OMEGA_X.exe(또는 python.exe)가 is_safe_to_modify 를 통과했다.
# 즉 최적화 루프가 자기 자신에게 EcoQoS 를 걸고 BELOW_NORMAL 로 내린
# 다음 그 상태로 계속 최적화를 돌렸다. 자기 손발을 묶고 뛰는 셈.
SELF_PID = os.getpid()
try:
    _SELF_NAME = os.path.basename(sys.executable).lower()
except Exception:
    _SELF_NAME = "omega_x.exe"
_SELF_NAMES = frozenset({_SELF_NAME, "omega_x.exe", "omega_x_lite.exe",
                         "omega15.exe", "omega_15.exe"})

POWER_HIGH = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"
POWER_BAL  = "381b4222-f694-41f0-9685-ff5bb260df2e"

# ★패치32 — 게임 서명 확대★ exe 이름(소문자)에 대한 '부분 문자열' 검사다.
#   누락은 싸고(general 로 갈 뿐) 오인은 비싸다(최대 부스트가 멋대로 켜진다).
#   그래서 짧고 흔한 낱말(rust, ark, war, delta, hunt)은 안 넣고
#   실행 파일 이름으로 좁혔다 — rustclient / peak.exe / cod.exe / wow.exe.
#   마인크래프트 자바 에디션은 창이 javaw.exe 라 여기서 못 잡는다(dev 로 간다).
GAME_SIGS = (
    # ── 런처 ── 게임 직전·직후 상태라 같이 본다
    "epicgames", "battlenet", "riotclient",
    # ── FPS · 배틀로얄 · 추출 ──
    "valorant", "csgo", "cs2.exe", "overwatch", "fortnite", "r5apex",
    "pubg", "tslgame", "rainbowsix", "tarkov", "deltaforce", "raiders",
    "thefinals", "battlefield", "bf6.exe", "bf2042", "cod.exe", "modernwarfare",
    "blackops", "warzone", "helldivers", "destiny2", "crossfire",
    "suddenattack", "arenabreakout", "huntgame", "titanfall", "halo",
    "warthunder", "aces.exe", "deadbydaylight",
    "theisle", "squadgame", "insurgency", "readyornot", "grayzone",
    # ── MOBA · 히어로 · 격투 ──
    "league", "dota2", "deadlock", "marvelrivals", "marvel rivals",
    "smite", "predecessor",
    "tekken", "streetfighter", "mortalkombat", "guiltygear", "granblue",
    "brawlhalla", "rivalsofaether",
    # ── 생존 · 샌드박스 ──
    "minecraft", "roblox", "rustclient", "dayz", "7daystodie", "valheim",
    "palworld", "enshrouded", "vrising", "projectzomboid", "terraria",
    "tmodloader", "starbound", "satisfactory", "factorio", "stardew",
    "rimworld", "dontstarve", "unturned", "onehuman", "icarus",
    "greenhell", "subnautica", "raft.exe", "arkascended", "shootergame",
    # ── 협동 · 파티 ──
    "gmod", "left4dead", "tf_win64", "phasmophobia", "lethalcompany",
    "repo.exe", "peak.exe", "content warning", "among us", "deeprock",
    "fsd-win64", "payday", "gtfo", "vrchat",
    # ── 싱글 AAA ──
    "eldenring", "nightreign", "darksouls", "sekiro", "armoredcore",
    "cyberpunk", "witcher3", "rdr2", "gta5", "gtav", "fivem", "redm",
    "skyrim", "fallout4", "fallout76", "starfield", "baldur", "bg3.exe",
    "hogwarts", "spider-man", "godofwar", "horizonzerodawn", "deathstranding",
    "blackmyth", "wukong", "b1-win64", "expedition33", "kingdomcome",
    "silenthill",
    "residentevil", "monsterhunter", "spacemarine", "assassin", "farcry",
    "watchdogs", "mafia", "metalgear", "dyinglight",
    # ── 전략 · 경영 · RPG ──
    "civilization", "hoi4", "eu4.exe", "eu5.exe", "ck3.exe", "stellaris",
    "totalwar",
    "warhammer", "aoe2de", "starcraft", "sc2_x64", "frostpunk",
    "citiesskylines", "anno1800", "diablo", "pathofexile",
    "lastepoch", "grimdawn", "torchlight", "slaythespire", "balatro",
    "hades", "isaac", "vampiresurvivors", "limbuscompany", "hearthstone",
    "masterduel", "geometrydash", "ittakestwo",
    # ── 레이싱 · 스포츠 · 시뮬 ──
    "beamng", "forza", "assettocorsa", "iracing", "f1_24", "f1_25",
    "f1_26", "eurotrucks", "amtrucks", "farmingsimulator", "flightsimulator",
    "fc24", "fc25", "fc26", "fifa", "efootball", "nba2k", "football manager",
    "russianfishing", "kartdrift", "kartrider",
    # ── MMO · 가챠 ──
    "ffxiv", "wow.exe", "wowclassic", "lostark", "blackdesert", "warframe",
    "guildwars2", "newworld", "albiononline", "rs2client", "runescape",
    "genshin", "yuanshen", "starrail", "hkrpg", "zenlesszonezero",
    "honkai", "wutheringwaves", "nikke", "wherewindsmeet", "naraka",
    # ── 국내 온라인 ──
    "maplestory", "dnf.exe", "fconline", "fifaonline", "lineage", "aion",
    "bladeandsoul", "mabinogi", "elsword", "cyphers",
)

DEV_SIGS = ("code", "pycharm", "idea", "eclipse", "devenv", "node",
            "javaw", "git", "wsl", "cursor", "sublime", "atom",
            "vim", "rider")

CREATIVE_SIGS = ("premiere", "davinci", "photoshop", "blender",
                 "aftereffects", "illustrator", "figma", "resolve",
                 "lightroom", "obs64", "obs32", "audition", "cinema4d")

BROWSER_SIGS = ("chrome", "msedge", "firefox", "opera", "brave", "vivaldi")
OFFICE_SIGS  = ("winword", "excel", "powerpnt", "outlook", "teams",
                "zoom", "notion", "slack", "onenote")

BURST_INPUT_MS    = 150
BURST_AFFINITY_MS = 1500
BURST_IO_MS       = 1500
BURST_TIMER_MS    = 1500
BURST_THROTTLE_MS = 1500

OBSERVER_INTERVAL = 1.0
AUTO_INTERVAL     = 6.0

RAM_WARN     = 75.0
RAM_CRITICAL = 85.0

COOLDOWNS = {
    "thread_burst":  0.4,
    "affinity":      1.0,
    "mmcss":         1.5,
    "bg_throttle":   0.6,
    "io_priority":   1.0,
    "idle_cleanup":  5.0,
    "ecoqos":        2.0,
}

PERF_HISTORY: list = []
MAX_HISTORY = 300


def is_admin():
    """Check if running as admin. Return True if yes, False otherwise."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def request_admin_elevation():
    """Request UAC elevation if not already admin.
    Returns True if user grants elevation, False otherwise.
    """
    try:
        # frozen EXE 는 exe 경로를 인자로 넘기면 안 된다 (스크립트와 다름).
        if getattr(sys, "frozen", False):
            params = None
        else:
            params = f'"{os.path.abspath(sys.argv[0])}"'
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1
        )
        return True
    except Exception:
        return False


def request_admin_with_action(action_id: str) -> bool:
    """UAC 띄우고 admin으로 재시작하면서 자동 실행할 액션 ID 전달.
    action_id 예: 'lite', 'hard'.
    성공 시 (사용자가 UAC 허용) True 반환 후 현재 프로세스가 종료되어야 함.
    실패/거부 시 False 반환, 현재 프로세스 계속 실행."""
    if is_admin():
        return True
    try:
        # argv 인젝션 방지: action_id에 공백/특수문자 차단
        safe_id = "".join(c for c in str(action_id) if c.isalnum() or c in "_-")[:20]
        # frozen EXE 는 exe 경로를 인자로 넘기지 않고 플래그만 전달.
        if getattr(sys, "frozen", False):
            params = f'--auto-action={safe_id}'
        else:
            script_path = os.path.abspath(sys.argv[0])
            params = f'"{script_path}" --auto-action={safe_id}'
        # SW_SHOWNORMAL = 1
        # 반환값: > 32 = 성공, <= 32 = 실패 (5 = ERROR_ACCESS_DENIED 등)
        ret = ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, params, None, 1)
        return int(ret) > 32
    except Exception:
        return False


# ============================================================================
# ERROR LOGGER — Persists uncaught exceptions for support / MS Store crash tracking
# ============================================================================
class ErrorLogger:
    """Writes uncaught exceptions to %APPDATA%\\OMEGA_X\\error.log.
    Auto-rotates when file exceeds 1MB. Last 5 errors kept in memory."""

    MAX_LOG_BYTES = 1_000_000  # 1MB

    def __init__(self):
        try:
            self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
            self._dir.mkdir(parents=True, exist_ok=True)
            self._path = self._dir / "error.log"
        except Exception:
            self._path = None
        self.recent = deque(maxlen=5)

    def log(self, exc_type, exc_value, tb_str: str, context: str = ""):
        """Record one error to disk + memory."""
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_lines = [
            f"\n{'=' * 70}",
            f"[{ts}] {exc_type.__name__}: {exc_value}",
            f"Context: {context}" if context else "",
            f"OMEGA X v{APP_VERSION} · Win {WIN_MAJOR}.{WIN_MINOR} build {WIN_BUILD}",
            tb_str,
        ]
        entry = "\n".join(line for line in entry_lines if line)
        self.recent.append(entry)

        if not self._path: return
        try:
            # Rotate if too big
            if self._path.exists() and self._path.stat().st_size > self.MAX_LOG_BYTES:
                old = self._path.with_suffix(".log.old")
                try: old.unlink()
                except Exception as _dx: DIAG.q("ErrorLogger.log#0", _dx)
                self._path.rename(old)
            # Append new entry
            with open(self._path, "a", encoding="utf-8") as f:
                f.write(entry + "\n")
        except Exception as _dx:
            DIAG.q("ErrorLogger.log#1", _dx)

    def get_log_path(self) -> str:
        return str(self._path) if self._path else "(unavailable)"


# Singleton
ERROR_LOG = ErrorLogger()


def install_global_exception_handler():
    """Catch uncaught exceptions in main + threads."""
    import traceback as _tb

    def _handle(exc_type, exc_value, exc_tb):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        tb_str = "".join(_tb.format_exception(exc_type, exc_value, exc_tb))
        ERROR_LOG.log(exc_type, exc_value, tb_str, "main thread")
        # Still print to stderr for dev visibility
        sys.__excepthook__(exc_type, exc_value, exc_tb)

    sys.excepthook = _handle

    # Thread exceptions (Python 3.8+)
    try:
        def _thread_handle(args):
            tb_str = "".join(_tb.format_exception(
                args.exc_type, args.exc_value, args.exc_traceback))
            ERROR_LOG.log(args.exc_type, args.exc_value, tb_str,
                         f"thread: {args.thread.name if args.thread else '?'}")
        threading.excepthook = _thread_handle
    except Exception as _dx:
        DIAG.q("module.install_global_exception_handler#0", _dx)


# ============================================================================
# UTILITIES
# ============================================================================
def desktop_path(filename: str) -> str:
    return str(Path.home() / "Desktop" / filename)

def save_and_open(filename: str, content: str, encoding="utf-8") -> str:
    import webbrowser
    path = desktop_path(filename)
    try:
        with open(path, "w", encoding=encoding) as f:
            f.write(content)
        if filename.endswith(".html"):
            webbrowser.open(f"file:///{path.replace(os.sep, '/')}")
    except Exception as _dx:
        DIAG.q("module.save_and_open#0", _dx)
    return path

# ★수정★ 사이클당 3회 이상(_run_cycle / _measure_full /
# _apply_ecoqos_bulk / 각 액션) 호출되면서 매번 psutil.Process(pid).name()
# 으로 핸들을 열었다. pid 는 GetForegroundWindow 로 싸게 얻고, 이름은
# pid 가 바뀌었을 때만 조회한다. 0.5초 TTL.
_FG_CACHE = {"t": 0.0, "pid": None, "name": "unknown"}
_FG_LK = threading.Lock()

# ============================================================================
# ★신규★ 중앙 지연 스케줄러 — threading.Timer 남발 제거
# ============================================================================
# 기존: 액션 하나당 threading.Timer 를 새로 만들었다. Hard Core 는 사이클
# (4초)마다 thread_burst / io_priority / bg_throttle / core_throttle 등
# 3~5개를 예약하므로 초당 약 1개꼴로 OS 스레드가 생성·소멸했다. 윈도우에서
# 스레드 생성은 스택 예약(기본 1MB commit-on-demand) + 스케줄러 등록을
# 동반하는 무거운 작업이고, 이게 바로 이 앱이 줄이겠다는 컨텍스트 스위치를
# 스스로 만들어내는 자충수였다.
# → 스레드 1개 + 힙으로 전부 처리한다.
class _DelayScheduler:
    def __init__(self):
        import heapq
        self._heap = []
        self._heapq = heapq
        self._cv = threading.Condition()
        self._seq = 0
        self._started = False

    def _ensure(self):
        if self._started: return
        with self._cv:
            if self._started: return
            self._started = True
            threading.Thread(target=self._loop, daemon=True,
                             name="omega-sched").start()

    def call_later(self, delay, fn):
        self._ensure()
        due = time.monotonic() + max(0.0, delay)
        with self._cv:
            self._seq += 1
            self._heapq.heappush(self._heap, (due, self._seq, fn))
            self._cv.notify()

    def _loop(self):
        while True:
            with self._cv:
                if not self._heap:
                    self._cv.wait(1.0); continue
                due, _, fn = self._heap[0]
                now = time.monotonic()
                if due > now:
                    self._cv.wait(min(due - now, 1.0)); continue
                self._heapq.heappop(self._heap)
            try: fn()
            except Exception as _dx: DIAG.q("_DelayScheduler._loop#0", _dx)

    def pending(self):
        with self._cv: return len(self._heap)


SCHED = _DelayScheduler()


def get_foreground_info():
    now = time.monotonic()
    c = _FG_CACHE
    if now - c["t"] < 0.5:
        return c["name"], c["pid"]
    try:
        hwnd = user32.GetForegroundWindow()
        pid = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        v = pid.value
        if v == 0:
            with _FG_LK:
                c["t"] = now; c["pid"] = None; c["name"] = "unknown"
            return "unknown", None
        if v == c["pid"]:
            with _FG_LK: c["t"] = now
            return c["name"], v
        name = psutil.Process(v).name().lower()
        with _FG_LK:
            c["t"] = now; c["pid"] = v; c["name"] = name
        return name, v
    except Exception:
        return c["name"], c["pid"]

def record_perf(cpu, ram, score):
    PERF_HISTORY.append({
        "time":  datetime.now().strftime("%m/%d %H:%M"),
        "cpu":   round(cpu, 1),
        "ram":   round(ram, 1),
        "score": score,
    })
    if len(PERF_HISTORY) > MAX_HISTORY:
        PERF_HISTORY.pop(0)

# ★★수정(치명적)★★ ────────────────────────────────────────────
# psutil 의 Windows 구현(_pswindows.Process.status)은
#     suspended → STATUS_STOPPED, 그 외 전부 → STATUS_RUNNING
# 만 반환한다. 리눅스의 'sleeping' 은 Windows 에 존재하지 않는다.
# 그런데 이 파일의 세 곳이 status == "sleeping" 을 필수 조건으로 걸고
# 있었다. 즉 아래 세 액션은 '실행은 되지만 대상이 0개'인 완전한
# no-op 였다.
#   · LatencyOptimizer.idle_cleanup
#   · ModernOptimizer.lower_bg_memory_priority  (2차 작업의 핵심 신규 액션)
#   · CoreMode._apply_ecoqos_bulk               (Hard Core 의 주력 절전 액션)
# 백그라운드 부하가 줄지 않으니 AI 점수에 잡힐 변화도 없었다.
def proc_is_idle(inf, cpu_max=0.3) -> bool:
    """Windows 에서 '지금 놀고 있는 프로세스'를 판정한다.
    status 대신 실제 CPU 사용률을 쓴다(중단된 프로세스는 항상 참)."""
    if inf.get("status") == "stopped":
        return True
    try:
        return (inf.get("cpu_percent", 0) or 0) < cpu_max
    except Exception:
        return False


def is_safe_to_modify(name: str) -> bool:
    nl = (name or "").lower()
    if nl in SYSTEM_WHITELIST:
        return False
    if nl in _SELF_NAMES:          # ★추가★ 자기 자신은 절대 대상 아님
        return False
    if any(k in nl for k in SAFE_KEYWORDS):
        return False
    return True


def is_target(pid, name) -> bool:
    """★신규★ 최적화 대상 판정의 단일 진입점.

    기존 코드의 모든 강등 액션(_throttle_bg_cpu / _apply_ecoqos_bulk /
    lower_bg_memory_priority / io_priority_boost / apply_core_split)은
    "이름이 안전목록에 없고 pid != fg_pid" 만 확인했다. 문제는
    fg_pid 가 GetForegroundWindow 가 돌려주는 pid '하나'라는 점이다.

    크롬·엣지·디스코드·일렉트론 앱·다수의 최신 게임은 실제 작업을
    자식 프로세스가 한다(렌더러·GPU 프로세스·서브프로세스). 그래서
    유튜브를 보는 동안 chrome.exe 본체만 제외되고 정작 디코딩·렌더링을
    하는 자식 프로세스는 전부 BELOW_NORMAL + EcoQoS + 메모리 우선순위
    하향 + IO Low 를 동시에 맞았다. 사용자가 보고 있는 바로 그 앱을
    최적화 도구가 직접 느리게 만든 것이다.

    이제 포그라운드 '프로세스 트리 전체'를 제외한다.
    """
    if pid in (0, 4) or pid == SELF_PID:
        return False
    if not is_safe_to_modify(name):
        return False
    nl = (name or "").lower()
    if any(k in nl for k in NO_DEGRADE_KEYWORDS):
        return False
    if FG.is_protected(pid):
        return False
    return True

def format_bytes(b: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if b < 1024:
            return f"{b:.1f}{unit}"
        b /= 1024
    return f"{b:.1f}PB"


# Auto-elevation 제거됨 — admin 권한은 필요한 작업(예: Hard Core)을 사용자가
# 클릭했을 때만 런타임에 요청. 일반 권한으로도 프로그램 실행 가능.


# ============================================================================
# OBSERVER — Cached System Metrics
# ============================================================================
class WinPerfCounters:
    PDH_FMT_DOUBLE = 0x00000200

    class _CV(ctypes.Structure):
        _fields_ = [("CStatus", ctypes.c_ulong),
                    ("doubleValue", ctypes.c_double)]

    # 표본 하나는 노이즈가 크다(대표님 실측: 1.5초에 ±43~60%).
    # 최근 표본의 중앙값을 노출해 단발 스파이크가 점수를 흔들지 못하게 한다.
    SMOOTH_N = 5

    def __init__(self):
        self._cpu_q = self._disk_q = self._pf = self._cs = 0.0
        self._disk_busy = 0.0     # 100 - % Idle Time
        self._hard_faults = 0.0   # Pages Input/sec (하드 폴트만)
        self._hist = {}           # 평활용 최근 표본
        self._lk = threading.Lock()
        self._ok = False
        # 진단용: 왜 실패했는지 UI/로그에서 볼 수 있어야 한다.
        self.fail_reason = ""
        self._stop = threading.Event()
        self._init()
        if self._ok:
            threading.Thread(target=self._loop, daemon=True).start()

    # ★★수정(치명적)★★ ─────────────────────────────────────────
    # 기존 코드는 PdhAddCounterW 에 영문 카운터 경로를 넘겼다.
    # MSDN 명시: PdhAddCounter 에 넘기는 경로는 '현지화된' 이름이어야
    # 한다. 한글 Windows 의 실제 경로는
    #     \System\Processor Queue Length  →  \System\프로세서 큐 길이
    # 이므로 영문 경로는 PDH_CSTATUS_NO_OBJECT 로 실패한다.
    # r1/r2 실패 → return → self._ok=False → 수집 스레드가 아예 기동하지
    # 않는다. 그 결과 cpu_queue / disk_queue / page_faults /
    # ctx_switches 네 값이 앱 실행 내내 0.0 으로 고정된다.
    #
    # 이 네 값에 의존하는 것:
    #   · PIS 컴포넌트 responsive(0.18) + disk(0.12) + thrashing(0.10)
    #     = 전체 가중치의 40% 가 상시 0
    #   · compute_lpi 의 io_p / cpu_p 항
    #   · AICore._normalize 의 12개 특징 중 4개(2,3,4,5번)
    #     → STUTTER 상태는 그 4개에 가중치가 몰려 있어 사실상 감지 불가
    #
    # 해결: 언어 중립 API 인 PdhAddEnglishCounterW 를 우선 사용하고,
    # 없거나 실패하면 기존 PdhAddCounterW 로 폴백한다.
    def _init(self):
        try:
            p = ctypes.windll.pdh
        except Exception:
            self.fail_reason = "pdh.dll load failed"
            return
        try:
            # x64 에서 핸들이 32비트로 잘리는 것을 막는다(파일 전체 방침).
            try:
                p.PdhOpenQueryW.argtypes = [wintypes.LPCWSTR, ctypes.c_size_t,
                                            ctypes.POINTER(ctypes.c_void_p)]
                p.PdhOpenQueryW.restype = ctypes.c_long
                for _fn in ("PdhAddEnglishCounterW", "PdhAddCounterW"):
                    _f = getattr(p, _fn, None)
                    if _f is not None:
                        _f.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR,
                                       ctypes.c_size_t,
                                       ctypes.POINTER(ctypes.c_void_p)]
                        _f.restype = ctypes.c_long
                p.PdhCollectQueryData.argtypes = [ctypes.c_void_p]
                p.PdhCollectQueryData.restype = ctypes.c_long
                p.PdhGetFormattedCounterValue.argtypes = [
                    ctypes.c_void_p, ctypes.c_ulong,
                    ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p]
                p.PdhGetFormattedCounterValue.restype = ctypes.c_long
            except Exception as _dx:
                DIAG.q("WinPerfCounters._init#0", _dx)

            hq = ctypes.c_void_p()
            if p.PdhOpenQueryW(None, 0, ctypes.byref(hq)) != 0:
                self.fail_reason = "PdhOpenQueryW failed"
                return

            eng = getattr(p, "PdhAddEnglishCounterW", None)

            def _add(path, handle):
                """언어 중립 우선, 실패 시 현지화 API 폴백. 0=성공."""
                if eng is not None:
                    r = eng(hq, path, 0, ctypes.byref(handle))
                    if r == 0:
                        return 0
                return p.PdhAddCounterW(hq, path, 0, ctypes.byref(handle))

            # ★★수정(대표님 PC 실측 반영)★★
            # 진단 스크립트 결과, 등록은 전부 성공하는데 값이 이렇게 나왔다:
            #   Processor Queue Length      0.00 / 0.00
            #   Current Disk Queue Length   0.00 / 0.00
            #   Page Faults/sec         79,311 / 45,136  (1.5초에 -43%)
            #   Context Switches/sec    31,272 / 12,597  (1.5초에 -60%)
            #
            # 세 가지가 전부 '점수 재료로 쓸 수 없는 값'이다.
            #  · Processor Queue Length 는 ready 큐의 '순간' 표본이다.
            #    32스레드 CPU 가 포화되기 전에는 사실상 항상 0 이라
            #    responsive 컴포넌트(0.18)의 델타가 영구히 0 이었다.
            #  · Current Disk Queue Length 도 순간값이고 NVMe 에선 거의
            #    항상 0 → disk 컴포넌트(0.12) 영구 0.
            #  · Page Faults/sec 는 '소프트 폴트'(이미 RAM 에 있는 페이지)
            #    까지 센다. 유휴 상태에서도 8만이 나오고 1.5초에 43% 씩
            #    요동친다. 실제 스래싱과 무관하며 클램프에 항상 포화돼
            #    ±3.3점의 순수 노이즈만 주입했다.
            #
            # 교체안:
            #  · 디스크    : % Idle Time (rate 카운터, 실제로 움직인다)
            #                → 100 - idle = 디스크 사용률
            #  · 스래싱    : Pages Input/sec = '하드' 폴트만. 디스크에서
            #                실제로 페이지를 읽어온 횟수다. 유휴 시 0 에
            #                가깝고 진짜 메모리 압박에서만 치솟는다.
            #  · 큐 길이   : 유지하되, 양쪽이 0 이면 '측정 불가'로 빼서
            #                가중치 재정규화가 처리하게 한다(아래 PIS).
            self._hc = ctypes.c_void_p()
            self._hd = ctypes.c_void_p()
            self._hpf = ctypes.c_void_p()
            self._hcs = ctypes.c_void_p()
            self._hdi = ctypes.c_void_p()
            self._hpi = ctypes.c_void_p()
            r1 = _add(r"\System\Processor Queue Length", self._hc)
            r2 = _add(r"\PhysicalDisk(_Total)\Current Disk Queue Length", self._hd)
            r3 = _add(r"\Memory\Page Faults/sec", self._hpf)
            r4 = _add(r"\System\Context Switches/sec", self._hcs)
            r5 = _add(r"\PhysicalDisk(_Total)\% Idle Time", self._hdi)
            r6 = _add(r"\Memory\Pages Input/sec", self._hpi)
            # ★수정★ 기존엔 r1/r2 중 하나만 실패해도 전부 포기했다.
            # 이제 성공한 카운터만 개별적으로 살린다(부분 실패 허용).
            self._has_cq = (r1 == 0)
            self._has_dq = (r2 == 0)
            self._has_pf = (r3 == 0)
            self._has_cs = (r4 == 0)
            self._has_di = (r5 == 0)
            self._has_pi = (r6 == 0)
            if not any((self._has_cq, self._has_dq, self._has_pf,
                        self._has_cs, self._has_di, self._has_pi)):
                self.fail_reason = "no counter registered (0x%08X)" % (r1 & 0xFFFFFFFF)
                p.PdhCloseQuery(hq); return
            if not (self._has_cq and self._has_dq):
                self.fail_reason = "partial (cq=%d dq=%d pf=%d cs=%d)" % (
                    self._has_cq, self._has_dq, self._has_pf, self._has_cs)
            self._pdh = p
            self._hq = hq
            self._ok = True
        except Exception as e:
            self.fail_reason = "exception: %s" % e

    def _loop(self):
        while not self._stop.is_set():
            try:
                self._pdh.PdhCollectQueryData(self._hq)
                cq = dq = pf = cs = 0.0
                if self._has_cq:
                    vc = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hc, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vc)) == 0:
                        cq = max(0.0, vc.doubleValue)
                if self._has_dq:
                    vd = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hd, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vd)) == 0:
                        dq = max(0.0, vd.doubleValue)
                if self._has_pf:
                    vpf = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hpf, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vpf)) == 0:
                        pf = max(0.0, vpf.doubleValue)
                if self._has_cs:
                    vcs = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hcs, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vcs)) == 0:
                        cs = max(0.0, vcs.doubleValue)
                di = pi = 0.0
                if self._has_di:
                    vdi = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hdi, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vdi)) == 0:
                        di = max(0.0, min(100.0, 100.0 - vdi.doubleValue))
                if self._has_pi:
                    vpi = self._CV()
                    if self._pdh.PdhGetFormattedCounterValue(
                            self._hpi, self.PDH_FMT_DOUBLE, None,
                            ctypes.byref(vpi)) == 0:
                        pi = max(0.0, vpi.doubleValue)
                with self._lk:
                    self._cpu_q = self._smooth("cq", cq)
                    self._disk_q = self._smooth("dq", dq)
                    self._pf = self._smooth("pf", pf)
                    self._cs = self._smooth("cs", cs)
                    self._disk_busy = self._smooth("di", di)
                    self._hard_faults = self._smooth("pi", pi)
            except Exception as _dx:
                DIAG.q("WinPerfCounters._loop#0", _dx)
            self._stop.wait(1.5)

    def _smooth(self, key, v):
        """최근 SMOOTH_N 표본의 중앙값. 락 안에서만 호출한다."""
        h = self._hist.setdefault(key, [])
        h.append(v)
        if len(h) > self.SMOOTH_N:
            h.pop(0)
        s = sorted(h); n = len(s); m = n // 2
        return float(s[m]) if n % 2 else (s[m - 1] + s[m]) / 2.0

    @property
    def disk_busy(self):
        """디스크 사용률 %(= 100 - % Idle Time). Current Disk Queue Length
        와 달리 NVMe 에서도 실제로 움직인다."""
        with self._lk: return self._disk_busy

    @property
    def hard_faults(self):
        """Pages Input/sec — 디스크에서 실제로 읽어온 페이지 수.
        Page Faults/sec 와 달리 소프트 폴트를 세지 않는다."""
        with self._lk: return self._hard_faults

    @property
    def cpu_queue(self):
        with self._lk: return self._cpu_q
    @property
    def disk_queue(self):
        with self._lk: return self._disk_q
    @property
    def page_faults(self):
        with self._lk: return self._pf
    @property
    def ctx_switches(self):
        with self._lk: return self._cs

    @property
    def ok(self):
        """PDH 수집이 실제로 살아있는가. False 면 큐/폴트 지표는 전부 0 이며
        PIS 의 responsive/disk/thrashing 컴포넌트를 신뢰하면 안 된다."""
        return self._ok


# ----------------------------------------------------------------------------
# THERMAL MONITOR — CPU 온도 관측 (읽기 전용)
# ----------------------------------------------------------------------------
# ★이 클래스가 하지 않는 것★
#   팬 속도 제어 · 전력 한계(PL1/PL2·TGP) 조정 · 언더볼팅 · 커널 드라이버
#   설치. 전부 벤더 전용 영역이라 표준 API 가 없고, 잘못된 EC 명령은
#   팬을 멈추거나 기기를 상하게 한다. "소프트웨어로 되돌릴 수 있는 것만
#   건드린다"는 이 파일의 원칙이 여기서도 그대로다. 온도는 읽기만 한다.
#
# ★측정 경로★
#   PDH 카운터 \Thermal Zone Information(*)\Temperature.
#   ACPI 펌웨어가 노출한 열 구역(Thermal Zone)을 Windows 가 중계하는
#   값이라 추가 설치도, 관리자 권한도, 드라이버도 필요 없다.
#   WinPerfCounters 와 같은 PDH 인프라를 재사용한다.
#
#   ※한계(중요) — 이 값을 아예 안 채우는 PC 가 많다. 특히 게이밍
#     노트북은 열 구역을 안 내보내거나, 내보내도 CPU 패키지가 아니라
#     섀시 쪽 온도를 준다. 그래서 '못 읽음'을 고장이 아니라 정상 상태의
#     하나로 취급한다. ok=False 면 UI 는 그 항목을 통째로 숨긴다.
#     0도나 "알 수 없음"을 점수·화면에 끼워 넣지 않는다 —— PIS 가 상시 0
#     인 카운터를 '측정 불가'로 빼는 것과 같은 판단이다.
#
# ★단위★ 이 카운터는 켈빈(K)으로 나온다. 1/10 K 로 주는 펌웨어도 있다.
#   섭씨로 바꾼 뒤 상식 범위(5~125℃) 밖이면 그 표본은 버린다.
#
# ★고정값 함정★ 등록은 성공하는데 값이 영원히 같은 PC 가 있다(펌웨어가
#   상수를 박아둔 경우). STATIC_N 회 연속 완전 동일하면 측정 불가로
#   내린다. 움직이지 않는 숫자는 온도가 아니라 장식이다.
# ----------------------------------------------------------------------------
class ThermalMonitor:
    PDH_FMT_DOUBLE = 0x00000200
    ENG_OBJECT = "Thermal Zone Information"
    ENG_COUNTER = "Temperature"
    SMOOTH_N = 5        # WinPerfCounters 와 같은 중앙값 평활
    HIST_N = 60         # 추이 보관(약 4분)
    POLL_S = 4.0
    SANE_MIN_C = 5.0
    SANE_MAX_C = 125.0
    STATIC_N = 40       # 연속 동일값 허용 한도(약 2.7분)

    class _CV(ctypes.Structure):
        _fields_ = [("CStatus", ctypes.c_ulong),
                    ("doubleValue", ctypes.c_double)]

    def __init__(self):
        self._lk = threading.Lock()
        self._stop = threading.Event()
        self._val = None          # 평활된 섭씨 (float | None)
        self._smooth_buf = []
        self._hist = deque(maxlen=self.HIST_N)
        self._zones = []          # [(zone_name, handle)]
        self._static_run = 0
        self._last_raw = None
        self._peak = None
        self._ok = False
        self.fail_reason = ""
        self.source = ""
        self._pdh = None
        self._hq = None
        self._init_source()
        if self._ok:
            threading.Thread(target=self._poll_loop, daemon=True).start()

    # ── 초기화 ───────────────────────────────────────────────────────
    def _init_source(self):
        try:
            p = ctypes.windll.pdh
        except Exception:
            self.fail_reason = "pdh.dll load failed"
            return
        hq = None
        try:
            self._declare(p)
            hq = ctypes.c_void_p()
            if p.PdhOpenQueryW(None, 0, ctypes.byref(hq)) != 0:
                self.fail_reason = "PdhOpenQueryW failed"
                return
            src = "english"
            paths = self._expand(p, "\\%s(*)\\%s" % (self.ENG_OBJECT,
                                                     self.ENG_COUNTER))
            if not paths:
                loc = self._localized_path()
                if loc:
                    paths = self._expand(p, loc)
                    src = "localized"
            if not paths:
                self.fail_reason = "no thermal zone exposed by firmware"
                return
            zones = []
            for path in paths:
                h = ctypes.c_void_p()
                try:
                    if p.PdhAddCounterW(hq, path, 0, ctypes.byref(h)) == 0:
                        zones.append((self._zone_name(path), h))
                except Exception as _dx:
                    DIAG.q("ThermalMonitor._init_source#0", _dx)
            if not zones:
                self.fail_reason = "PdhAddCounterW failed for every zone"
                return
            self._pdh = p
            self._hq = hq
            self._zones = zones
            # 등록만 되고 값이 안 나오는 PC 가 있다. 그건 '측정 가능'이
            # 아니다 — 첫 표본이 상식 범위에 들어올 때만 ok 로 올린다.
            try:
                p.PdhCollectQueryData(hq)
                time.sleep(0.05)
            except Exception as _dx:
                DIAG.q("ThermalMonitor._init_source#1", _dx)
            first = self._read_once()
            if first is None:
                self.fail_reason = "counter present but value out of range"
                self._pdh = None
                self._zones = []
                return
            self.source = "PDH Thermal Zone (%s, %d zone%s)" % (
                src, len(zones), "" if len(zones) == 1 else "s")
            self._push(first)
            self._ok = True
        except Exception as e:
            self.fail_reason = "exception: %s" % e
        finally:
            if not self._ok and hq is not None:
                try: p.PdhCloseQuery(hq)
                except Exception as _dx: DIAG.q("ThermalMonitor._init_source#2", _dx)

    @staticmethod
    def _declare(p):
        """x64 에서 핸들이 32비트로 잘리는 것을 막는다(파일 전체 방침)."""
        try:
            p.PdhOpenQueryW.argtypes = [wintypes.LPCWSTR, ctypes.c_size_t,
                                        ctypes.POINTER(ctypes.c_void_p)]
            p.PdhOpenQueryW.restype = ctypes.c_long
            p.PdhAddCounterW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR,
                                         ctypes.c_size_t,
                                         ctypes.POINTER(ctypes.c_void_p)]
            p.PdhAddCounterW.restype = ctypes.c_long
            p.PdhCollectQueryData.argtypes = [ctypes.c_void_p]
            p.PdhCollectQueryData.restype = ctypes.c_long
            p.PdhGetFormattedCounterValue.argtypes = [
                ctypes.c_void_p, ctypes.c_ulong,
                ctypes.POINTER(ctypes.c_ulong), ctypes.c_void_p]
            p.PdhGetFormattedCounterValue.restype = ctypes.c_long
            p.PdhCloseQuery.argtypes = [ctypes.c_void_p]
            p.PdhCloseQuery.restype = ctypes.c_long
            f = getattr(p, "PdhExpandWildCardPathW", None)
            if f is not None:
                f.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR,
                              ctypes.c_void_p,
                              ctypes.POINTER(ctypes.c_ulong),
                              ctypes.c_ulong]
                f.restype = ctypes.c_long
        except Exception as _dx:
            DIAG.q("ThermalMonitor._declare#0", _dx)

    def _expand(self, p, wildcard):
        """와일드카드 경로를 실제 열 구역 경로 목록으로 펼친다.

        ※PdhAddCounter 는 와일드카드를 못 받는다. 그래서 먼저 펼치고
          구역별로 하나씩 등록한다(구역이 여러 개인 노트북이 흔하다).
        """
        fn = getattr(p, "PdhExpandWildCardPathW", None)
        if fn is None:
            return []
        try:
            need = ctypes.c_ulong(0)
            fn(None, wildcard, None, ctypes.byref(need), 0)
            if not need.value or need.value > 1 << 20:
                return []
            buf = ctypes.create_unicode_buffer(need.value)
            if fn(None, wildcard, buf, ctypes.byref(need), 0) != 0:
                return []
            raw = buf[:need.value]
            return [s for s in raw.split("\x00") if s]
        except Exception:
            return []

    def _localized_path(self):
        """영문 카운터 이름이 안 먹는 Windows(한국어판 등)를 위한 폴백.

        Perflib 의 인덱스 대응표(009=영문 / CurrentLanguage=현지어)로
        현지화된 개체·카운터 이름을 찾아 경로를 만든다. PdhAddEnglishCounter
        가 내부적으로 하는 일과 같다 — 다만 PdhExpandWildCardPath 에는
        English 판 API 가 없어서 직접 해야 한다.
        """
        try:
            import winreg
        except Exception:
            return ""
        base = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Perflib"

        def _multi(sub):
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                    base + sub) as k:
                    v, _ = winreg.QueryValueEx(k, "Counter")
                return list(v or [])
            except Exception:
                return []

        eng, loc = _multi(r"\009"), _multi(r"\CurrentLanguage")
        if not eng or not loc:
            return ""
        name_to_idx = {}
        for i in range(0, len(eng) - 1, 2):
            name_to_idx[eng[i + 1]] = eng[i]
        idx_to_name = {}
        for i in range(0, len(loc) - 1, 2):
            idx_to_name[loc[i]] = loc[i + 1]
        o = idx_to_name.get(name_to_idx.get(self.ENG_OBJECT, ""), "")
        c = idx_to_name.get(name_to_idx.get(self.ENG_COUNTER, ""), "")
        if not o or not c:
            return ""
        return "\\%s(*)\\%s" % (o, c)

    @staticmethod
    def _zone_name(path):
        try:
            return path.split("(", 1)[1].split(")", 1)[0]
        except Exception:
            return path

    @classmethod
    def _to_celsius(cls, raw):
        """켈빈 / 1/10 켈빈 / 섭씨를 구분해 섭씨로. 이상하면 None."""
        try:
            raw = float(raw)
        except Exception:
            return None
        if raw != raw or raw in (float("inf"), float("-inf")):
            return None          # NaN/inf — 카운터가 깨진 경우
        if raw <= 0:
            return None
        if raw > 1000.0:
            c = raw / 10.0 - 273.15
        elif raw > 200.0:
            c = raw - 273.15
        else:
            c = raw
        if c < cls.SANE_MIN_C or c > cls.SANE_MAX_C:
            return None
        return c

    # ── 수집 ─────────────────────────────────────────────────────────
    def _read_once(self):
        p, hq = self._pdh, self._hq
        if not p or not hq:
            return None
        try:
            p.PdhCollectQueryData(hq)
        except Exception:
            return None
        best = None
        for _name, h in self._zones:
            v = self._CV()
            try:
                if p.PdhGetFormattedCounterValue(
                        h, self.PDH_FMT_DOUBLE, None,
                        ctypes.byref(v)) != 0:
                    continue
            except Exception:
                continue
            c = self._to_celsius(v.doubleValue)
            if c is None:
                continue
            if best is None or c > best:
                best = c        # 구역이 여러 개면 가장 뜨거운 쪽을 쓴다
        return best

    def _poll_loop(self):
        while not self._stop.is_set():
            try:
                c = self._read_once()
                if c is None:
                    with self._lk:
                        self._val = None
                else:
                    self._push(c)
            except Exception as _dx:
                DIAG.q("ThermalMonitor._poll_loop#0", _dx)
            self._stop.wait(self.POLL_S)

    def _push(self, c):
        with self._lk:
            if self._last_raw is not None and abs(c - self._last_raw) < 1e-9:
                self._static_run += 1
            else:
                self._static_run = 1      # 이 표본부터 새 연속 구간
            self._last_raw = c
            if self._static_run >= self.STATIC_N:
                # 움직이지 않는 숫자는 온도가 아니다. 꾸며서 보여주느니
                # 측정 불가로 내린다.
                self._ok = False
                self.fail_reason = "constant %.1fC for %d samples" % (
                    c, self._static_run)
                self._val = None
                return
            b = self._smooth_buf
            b.append(c)
            if len(b) > self.SMOOTH_N:
                b.pop(0)
            s = sorted(b)
            n = len(s)
            m = n // 2
            self._val = float(s[m]) if n % 2 else (s[m - 1] + s[m]) / 2.0
            self._hist.append((time.time(), self._val))
            if self._peak is None or self._val > self._peak:
                self._peak = self._val

    # ── 노출 ─────────────────────────────────────────────────────────
    @property
    def cpu_temp_c(self):
        """섭씨 온도(평활값) 또는 None. None = 지금 이 PC 에서 못 읽음."""
        with self._lk:
            return self._val

    @property
    def ok(self):
        """온도를 실제로 읽고 있는가. False 면 화면에서 항목 자체를 숨긴다."""
        return self._ok

    @property
    def peak_c(self):
        with self._lk:
            return self._peak

    def history(self):
        with self._lk:
            return list(self._hist)

    def zone_count(self):
        return len(self._zones)

    def stop(self):
        self._stop.set()
        p, hq = self._pdh, self._hq
        self._pdh = None
        try:
            if p and hq:
                p.PdhCloseQuery(hq)
        except Exception as _dx:
            DIAG.q("ThermalMonitor.stop#0", _dx)

# ----------------------------------------------------------------------------
# ECOQOS LEDGER — EcoQoS 를 건 프로세스를 '한 곳에서만' 장부에 적는다
# ----------------------------------------------------------------------------
# ★실사용 신고: "EcoQoS 가 풀리지 않는다" — 원인 4종을 여기서 전부 잡는다★
#
#  (1) ★장부가 두 개였다★
#      LatencyOptimizer._ecoqos_pids 와 CoreMode._ecoqos_pids 가 각각
#      따로 있었는데, 알트탭 때 포그라운드 트리를 풀어주는
#      CoreMode._release_fg_tree 는 자기 장부만 봤다. Auto 루프
#      (LatencyOptimizer.apply_ecoqos)가 걸어둔 크롬 렌더러·디스코드
#      헬퍼·런처는 사용자가 그 앱으로 전환해도 영영 저클럭에 묶였다.
#      → 장부를 이 클래스 하나로 합친다. 두 클래스는 같은 객체를 본다.
#
#  (2) ★해제 방식이 틀렸다★
#      해제를 ControlMask=1 / StateMask=0 으로 했다. 이건 '기본값 복귀'가
#      아니라 "이 프로세스는 앞으로 절대 절전하지 마라"는 영구 opt-out
#      이다. Windows 가 알아서 절전시켰어야 할 프로세스까지 고성능에
#      묶여 전력과 발열이 오히려 늘고, 작업 관리자 '전원 조절' 열에도
#      흔적이 남는다. 진짜 복귀는 ControlMask=0 / StateMask=0 이다.
#
#  (3) ★실패해도 장부에서 지웠다★
#      핸들을 못 열거나(보호 프로세스) API 가 실패해도 discard 했다.
#      한 번 실패하면 그 프로세스는 영원히 풀 기회를 잃었다.
#      → 성공을 '확인'했을 때만 지운다(GetProcessInformation 재조회).
#        실패는 장부에 남겨 다음 사이클에 다시 시도한다.
#
#  (4) ★크래시·강제 종료면 해제 코드가 아예 안 돈다★
#      EcoQoS 는 대상 프로세스가 살아있는 한 남는다. 며칠째 켜둔
#      explorer·디스코드가 계속 느린 채로 남는다는 뜻이다.
#      → 장부를 디스크에 적고(원자적 교체), 다음 실행 때 살아있는
#        프로세스를 전부 풀어준다. StartupManager 백업과 같은 방식이다.
#
# ★pid 재사용 방어★ pid 는 재사용된다. create_time 을 함께 적고 해제
#   직전에 같은 프로세스인지 확인한다. 아니면 엉뚱한 새 프로세스의
#   전원 설정을 건드린다.
#
# 이 객체는 set 처럼 동작한다(in / len / iter / add / discard / clear /
# &=). 기존 호출부를 그대로 둔 채 장부만 하나로 합치기 위해서다.
# ----------------------------------------------------------------------------
class EcoQoSLedger:
    MAX_TRACK = 400          # 장부 상한(이 이상은 죽은 pid 부터 정리)
    MAX_FAIL = 8             # 이만큼 연속 실패하면 포기(무한 재시도 방지)
    SAVE_MIN_S = 8.0         # 디스크 기록 최소 간격

    class _PTS(ctypes.Structure):
        _fields_ = [("Version", ctypes.c_ulong),
                    ("ControlMask", ctypes.c_ulong),
                    ("StateMask", ctypes.c_ulong)]

    def __init__(self):
        self._lk = threading.RLock()
        self._d = {}                 # pid -> [name, create_time, fail_count]
        self._last_save = 0.0
        self._dirty = False
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "ecoqos_pending.json"

    # ── Win32 ────────────────────────────────────────────────────────
    def _set(self, pid, on):
        """on=True: EcoQoS 켜기 / False: '시스템 관리'로 복귀."""
        try:
            h = _open_proc(pid, ACC_SET_PRIORITY)
            if not h:
                return False
            st = self._PTS()
            st.Version = 1
            if on:
                st.ControlMask = 0x1     # EXECUTION_SPEED
                st.StateMask = 0x1
            else:
                # ★기본값 복귀★ 둘 다 0 이어야 한다. ControlMask=1,
                # StateMask=0 은 '영구 opt-out' 이지 복귀가 아니다.
                st.ControlMask = 0x0
                st.StateMask = 0x0
            r = kernel32.SetProcessInformation(h, 4, ctypes.byref(st),
                                               ctypes.sizeof(st))
            _close(h)
            return bool(r)
        except Exception:
            return False

    def _query(self, pid):
        """지금 EcoQoS 가 걸려 있는가. True/False, 조회 불가면 None."""
        try:
            fn = getattr(kernel32, "GetProcessInformation", None)
            if fn is None:
                return None
            h = _open_proc(pid, ACC_SET_PRIORITY)
            if not h:
                return None
            st = self._PTS()
            st.Version = 1
            r = fn(h, 4, ctypes.byref(st), ctypes.sizeof(st))
            _close(h)
            if not r:
                return None
            return bool(st.ControlMask & 0x1) and bool(st.StateMask & 0x1)
        except Exception:
            return None

    @staticmethod
    def _ct(pid):
        try:
            return round(float(psutil.Process(pid).create_time()), 2)
        except Exception:
            return 0.0

    def _same_proc(self, pid, ct):
        """pid 재사용 판별. 살아있고 생성 시각이 같으면 같은 프로세스."""
        try:
            if not psutil.pid_exists(pid):
                return False
            if not ct:
                return True
            return abs(self._ct(pid) - ct) < 1.0
        except Exception:
            return False

    # ── 장부 ─────────────────────────────────────────────────────────
    def apply(self, pid, name=None, ct=None):
        """EcoQoS 적용 + 장부 기록. 성공 여부를 돌려준다."""
        if not pid or pid == SELF_PID:
            return False
        if not self._set(pid, True):
            return False
        with self._lk:
            if pid not in self._d:
                self._d[pid] = [name or "", ct if ct is not None else self._ct(pid), 0]
            self._dirty = True
            if len(self._d) > self.MAX_TRACK:
                self._gc_locked()
        self._save()
        return True

    def release(self, pid):
        """기본값으로 복귀. ★성공을 확인했을 때만★ 장부에서 지운다."""
        with self._lk:
            ent = self._d.get(pid)
        if ent is None:
            return self._set(pid, False)
        if not self._same_proc(pid, ent[1]):
            self._forget(pid)          # 죽었으면 EcoQoS 도 같이 사라졌다
            return True
        ok = self._set(pid, False)
        if ok and self._query(pid) is not True:
            self._forget(pid)
            return True
        with self._lk:
            ent[2] += 1
            if ent[2] >= self.MAX_FAIL:
                self._d.pop(pid, None)
                self._dirty = True
        return False

    def release_pids(self, pids):
        n = 0
        for pid in list(pids):
            try:
                if self.release(pid):
                    n += 1
            except Exception as _dx:
                DIAG.q("EcoQoSLedger.release_pids#0", _dx)
        self._save(force=True)
        return n

    def release_all(self):
        with self._lk:
            pids = list(self._d.keys())
        n = self.release_pids(pids)
        self._save(force=True)
        return n

    def _forget(self, pid):
        with self._lk:
            if self._d.pop(pid, None) is not None:
                self._dirty = True

    def _gc_locked(self):
        for pid in [p for p in self._d if not psutil.pid_exists(p)]:
            self._d.pop(pid, None)

    # ── 디스크(크래시 대비) ──────────────────────────────────────────
    def _save(self, force=False):
        now = time.time()
        with self._lk:
            if not force and (not self._dirty or
                              now - self._last_save < self.SAVE_MIN_S):
                return
            data = {"pids": [[p, v[0], v[1]] for p, v in self._d.items()]}
            self._dirty = False
            self._last_save = now
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            if not data["pids"]:
                if self._path.exists():
                    self._path.unlink()
                return
            tmp = self._path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f)
            os.replace(str(tmp), str(self._path))
        except Exception as _dx:
            DIAG.q("EcoQoSLedger._save#0", _dx)

    def sweep_startup(self):
        """지난 실행이 비정상 종료됐다면 남은 EcoQoS 를 풀고 시작한다."""
        n = 0
        try:
            if not self._path.exists():
                return 0
            with open(self._path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for row in (data.get("pids") or []):
                try:
                    pid = int(row[0]); ct = float(row[2]) if len(row) > 2 else 0.0
                except Exception:
                    continue
                if pid == SELF_PID or not self._same_proc(pid, ct):
                    continue
                if self._set(pid, False):
                    n += 1
        except Exception as _dx:
            DIAG.q("EcoQoSLedger.sweep_startup#0", _dx)
        try:
            if self._path.exists():
                self._path.unlink()
        except Exception as _dx:
            DIAG.q("EcoQoSLedger.sweep_startup#1", _dx)
        return n

    # ── set 처럼 쓰기 위한 최소 인터페이스 ───────────────────────────
    def __contains__(self, pid):
        with self._lk: return pid in self._d
    def __len__(self):
        with self._lk: return len(self._d)
    def __iter__(self):
        with self._lk: return iter(list(self._d.keys()))
    def __iand__(self, other):
        with self._lk:
            for pid in [p for p in self._d if p not in other]:
                self._d.pop(pid, None)
            self._dirty = True
        return self
    def add(self, pid):
        with self._lk:
            if pid not in self._d:
                self._d[pid] = ["", self._ct(pid), 0]
                self._dirty = True
    def discard(self, pid):
        self._forget(pid)
    def clear(self):
        with self._lk:
            self._d.clear(); self._dirty = True
        self._save(force=True)


ECO = EcoQoSLedger()


# ----------------------------------------------------------------------------
# THERMAL GOVERNOR — 온도가 높으면 CPU 최대 속도를 스스로 낮췄다가 되돌린다
# ----------------------------------------------------------------------------
# ★무엇을 건드리는가★
#   전원 계획의 '최대 프로세서 상태'(PROCTHROTTLEMAX) 하나뿐이다.
#   powercfg 로 바꾸는 문서화된 설정이고, 값을 되돌리면 원래대로 온다.
#   팬·전력 한계(PL1/PL2)·전압은 여전히 건드리지 않는다 — 벤더 전용
#   영역이고 되돌릴 보장이 없다.
#
# ★이게 실제로 온도를 낮추는 이유★
#   온도는 대부분 부스트 구간(높은 클럭 = 높은 전압)에서 만들어진다.
#   최대 상태를 90%/80% 로 내리면 그 구간을 안 쓴다. 대신 성능이 실제로
#   줄어든다 — 그래서 기본값이 '꺼짐'이고, 켜져 있는 동안 화면에
#   "제한 중"이라고 계속 표시한다. 몰래 깎지 않는다.
#
# ★단계와 히스테리시스★
#   100 → 90 → 80 → 70 %. 기준을 넘으면 한 단계 내리고, 계속 뜨거우면
#   STEP_UP_HOLD_S 뒤에 한 단계 더. 식을 때는 기준보다 HYST_C 만큼 더
#   내려간 상태가 COOL_HOLD_S 동안 유지돼야 한 단계 올린다. 이 여유가
#   없으면 기준선 근처에서 초당 몇 번씩 오르내리며(채터링) 오히려
#   버벅인다.
#
# ★안전장치★
#   · 온도를 못 읽게 되면(센서 사라짐 등) 60초 안에 무조건 100% 복귀.
#     죽은 센서를 근거로 CPU 를 묶어두는 게 최악이다.
#   · 원래 값은 캡을 걸기 '전에' %APPDATA%/OMEGA_X/thermal_cap.json 에
#     적는다. 앱이 크래시해도 다음 실행에서 recover_startup() 이 복원한다.
#     (이게 없으면 크래시 한 번에 PC 가 70% 로 영구히 묶인다)
#   · guard.record 로 앱 종료 롤백에도 등록한다.
# ----------------------------------------------------------------------------
class ThermalGovernor:
    SUB_PROCESSOR = "54533251-82be-4824-96c1-47b60b740d00"
    PROCTHROTTLEMAX = "bc5038f7-23e0-4960-96da-33abaf5935ec"
    TIERS = (100, 90, 80, 70)
    STEP_UP_HOLD_S = 20.0     # 한 단계 더 내리기 전 유지 시간
    COOL_HOLD_S = 45.0        # 한 단계 올리기 전 식은 상태 유지 시간
    HYST_C = 6.0              # 복귀 여유(채터링 방지)
    LOST_SENSOR_S = 60.0      # 온도를 이만큼 못 읽으면 무조건 복귀
    POLL_S = 5.0

    def __init__(self, thermal, guard=None, log_fn=None):
        self.thermal = thermal
        self.guard = guard
        self.log_fn = log_fn
        self.enabled = False
        self.tier = 0
        self.fail_reason = ""
        self._since = 0.0
        self._cool_since = None
        self._lost_since = None
        self._orig = None          # (ac, dc) — 사용자의 원래 최대 상태
        self._recorded = False
        self._stop = threading.Event()
        self._thr = None
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "thermal_cap.json"

    # ── powercfg ─────────────────────────────────────────────────────
    def _query_orig(self):
        """현재 '최대 프로세서 상태'(AC/DC)를 읽는다. 실패하면 None."""
        import re
        try:
            r = subprocess_run(["powercfg", "/q", "SCHEME_CURRENT",
                                self.SUB_PROCESSOR, self.PROCTHROTTLEMAX],
                               timeout=6)
            if not r or r.returncode != 0 or not r.stdout:
                return None
            ac = dc = None
            for ln in r.stdout.splitlines():
                m = re.search(r"0x([0-9a-fA-F]{8})", ln)
                if not m:
                    continue
                # 로케일과 무관하게 'AC'/'DC' 토큰은 그대로 나온다.
                if "AC" in ln and ac is None:
                    ac = int(m.group(1), 16)
                elif "DC" in ln and dc is None:
                    dc = int(m.group(1), 16)
            if ac is None and dc is None:
                return None
            ac = 100 if ac is None else max(1, min(100, ac))
            dc = ac if dc is None else max(1, min(100, dc))
            return (ac, dc)
        except Exception:
            return None

    def _write_index(self, ac, dc):
        try:
            a = subprocess_run(["powercfg", "/setacvalueindex", "SCHEME_CURRENT",
                                self.SUB_PROCESSOR, self.PROCTHROTTLEMAX,
                                str(int(ac))], timeout=6)
            b = subprocess_run(["powercfg", "/setdcvalueindex", "SCHEME_CURRENT",
                                self.SUB_PROCESSOR, self.PROCTHROTTLEMAX,
                                str(int(dc))], timeout=6)
            subprocess_run(["powercfg", "/setactive", "SCHEME_CURRENT"], timeout=6)
            return bool(a and a.returncode == 0) or bool(b and b.returncode == 0)
        except Exception:
            return False

    def probe(self):
        """이 PC 에서 최대 프로세서 상태를 바꿀 수 있는지 확인만 한다."""
        o = self._query_orig()
        if o is None:
            self.fail_reason = "powercfg query failed (권한/정책)"
            return False
        self._orig = o
        return True

    # ── 상태 저장/복원 ───────────────────────────────────────────────
    def _persist_orig(self):
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            tmp = self._path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump({"ac": self._orig[0], "dc": self._orig[1]}, f)
            os.replace(str(tmp), str(self._path))
        except Exception as _dx:
            DIAG.q("ThermalGovernor._persist_orig#0", _dx)

    def _clear_persist(self):
        try:
            if self._path.exists():
                self._path.unlink()
        except Exception as _dx:
            DIAG.q("ThermalGovernor._clear_persist#0", _dx)

    @classmethod
    def recover_startup(cls):
        """지난 실행이 캡을 건 채로 죽었다면 원래 값으로 되돌리고 시작."""
        try:
            d = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
            p = d / "thermal_cap.json"
            if not p.exists():
                return False
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            ac = int(data.get("ac", 100)); dc = int(data.get("dc", 100))
            g = cls.__new__(cls)
            g.SUB_PROCESSOR = cls.SUB_PROCESSOR
            g._write_index = cls._write_index.__get__(g, cls)
            g._write_index(ac, dc)
            p.unlink()
            return True
        except Exception:
            return False

    # ── 캡 적용 ──────────────────────────────────────────────────────
    def _apply_tier(self, tier):
        tier = max(0, min(len(self.TIERS) - 1, tier))
        if tier == self.tier:
            return False
        if self._orig is None and not self.probe():
            return False
        if tier > 0 and not self._recorded:
            # ★캡을 걸기 전에★ 원래 값을 디스크와 guard 양쪽에 남긴다.
            self._persist_orig()
            self._recorded = True
            if self.guard is not None:
                try:
                    self.guard.record("thermal_cap", "system", self.restore)
                except Exception as _dx:
                    DIAG.q("ThermalGovernor._apply_tier#0", _dx)
        pct = self.TIERS[tier]
        if tier == 0:
            ok = self._write_index(self._orig[0], self._orig[1])
            if ok:
                self._clear_persist()
                self._recorded = False
        else:
            base_ac, base_dc = self._orig
            ok = self._write_index(min(base_ac, pct), min(base_dc, pct))
        if not ok:
            self.fail_reason = "powercfg set failed"
            return False
        self.tier = tier
        self._since = time.time()
        if self.log_fn:
            try:
                self.log_fn(t("thermal_cap_restored") if tier == 0
                            else t("thermal_capped", pct=pct))
            except Exception as _dx:
                DIAG.q("ThermalGovernor._apply_tier#1", _dx)
        return True

    def restore(self):
        """원래 최대 프로세서 상태로 되돌린다(멱등)."""
        if self._orig is None:
            self._clear_persist()
            return False
        ok = self._write_index(self._orig[0], self._orig[1])
        self.tier = 0
        self._cool_since = None
        self._clear_persist()
        self._recorded = False
        return ok

    # ── 판단 로직(순수 함수 — 스텁으로 검증 가능) ────────────────────
    def decide(self, temp_c, now, threshold):
        """다음 단계 번호를 돌려준다. 부작용 없음."""
        if temp_c is None:
            # 센서를 잃었다. 죽은 센서를 근거로 CPU 를 묶어두지 않는다.
            if self._lost_since is None:
                self._lost_since = now
            if self.tier > 0 and (now - self._lost_since) >= self.LOST_SENSOR_S:
                return 0
            return self.tier
        self._lost_since = None
        if temp_c >= threshold:
            self._cool_since = None
            if self.tier == 0:
                return 1
            if (now - self._since) >= self.STEP_UP_HOLD_S and \
                    temp_c >= threshold + 2.0:
                return min(self.tier + 1, len(self.TIERS) - 1)
            return self.tier
        if temp_c <= threshold - self.HYST_C:
            if self._cool_since is None:
                self._cool_since = now
            elif (now - self._cool_since) >= self.COOL_HOLD_S and self.tier > 0:
                self._cool_since = now
                return self.tier - 1
            return self.tier
        # 기준선 바로 아래 — 유지(채터링 방지 구간)
        self._cool_since = None
        return self.tier

    def tick(self):
        temp = None
        try:
            temp = self.thermal.cpu_temp_c if self.thermal else None
        except Exception:
            temp = None
        want = self.decide(temp, time.time(), thermal_threshold())
        if want != self.tier:
            self._apply_tier(want)

    # ── 수명 ─────────────────────────────────────────────────────────
    def start(self):
        if self.enabled:
            return True
        if not (self.thermal and self.thermal.ok):
            self.fail_reason = "no temperature source"
            return False
        if self._orig is None and not self.probe():
            return False
        self.enabled = True
        self._stop.clear()
        self._since = time.time()
        self._thr = threading.Thread(target=self._loop, daemon=True)
        self._thr.start()
        return True

    def _loop(self):
        while not self._stop.is_set():
            try:
                self.tick()
            except Exception as _dx:
                DIAG.q("ThermalGovernor._loop#0", _dx)
            self._stop.wait(self.POLL_S)

    def stop(self, restore=True):
        self.enabled = False
        self._stop.set()
        if restore and self.tier > 0:
            try:
                self.restore()
            except Exception as _dx:
                DIAG.q("ThermalGovernor.stop#0", _dx)

    def status_pct(self):
        return self.TIERS[self.tier] if self.tier else 100


def _cpu_name():
    try:
        import winreg
        with winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE,
                r"HARDWARE\DESCRIPTION\System\CentralProcessor\0") as k:
            v, _ = winreg.QueryValueEx(k, "ProcessorNameString")
        return str(v)
    except Exception:
        return ""


def _is_laptop():
    try:
        return psutil.sensors_battery() is not None
    except Exception:
        return False


def auto_thermal_threshold():
    r"""개입 기준 온도를 추정한다.

    ★코어 수·스레드 수로는 온도 한계를 알 수 없다★
    같은 8코어 16스레드라도 노트북 Ryzen 은 설계상 95℃ 부근에서 계속
    돌고(그게 정상 동작이다), 데스크톱 칩은 80℃ 대에서 논다. 코어 수는
    '고성능인가'는 알려줘도 '몇 도가 위험한가'는 알려주지 않는다.
    실제로 필요한 값은 Tjmax 인데, 그건 모델별 상수라 사용자 모드에서
    읽을 방법이 없고 모델 표를 코드에 박으면 틀린 값이 반드시 섞인다.

    그래서 확실히 알 수 있는 것 두 가지만 쓴다.
      · 노트북인가(배터리 유무) — 노트북은 원래 높게 돌린다
      · 제조사(레지스트리 ProcessorNameString)
    이건 '추정'이고, 사용자가 설정에서 언제든 직접 정할 수 있다.
    """
    name = _cpu_name().lower()
    lap = _is_laptop()
    amd = ("amd" in name) or ("ryzen" in name)
    intel = "intel" in name or "core(tm)" in name
    if lap:
        if amd:
            return 92      # Ryzen 모바일: Tjmax 95~100, 90℃ 는 정상 운용
        if intel:
            return 93      # Intel 모바일: Tjmax 100
        return 92
    if amd:
        return 88          # 데스크톱 Ryzen: Tjmax 95
    if intel:
        return 90
    return 88


def thermal_threshold():
    """설정값이 있으면 그걸, 없으면(0=자동) 추정값."""
    try:
        v = int(SETTINGS.get("thermal_threshold_c", 0) or 0)
    except Exception:
        v = 0
    if 60 <= v <= 99:
        return float(v)
    return float(auto_thermal_threshold())

# ----------------------------------------------------------------------------
# GLOBAL PROCESS CACHE — single source of truth for ALL process_iter callers
# ----------------------------------------------------------------------------
# process_iter() is the #1 cost in this app. Originally 18 callsites each
# walked all ~500 processes independently. This singleton hands out a cached
# list (full attribute set the app uses anywhere) with a 3s TTL, and ALSO
# patches psutil.process_iter so any caller — including 3rd-party code paths
# we don't touch — transparently shares the cache.
# ----------------------------------------------------------------------------
class _GlobalProcCache:
    # ★주의★ 여기에 "ppid" 를 넣으면 안 된다.
    # psutil 의 윈도우 구현에서 Process.ppid() 는
    #     return ppid_map()[self.pid]
    # 이고 ppid_map 은 cext.ppid_map, 즉 CreateToolhelp32Snapshot 으로
    # 전체 프로세스를 훑는 함수다. 게다가 oneshot() 캐시 대상이 아니다.
    # 따라서 process_iter(["ppid", ...]) 는 프로세스 500개면 전체 스냅샷을
    # 500번 뜬다. 부모 정보는 ForegroundTracker 가 ppid_map() 을 직접
    # '한 번만' 호출해서 얻는다(_maps 참조).
    _FULL_ATTRS = ["pid", "name", "cpu_percent", "memory_percent",
                   "memory_info", "status", "num_threads"]
    # ★수정★ TTL 3.0s 는 코어 사이클(3~4초)과 거의 같아 사실상 매 사이클
    # 전체 프로세스 워크(속성 7개, 프로세스마다 핸들 오픈)를 다시 돌렸다.
    # 5.0s 로 올려 워크 빈도를 ~40% 줄인다. cpu_percent 델타 구간도 넓어져
    # 순간 튐이 줄고 판정이 안정된다.
    TTL = 5.0

    def __init__(self):
        self._lk = threading.Lock()
        self._t = 0.0
        self._procs = []          # list of psutil.Process (cached)
        self._info_cache = []     # list of info-dicts (cached)
        self._warmed = False
        self._refreshing = False  # 백그라운드 갱신 중복 방지(single-flight)

    def _refresh(self):
        # Walk processes ONCE with full attr set; populate both views.
        procs = []
        infos = []
        try:
            for p in _orig_process_iter(self._FULL_ATTRS):
                procs.append(p)
                try:
                    info = dict(p.info)
                    if info.get("name"):
                        infos.append(info)
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except Exception as _dx:
            DIAG.q("_GlobalProcCache._refresh#0", _dx)
        self._procs = procs
        self._info_cache = infos
        self._t = time.time()
        self._warmed = True

    def iter_procs(self, attrs=None, force=False):
        """Drop-in replacement for psutil.process_iter — returns cached
        psutil.Process objects whose `.info` already has the full attr set."""
        now = time.time()
        if force or (now - self._t) > self.TTL or not self._warmed:
            with self._lk:
                if force or (now - self._t) > self.TTL or not self._warmed:
                    self._refresh()
        return list(self._procs)

    def info_list(self, force=False):
        """Returns cached info-dicts — for code that just reads fields."""
        now = time.time()
        if force or (now - self._t) > self.TTL or not self._warmed:
            with self._lk:
                if force or (now - self._t) > self.TTL or not self._warmed:
                    self._refresh()
        return list(self._info_cache)

    def warm_async(self):
        """Kick off a non-blocking first walk so first real call is instant."""
        threading.Thread(target=self._refresh, daemon=True).start()

    # ── ★GUI 스레드 전용 논블로킹 경로★ ─────────────────────────
    # info_list()/iter_procs() 는 TTL 이 지나면 '호출한 스레드에서' 전체
    # 프로세스 워크(500개 × 속성 7개, 프로세스마다 핸들 오픈)를 돌린다.
    # 이걸 Tk 스레드에서 부르면 그 수백 ms 동안 창이 멈춘다 — 클릭도
    # 안 먹고 리페인트도 안 된다. 최적화 도구가 자기 창부터 버벅이면
    # 사용자는 "이 프로그램이 내 PC 를 느리게 한다"고 결론 내린다.
    # 아래 두 함수는 절대 기다리지 않는다: 캐시가 있으면 그대로 주고,
    # 낡았으면 백그라운드 갱신만 걸어둔 뒤 낡은 값을 준다. 화면에
    # 몇 초 묵은 프로세스 목록이 뜨는 것은 창이 멈추는 것보다 훨씬 낫다.
    def _refresh_async(self):
        if self._refreshing:
            return
        self._refreshing = True

        def run():
            try:
                self._refresh()
            except Exception as _dx:
                DIAG.q("_GlobalProcCache.run#0", _dx)
            finally:
                self._refreshing = False
        threading.Thread(target=run, daemon=True).start()

    def info_list_nowait(self):
        """캐시된 info-dict 목록. 절대 블로킹하지 않는다."""
        if not self._warmed:
            self._refresh_async()
            return []
        if (time.time() - self._t) > self.TTL:
            self._refresh_async()
        return list(self._info_cache)


_orig_process_iter = psutil.process_iter

# ★신규★ 부모-자식 맵을 '한 번에' 얻는 내부 함수.
# psutil.Process.ppid() 를 프로세스마다 부르면 그때마다
# CreateToolhelp32Snapshot 전체 워크가 돈다(캐시 없음). 이 함수는
# 그 스냅샷을 딱 한 번만 떠서 {pid: ppid} 딕셔너리로 돌려준다.
try:
    from psutil._pswindows import ppid_map as _ppid_map
except Exception:
    try:
        from psutil._psplatform import ppid_map as _ppid_map
    except Exception:
        _ppid_map = None

PROC_CACHE = _GlobalProcCache()
_CACHED_ATTRS = frozenset(_GlobalProcCache._FULL_ATTRS)

# Monkey-patch: most callsites ask for attrs that are a subset of the
# cache's _FULL_ATTRS — those get the cached list instantly. Callers that
# need exotic fields (e.g. io_counters) fall through to the original
# process_iter so behavior is preserved.
def _patched_process_iter(attrs=None, ad_value=None):
    if attrs is None or all(a in _CACHED_ATTRS for a in attrs):
        return iter(PROC_CACHE.iter_procs())
    return _orig_process_iter(attrs=attrs, ad_value=ad_value)
psutil.process_iter = _patched_process_iter


# ----------------------------------------------------------------------------
# ★신규★ FOREGROUND TRACKER — 포그라운드 '프로세스 트리' 보호
# ----------------------------------------------------------------------------
# 이 앱의 모든 강등 액션은 지금까지 "pid != fg_pid" 하나로 대상을 골랐다.
# fg_pid 는 GetForegroundWindow 가 주는 창 소유 프로세스 하나뿐이다.
#
# 문제: 사용자가 실제로 쓰는 앱 대부분이 멀티프로세스다.
#   chrome.exe(본체) ─┬─ chrome.exe --type=renderer   ← 실제 페이지 렌더링
#                     ├─ chrome.exe --type=gpu        ← 실제 디코딩/합성
#                     └─ chrome.exe --type=utility
#   같은 구조가 엣지·디스코드·슬랙·VS Code·옵시디언 등 일렉트론 전부,
#   그리고 언리얼/유니티 기반 게임의 셰이더 컴파일 워커에도 있다.
#
# 결과적으로 유튜브를 보는 동안 chrome.exe 본체만 빠지고, 정작 영상을
# 디코딩하는 GPU 프로세스는 BELOW_NORMAL + EcoQoS(저클럭/E코어) +
# 메모리 우선순위 하향 + IO Low 를 동시에 맞았다. 최적화 도구가 사용자가
# 보고 있는 바로 그 앱을 직접 느리게 만드는 구조였다.
#
# ForegroundTracker 는:
#   (1) 포그라운드 pid 에서 같은 실행파일 이름을 따라 위로 올라가
#       그 앱의 '루트' 프로세스를 찾고
#   (2) 그 루트의 자손 전체를 보호 집합에 넣고
#   (3) 최근 90초 안에 포그라운드였던 앱도 유예로 보호한다
#       (알트탭으로 잠깐 벗어난 앱을 즉시 강등하면 돌아왔을 때 버벅인다)
# ----------------------------------------------------------------------------
class ForegroundTracker:
    TREE_TTL   = 2.0     # 트리 재구성 주기(초)
    GRACE_S    = 90.0    # 최근 포그라운드 유예(초)
    MAX_ASCEND = 6

    def __init__(self):
        self._lk = threading.Lock()
        self._tree = set()
        self._tree_t = 0.0
        self._tree_for = None
        self._recent = {}      # pid -> 마지막으로 포그라운드였던 시각
        self._root = None

    # ── 내부: 부모/자식 맵 구성 ────────────────────────────
    # 이름은 PROC_CACHE(이미 떠 있는 목록)에서, 부모 관계는 ppid_map()
    # '단 한 번' 호출로 얻는다. 트리는 TREE_TTL(2초) 동안 재사용하므로
    # 스냅샷 비용은 2초에 1회다.
    def _maps(self):
        names = {}
        for inf in PROC_CACHE._info_cache:
            pid = inf.get("pid")
            if pid is None: continue
            names[pid] = (inf.get("name") or "").lower()
        parent = {}
        children = defaultdict(list)
        if _ppid_map is not None:
            try:
                for pid, pp in _ppid_map().items():
                    parent[pid] = pp
                    children[pp].append(pid)
                    names.setdefault(pid, "")
            except Exception as _dx:
                DIAG.q("ForegroundTracker._maps#0", _dx)
        return parent, children, names

    def _build(self, fg_pid, fg_name):
        parent, children, names = self._maps()
        if fg_pid not in parent and fg_pid not in names:
            # 캐시가 아직 이 프로세스를 모르는 경우(방금 실행된 앱).
            # 최소한 자기 자신과 psutil 로 얻는 직계 자식은 보호한다.
            out = {fg_pid}
            try:
                for ch in psutil.Process(fg_pid).children(recursive=True):
                    out.add(ch.pid)
            except Exception as _dx:
                DIAG.q("ForegroundTracker._build#0", _dx)
            return out, fg_pid

        # (1) 같은 실행파일 이름을 따라 위로 올라가 루트를 찾는다.
        #     chrome 렌더러(자식)가 포그라운드일 때도 본체를 찾아낸다.
        root = fg_pid
        for _ in range(self.MAX_ASCEND):
            pp = parent.get(root)
            if pp is None or pp in (0, 4): break
            if names.get(pp) != names.get(root): break
            root = pp

        # (2) 루트의 자손 전체 (BFS, 폭주 방지 상한)
        out = {root}
        stack = [root]
        while stack and len(out) < 256:
            cur = stack.pop()
            for ch in children.get(cur, ()):
                if ch not in out:
                    out.add(ch); stack.append(ch)

        # (3) 포그라운드 pid 자신과 그 조상 사슬도 포함
        out.add(fg_pid)
        cur = fg_pid
        for _ in range(self.MAX_ASCEND):
            pp = parent.get(cur)
            if pp is None or pp in (0, 4): break
            out.add(pp); cur = pp
        return out, root

    def refresh(self, fg_pid=None, fg_name=None):
        if fg_pid is None:
            fg_name, fg_pid = get_foreground_info()
        if not fg_pid:
            return self._tree
        now = time.monotonic()
        with self._lk:
            self._recent[fg_pid] = now
            fresh = (now - self._tree_t) < self.TREE_TTL
            same  = (self._tree_for == fg_pid)
            if fresh and same:
                return self._tree
        try:
            tree, root = self._build(fg_pid, fg_name or "")
        except Exception:
            tree, root = {fg_pid}, fg_pid
        with self._lk:
            self._tree = tree
            self._tree_t = now
            self._tree_for = fg_pid
            self._root = root
            for p in tree:
                self._recent[p] = now
            if len(self._recent) > 512:
                cut = now - self.GRACE_S
                self._recent = {k: v for k, v in self._recent.items()
                                if v > cut}
        return tree

    def is_protected(self, pid):
        """이 pid 를 강등해도 되는가? True 면 건드리면 안 된다."""
        if not pid: return False
        now = time.monotonic()
        with self._lk:
            if pid in self._tree:
                return True
            last = self._recent.get(pid)
        if last is not None and (now - last) < self.GRACE_S:
            return True
        # 트리가 오래됐으면 갱신 후 한 번 더 확인
        if (now - self._tree_t) > self.TREE_TTL:
            self.refresh()
            with self._lk:
                return pid in self._tree
        return False

    def tree(self):
        with self._lk:
            return set(self._tree)

    def release(self, pid):
        """유예 목록에서 즉시 제거(복구 완료 후 호출)."""
        with self._lk:
            self._recent.pop(pid, None)


FG = ForegroundTracker()


def release_fg_ecoqos():
    """포그라운드 트리에 걸린 EcoQoS 를 즉시 해제한다(경로 무관).

    ★패치23★ 예전에는 이 해제가 CoreMode._release_fg_tree 안에만
    있었고, 호출도 CoreMode 연속 사이클 한 곳뿐이었다. 그런데
    EcoQoS 를 거는 경로는 셋이다:

        CoreMode._apply_ecoqos_bulk    → 트리 해제 있음
        LatencyOptimizer.apply_ecoqos  → fg_pid '하나' 만 해제
        BatterySaver._loop             → 위 경로 사용

    fg_pid 는 GetForegroundWindow 가 주는 chrome.exe '본체' 다.
    그래서 유튜브를 보는 동안 본체만 풀리고, 정작 영상을 디코딩하는
    --type=gpu / --type=renderer 자식들은 저클럭·E코어에 묶인 채
    남았다. 해제 시점은 충전기를 꽂거나(revert_ecoqos_all) 모드를
    끌 때뿐이었다 — 그 사이 내내 사용자가 보고 있는 그 앱이 느렸다.

    함정 (25)의 변형이다. '새로 안 거는 것'(is_target 의
    FG.is_protected)과 '이미 건 것을 푸는 것'은 다른 일이다.
    """
    try:
        tree = FG.tree()
    except Exception:
        return 0
    if not tree:
        return 0
    try:
        return ECO.release_pids(tree & set(ECO))
    except Exception:
        return 0


class Observer:
    """Lightweight observer — delegates process iteration to PROC_CACHE."""

    def __init__(self, perf, thermal=None):
        self.perf = perf
        # 온도는 못 읽는 PC 가 많다. thermal 이 None 이거나 ok=False 면
        # 스냅샷의 cpu_temp_c 가 None 으로 흘러가고, 화면은 그 항목을
        # 숨긴다. 새 수집 경로를 만들지 않고 기존 스냅샷에 얹는다.
        self.thermal = thermal
        self.last_snap = {}
        self._snap_time = 0.0
        self._lk = threading.Lock()
        # Cached static values — never change after boot
        self._logical = psutil.cpu_count(logical=True) or 1
        self._physical = psutil.cpu_count(logical=False) or 1
        self._boot_time = psutil.boot_time()
        # cpu_freq is sometimes slow on Windows — cache + refresh every 10s
        self._cpu_freq = 0
        self._cpu_freq_t = 0.0
        psutil.cpu_percent(interval=None)  # prime

    def snapshot(self, force=False):
        now = time.time()
        if not force and (now - self._snap_time) < 2.5:
            return self.last_snap

        cpu = psutil.cpu_percent(interval=None)

        # cpu_freq: refresh every 10s only (it's slow on some Windows machines)
        if (now - self._cpu_freq_t) > 10.0:
            try:
                cf = psutil.cpu_freq()
                self._cpu_freq = cf.current if cf else 0
            except Exception:
                self._cpu_freq = 0
            self._cpu_freq_t = now
        cpu_freq = self._cpu_freq

        vm = psutil.virtual_memory()
        try:
            sys_drive = os.environ.get("SystemDrive", "C:") + "\\"
            disk = psutil.disk_usage(sys_drive)
            disk_pct, disk_free, disk_total = disk.percent, \
                disk.free / (1024**3), disk.total / (1024**3)
        except Exception:
            disk_pct = disk_free = disk_total = 0
        try:
            battery = psutil.sensors_battery()
            on_bat = battery is not None and not battery.power_plugged
            bat_pct = battery.percent if battery else 100.0
        except Exception:
            on_bat = False; bat_pct = 100.0

        uptime = (now - self._boot_time) / 3600

        # 온도 — 별도 스레드가 이미 재놓은 값을 읽기만 한다(비용 0).
        try:
            temp_c = self.thermal.cpu_temp_c if self.thermal else None
            temp_ok = bool(self.thermal and self.thermal.ok)
        except Exception:
            temp_c, temp_ok = None, False

        fg_name, fg_pid = get_foreground_info()
        fg_type = self._classify_fg(fg_name)

        # threads_running: reuse cached process list — DO NOT call
        # process_iter directly here. If cache is cold, estimate from CPU
        # so first snapshot doesn't pay the ~2s walk cost on GUI thread.
        if PROC_CACHE._warmed:
            try:
                # ★수정★ 기존: status == "running" 개수.
                # Windows psutil 은 정지되지 않은 모든 프로세스를
                # "running" 으로 보고하므로 이 값은 사실상 '총 프로세스
                # 수'(300개 안팎)였다. threads_ratio 가 늘 8~12 로 나와
                # idle 판정·LPI 의 스케줄러 항·AI 특징 10번이 모두
                # 무의미해졌다. 이제 실제로 CPU 를 쓰고 있는 프로세스만
                # 센다(런큐 근사치).
                threads_running = sum(
                    1 for inf in PROC_CACHE._info_cache
                    if (inf.get("cpu_percent", 0) or 0) >= 1.0
                )
            except Exception:
                threads_running = self._logical
        else:
            # Cheap estimate while cache warms up in the background
            threads_running = max(1, int(self._logical * cpu / 100.0))

        snap = {
            "ts": now,
            "cpu_pct": cpu, "cpu_freq_mhz": cpu_freq,
            "ram_pct": vm.percent,
            "ram_used_mb": (vm.total - vm.available) // (1024 * 1024),
            "ram_total_mb": vm.total // (1024 * 1024),
            "ram_available_mb": vm.available // (1024 * 1024),
            "disk_pct": disk_pct, "disk_free_gb": disk_free,
            "disk_total_gb": disk_total,
            "page_faults": self.perf.page_faults,
            "context_switches": self.perf.ctx_switches,
            "cpu_queue": self.perf.cpu_queue,
            "disk_queue": self.perf.disk_queue,
            "fg_name": fg_name, "fg_pid": fg_pid, "fg_type": fg_type,
            "threads_ratio": threads_running / self._logical,
            "threads_running": threads_running,
            "logical_cores": self._logical, "physical_cores": self._physical,
            "on_battery": on_bat, "battery_pct": bat_pct,
            "uptime_hours": uptime,
            "cpu_temp_c": temp_c, "thermal_ok": temp_ok,
        }
        with self._lk:
            self.last_snap = snap
        self._snap_time = now
        return snap

    def _classify_fg(self, name):
        for s in GAME_SIGS:
            if s in name: return "game"
        for s in CREATIVE_SIGS:
            if s in name: return "creative"
        for s in DEV_SIGS:
            if s in name: return "dev"
        for s in BROWSER_SIGS:
            if s in name: return "browser"
        for s in OFFICE_SIGS:
            if s in name: return "office"
        return "general"

    def get_processes(self, force=False):
        """Returns cached process info list. Delegates to global cache."""
        return PROC_CACHE.info_list(force=force)


def _median(vals):
    """중앙값. 평균과 달리 스파이크 한 번에 대표값이 끌려가지 않는다."""
    if not vals: return 0.0
    s = sorted(vals)
    n = len(s)
    m = n // 2
    return float(s[m]) if n % 2 else (s[m - 1] + s[m]) / 2.0


def compute_lpi(snap):
    """Latency Pressure Index 0-100 (higher = more responsive)."""
    cpu_p = min(100.0, snap["cpu_pct"] * 0.5 + snap["cpu_queue"] * 12.0)
    mem_p = max(0.0, (snap["ram_pct"] - 50.0) * 0.6) + \
            min(20.0, snap["page_faults"] / 200.0)
    io_p = min(100.0, snap["disk_queue"] * 16.0)
    sched_p = max(0.0, (snap["threads_ratio"] - 1.0) * 5.0)
    cpu_s = max(0.0, 100.0 - cpu_p)
    mem_s = max(0.0, 100.0 - min(100.0, mem_p))
    io_s = max(0.0, 100.0 - io_p)
    sched_s = max(0.0, 100.0 - min(100.0, sched_p))
    return int(max(0, min(100, cpu_s * 0.35 + mem_s * 0.25 +
                         io_s * 0.20 + sched_s * 0.20)))


# ============================================================================
# AI CORE — 12-feature softmax classifier with state smoothing
# ============================================================================
class AICore:
    STATES = ("IDLE", "WORK", "MULTITASK", "STUTTER", "GAME", "CREATIVE")

    WEIGHTS = {
        "IDLE":     [-2.5,-1.8,-0.8,-0.5,-1.2,-0.6,-0.5,-0.5,-0.3,-0.2,-0.8, 0.0],
        "WORK":     [ 0.3, 0.2, 0.1, 0.3, 0.0, 0.1, 0.0, 0.0, 1.5, 0.5, 0.0, 0.0],
        "MULTITASK":[ 1.5, 1.3, 0.7, 1.0, 0.8, 0.6, 0.0, 0.0, 0.5, 0.8, 1.0, 0.0],
        "STUTTER":  [ 0.6, 0.4, 1.8, 0.5, 1.7, 1.4, 0.3, 0.3, 0.0, 0.0, 0.5, 0.0],
        "GAME":     [ 1.0, 0.2, 0.0, 0.5, 0.3, 0.2, 3.5, 0.0, 0.0, 0.0, 0.3, 0.5],
        "CREATIVE": [ 1.2, 0.7, 0.5, 0.5, 0.5, 0.5, 0.0, 3.5, 0.5, 0.0, 0.5, 0.5],
    }
    BIAS = {
        "IDLE": 2.5, "WORK": 0.5, "MULTITASK": -0.3,
        "STUTTER": -1.0, "GAME": -1.8, "CREATIVE": -1.8,
    }

    # ★고정 상수 대신 이 PC 의 분포로 정규화한다★
    # 기존 _normalize 는 page_faults/5000, context_switches/50000,
    # cpu_queue/8 같은 상수로 나눴다. 이 값들은 어느 PC 기준인지 알 수
    # 없는 추측이고, 코어가 많은 PC 에서는 컨텍스트 스위치가 유휴 상태
    # 에서도 4만을 넘는다 — 그 특징은 항상 1.0 에 붙어버려 분류에
    # 아무 정보도 주지 못했다(특징이 죽는다).
    # 이제 각 특징을 '이 PC 에서 관측된 상위 10% 값' 으로 나눈다.
    # 같은 코드가 저사양 노트북과 32스레드 데스크톱에서 모두 의미를
    # 갖는다. 표본이 모자라면 기존 상수를 그대로 쓴다.
    SCALE_FALLBACK = {"page_faults": 5000.0, "context_switches": 50000.0,
                      "cpu_queue": 8.0, "disk_queue": 5.0,
                      "threads_ratio": 2.0, "cpu_freq_mhz": 5000.0}
    SCALE_MIN_N = 30
    SCALE_KEEP = 300

    def _scale(self, name, value):
        try:
            v = float(value or 0.0)
        except (TypeError, ValueError):
            return 0.0
        d = self._scales.get(name)
        if d is None:
            d = self._scales[name] = deque(maxlen=self.SCALE_KEEP)
        d.append(v)
        # 우선순위: 이번 실행의 P90 > 지난 실행의 P90 > 폴백 상수.
        # 가운데 항이 없으면 켤 때마다 1~2분씩 분류가 죽는다.
        ref = self._scale_ref.get(name) or self.SCALE_FALLBACK.get(name, 1.0)
        if len(d) >= self.SCALE_MIN_N:
            srt = sorted(d)
            p90 = srt[int(len(srt) * 0.9)]
            if p90 > 1e-6:
                ref = p90
                self._scale_ref[name] = p90
        return min(v / ref, 1.0) if ref > 1e-6 else 0.0

    # ★패치23★ P90 기준값을 세션 밖으로 남긴다.
    # 패치20 에서 '이 PC 의 P90 으로 정규화' 하도록 고쳤지만 그 표본이
    # deque(maxlen=300) 메모리에만 있었다. SCALE_MIN_N=30 이라 앱을
    # 켤 때마다 처음 30사이클(1~2분)은 출처 불명의 fallback 상수로
    # 되돌아갔다 — 코어 많은 PC 에서 특징이 1.0 에 붙어 죽던 패치20
    # 이전 상태로 실행할 때마다 회귀한 것이다.
    SCALE_SAVE_MIN_S = 120.0

    def _scales_path(self):
        d = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        return d / "ai_scales.json"

    def _load_scales(self):
        try:
            with open(str(self._scales_path()), encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            return
        if not isinstance(d, dict):
            return
        for k, v in d.items():
            try:
                v = float(v)
            except (TypeError, ValueError):
                continue
            # 저장값을 그대로 믿지 않는다. 폴백 상수의 1/20~20배를
            # 벗어나면 다른 PC 의 파일이거나 손상된 것으로 본다.
            ref = self.SCALE_FALLBACK.get(k)
            if ref and not (ref / 20.0 <= v <= ref * 20.0):
                continue
            if v > 1e-6:
                self._scale_ref[k] = v

    def _save_scales(self, force=False):
        now = time.time()
        if not force and (now - self._scale_saved) < self.SCALE_SAVE_MIN_S:
            return
        self._scale_saved = now
        if not self._scale_ref:
            return
        try:
            p = self._scales_path()
            p.parent.mkdir(parents=True, exist_ok=True)
            tmp = str(p) + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                f.write(json.dumps(self._scale_ref))
            os.replace(tmp, str(p))
        except Exception as _dx:
            DIAG.q("AICore._save_scales#0", _dx)

    def __init__(self):
        self.last_state = "IDLE"
        self._scales = {}
        self._scale_ref = {}      # 지난 실행에서 관측한 P90
        self._scale_saved = 0.0
        self._load_scales()
        self.confidence = 1.0
        self.state_history = deque(maxlen=20)
        self.lpi_history = deque(maxlen=30)
        self.transitions = defaultdict(int)
        self.session_states = defaultdict(int)
        self.anomaly_count = 0
        self.cycle = 0

    def _normalize(self, s):
        return [
            min(s["cpu_pct"]/100.0, 1.0),
            min(s["ram_pct"]/100.0, 1.0),
            self._scale("page_faults", s["page_faults"]),
            self._scale("context_switches", s["context_switches"]),
            self._scale("cpu_queue", s["cpu_queue"]),
            self._scale("disk_queue", s["disk_queue"]),
            1.0 if s["fg_type"] == "game" else 0.0,
            1.0 if s["fg_type"] == "creative" else 0.0,
            1.0 if s["fg_type"] == "dev" else 0.0,
            1.0 if s["fg_type"] == "browser" else 0.0,
            self._scale("threads_ratio", s["threads_ratio"]),
            self._scale("cpu_freq_mhz", s.get("cpu_freq_mhz", 0)),
        ]

    @staticmethod
    def _softmax(scores):
        ms = max(scores.values())
        es = {k: math.exp(v - ms) for k, v in scores.items()}
        t = sum(es.values())
        return {k: v/t for k, v in es.items()}

    def classify(self, snap):
        self.cycle += 1
        feats = self._normalize(snap)
        self._save_scales()          # 내부 주기 제한(120초)
        logits = {st: self.BIAS[st] + sum(f*w for f, w in zip(feats, self.WEIGHTS[st]))
                 for st in self.STATES}
        probs = self._softmax(logits)
        best = max(probs, key=probs.get)

        self.state_history.append(best)
        if len(self.state_history) >= 3:
            recent = list(self.state_history)[-3:]
            stable = recent[0] if recent[0] == recent[1] == recent[2] \
                    else recent[-1] if recent[-1] == recent[-2] \
                    else self.last_state
        else:
            stable = best

        if stable != self.last_state:
            self.transitions[(self.last_state, stable)] += 1
        self.session_states[stable] += 1
        self.last_state = stable
        self.confidence = probs[best]
        return stable, self.confidence, probs

    def detect_anomaly(self, lpi):
        self.lpi_history.append(lpi)
        if len(self.lpi_history) < 10: return False
        avg = sum(list(self.lpi_history)[-10:-1]) / 9.0
        if lpi < avg * 0.7 and lpi < 50:
            self.anomaly_count += 1
            return True
        return False

    def session_summary(self):
        total = sum(self.session_states.values()) or 1
        return {
            "dominant": max(self.session_states, key=self.session_states.get)
                       if self.session_states else "IDLE",
            "distribution": {k: round(v/total*100, 1)
                            for k, v in self.session_states.items()},
            "anomalies": self.anomaly_count,
            "cycles": self.cycle,
        }

    def recommendations(self, snap):
        recs = []
        if snap["ram_pct"] >= 85:
            recs.append({"severity": "high",
                        "title": "High Memory Pressure",
                        "msg": f"RAM at {snap['ram_pct']:.0f}% — run Hard Core to free memory"})
        elif snap["ram_pct"] >= 70:
            recs.append({"severity": "medium",
                        "title": "Memory Rising",
                        "msg": f"RAM at {snap['ram_pct']:.0f}% — Lite Core can help"})
        if snap["disk_pct"] >= 90:
            recs.append({"severity": "high",
                        "title": "Disk Almost Full",
                        "msg": f"{snap['disk_free_gb']:.1f}GB free — run Storage cleanup"})
        if snap["cpu_queue"] >= 4:
            recs.append({"severity": "high",
                        "title": "CPU Bottleneck",
                        "msg": f"Queue {snap['cpu_queue']:.1f} — Hard Core recommended"})
        if snap.get("uptime_hours", 0) > 168:
            recs.append({"severity": "low",
                        "title": "Long Uptime",
                        "msg": f"Up {snap['uptime_hours']:.0f}h — consider restart"})
        if snap["fg_type"] == "game" and self.last_state != "GAME":
            recs.append({"severity": "info",
                        "title": "Game Detected",
                        "msg": "Switch to Gaming profile in PC Boost tab"})
        return recs


# ============================================================================
# POLICY ENGINE
# ============================================================================
class PolicyEngine:
    PROFILES = ("Auto", "Gaming", "Working", "Multitask", "Creative", "Manual")

    POLICIES = {
        ("Auto", "IDLE"):      [],
        ("Auto", "WORK"):      ["thread_burst", "io_priority"],
        ("Auto", "MULTITASK"): ["thread_burst", "bg_throttle", "io_priority"],
        ("Auto", "STUTTER"):   ["thread_burst", "bg_throttle", "io_priority", "idle_cleanup"],
        ("Auto", "GAME"):      ["thread_burst", "bg_throttle", "io_priority", "mmcss"],
        ("Auto", "CREATIVE"):  ["thread_burst", "io_priority", "mmcss"],
        ("Gaming",   "*"):     ["thread_burst", "bg_throttle", "io_priority", "mmcss", "affinity"],
        ("Working",  "*"):     ["thread_burst", "io_priority"],
        ("Multitask","*"):     ["thread_burst", "bg_throttle"],
        ("Creative", "*"):     ["thread_burst", "io_priority", "mmcss"],
    }

    def __init__(self):
        self.profile = "Auto"
        self.timer_burst_enabled = False
        self.affinity_hint_enabled = False
        self._cooldowns = {k: 0.0 for k in COOLDOWNS}

    def set_profile(self, p):
        if p in self.PROFILES: self.profile = p

    def _ready(self, a):
        return time.monotonic() - self._cooldowns.get(a, 0.0) >= COOLDOWNS.get(a, 1.0)

    def _fire(self, a):
        self._cooldowns[a] = time.monotonic()

    def decide(self, state, snap):
        if self.profile == "Manual": return []
        actions = list(self.POLICIES.get(("Auto", state), [])) if self.profile == "Auto" \
                 else list(self.POLICIES.get((self.profile, "*"), []))
        if self.timer_burst_enabled and state == "GAME":
            actions.append("timer_burst")
        if self.affinity_hint_enabled and IS_HYBRID and state in ("GAME", "CREATIVE"):
            actions.append("affinity")
        if snap["ram_pct"] >= RAM_CRITICAL:
            actions.append("idle_cleanup")
        if IS_WIN11_22H2 and state in ("GAME", "CREATIVE", "STUTTER"):
            actions.append("ecoqos")
        ready = [a for a in actions if self._ready(a)]
        for a in ready: self._fire(a)
        return ready[:5]


# ----------------------------------------------------------------------------
# ACTION LEARNER — "이 PC 에서 실제로 효과가 있었던 액션만 계속한다"
# ----------------------------------------------------------------------------
# ★기존 'AI' 가 무엇이었나★
#   AICore 는 손으로 정한 가중치 표(WEIGHTS)로 상태를 분류하고,
#   PolicyEngine 은 상태→액션 목록을 고정 표에서 꺼냈다. 즉 판단은
#   전부 개발자가 미리 적어둔 상수였고, 실행 결과는 어디에도 되먹임되지
#   않았다. 어떤 액션이 이 PC 에서 아무 효과가 없어도 영원히 계속했다.
#   그건 학습이 아니라 규칙표다.
#
# ★이제 가능해진 이유★
#   패치19 에서 '같은 시간대 대조군' 측정이 생겼다. 효과를 편향 없이
#   잴 수 있게 되자, 비로소 "무엇이 실제로 통하는가"를 물어볼 수 있다.
#   측정 없는 학습은 그냥 미신을 강화한다.
#
# ★설계 — 액션별 무작위 보류(randomized withholding)★
#   매 사이클, 학습 대상 액션마다 ε 확률로 '이번엔 하지 않는다'를 고른다.
#   그리고 사이클 결과(백그라운드 부하, 낮을수록 좋음)를 그 선택과 함께
#   기록한다. 충분히 쌓이면 적용/보류 두 무리의 중앙값을 비교한다.
#     · 무작위로 배정하므로 시간대 교란이 평균적으로 상쇄된다.
#       (패치19 에서 문제 삼은 건 '고정 일정 + 편향된 시점'이지
#        시간분리 자체가 아니다. 무작위 배정은 통계적으로 유효하다)
#     · ε 는 표본이 쌓이면 줄어든다. 계속 모든 걸 실험하지는 않는다.
#
# ★판정 후 행동★
#   helps  → 계속 적용
#   hurts  → 적용 중단(가끔 탐색만)
#   neutral→ 적용 중단. 효과 없는 일을 계속하는 건 CPU 를 쓰는 만큼
#            그 자체로 손해다. 최적화 도구가 할 일이 아니다.
#
# ★학습 대상에서 제외되는 것★
#   되돌릴 수 없거나 안전이 걸린 액션은 학습시키지 않는다. RAM 위급 시
#   정리처럼 '효과가 아니라 필요' 때문에 하는 것도 제외한다.
#
# 학습 결과는 %APPDATA%/OMEGA_X/learned.json 에 남아 다음 실행에서
# 이어진다. PC 마다 답이 다르기 때문에 이 파일은 이 PC 전용이다.
# ----------------------------------------------------------------------------
class ActionLearner:
    """액션별 무작위 보류(randomized withholding)로 '했을 때 vs 안 했을 때'를
    비교한다. 효과가 없거나 오히려 나쁜 액션은 스스로 중단한다.

    ★v2 — v1 은 시뮬레이션에서만 배웠고 실제 PC 에서는 못 배웠다★
    600사이클 재현 결과, 진짜로 0.30코어를 낮추는 액션이 'neutral' 로
    판정돼 영구 중단됐다. 원인과 대응:

      (1) 캐리오버 — 1사이클만 건너뛰어도 지난 사이클에 걸어둔 EcoQoS·
          메모리 우선순위·nice 는 프로세스가 죽을 때까지 살아 있다.
          '보류' 표본이 사실 '적용' 표본이라 두 무리의 차이가 절반으로
          줄었다. → 결정을 BLOCK 사이클 동안 유지하고, off 로 뒤집히는
          순간 호출부가 실제로 되돌리게 한다(needs_release).
      (2) 잔상 — 방금 뒤집은 직후의 측정에는 직전 상태가 섞인다.
          → 블록의 앞 WARMUP 번은 표본으로 쓰지 않는다.
      (3) 문턱이 표본 수와 무관했다 — MAD 합을 그대로 썼는데 배경
          부하가 하루 종일 표류하는 PC 에서는 MAD 가 늘 커서 진짜 효과가
          묻힌다. → 표본이 쌓일수록 문턱이 내려가게 √n 으로 나눈다.
      (4) 중단이 비가역이었다 — neutral 이면 적용을 멈추므로 적용 표본이
          더 안 쌓여 영원히 neutral 이다. → 표본에 시각을 붙여 TTL 이
          지나면 버린다. 중단된 액션은 적용 표본이 먼저 말라 자동으로
          learning 으로 돌아가 재검증된다.
      (5) 문맥(app:*)마다 팔이 생겨 learned.json 이 무한히 커졌다.
          → 총량 상한 + 오래 안 쓴 것부터 정리.
    """
    LEARNABLE = ("ecoqos", "bg_throttle", "mem_priority", "trim",
                 "standby", "io_priority", "mmcss", "affinity")
    MIN_N = 8            # 적용/보류 각각 이만큼은 모여야 판정
    KEEP = 80
    EXPLORE_START = 0.35
    EXPLORE_MIN = 0.08
    SAVE_MIN_S = 20.0
    BLOCK = 3            # 결정 하나를 이만큼 유지(캐리오버 제거)
    WARMUP = 1           # 블록 앞부분은 표본에서 뺀다(잔상 제거)
    SAMPLE_TTL_S = 86400.0
    MAX_ARMS = 120       # 파일 크기·기동 시간 상한(팔당 표본 2*KEEP)
    NOISE_FLOOR = 0.02   # 이보다 작은 차이는 코어 단위로 무의미
    PRUNE_S = 60.0
    PAIR_K = 6           # 짝지을 이웃 표본 반경(시간 지역 비교)
    NOISE_C = 1.8        # 문턱 계수(크면 보수적 — 헛판정 대신 판정 지연)
    REVISIT = 60         # 한쪽 표본이 이만큼 오래되면 강제로 그쪽을 채운다
    MIN_BLOCKS = 4       # 짝지어진 블록이 이만큼은 있어야 판정
    AGREE = 0.85         # 블록의 이 비율 이상이 같은 방향이어야 판정

    def __init__(self):
        self._lk = threading.RLock()
        self._arms = {}          # key -> {"on": [[t,v]..], "off": [...], "t": ts}
        self._pending = {}       # key -> "on" | "off"
        self._block = {}         # action -> {"on","age","keys","release"}
        # ★시드를 0 으로 고정하면 매 실행·모든 PC 가 같은 난수열을 쓴다★
        # 스케줄 주기와 위상이 맞물리면 배정이 한쪽으로 굳는다.
        self._seed = ((int(time.time() * 1000) ^ (os.getpid() << 13))
                      & 0x7FFFFFFF) or 12345
        self._last_save = 0.0
        self._last_prune = 0.0
        self._seq = 0
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "learned.json"
        self.load()

    # ── 결정 ─────────────────────────────────────────────────────────
    def _key(self, state, action):
        return "%s|%s" % (state or "any", action)

    def _arm(self, state, action):
        k = self._key(state, action)
        a = self._arms.get(k)
        if a is None:
            a = self._arms[k] = {"on": [], "off": [], "t": time.time()}
        return a

    def _fresh(self, seq, now=None):
        """TTL 안에 든 표본의 값만."""
        now = time.time() if now is None else now
        ttl = self.SAMPLE_TTL_S
        out = []
        for p in seq:
            try:
                if now - p[0] <= ttl:
                    out.append(p[1])
            except Exception:
                continue
        return out

    def _fresh_kv(self, seq, now=None):
        """(순번, 값) — 순번은 두 무리를 시간순으로 섞기 위한 것."""
        now = time.time() if now is None else now
        ttl = self.SAMPLE_TTL_S
        out = []
        for p in seq:
            try:
                if now - p[0] > ttl:
                    continue
                out.append((float(p[2]) if len(p) > 2 else float(p[0]),
                            float(p[1])))
            except Exception:
                continue
        return out

    def explore_rate(self, state, action):
        a = self._arm(state, action)
        n = min(len(self._fresh(a["on"])), len(self._fresh(a["off"])))
        if n >= self.MIN_N * 3:
            return self.EXPLORE_MIN
        span = self.EXPLORE_START - self.EXPLORE_MIN
        return self.EXPLORE_MIN + span * (1.0 - n / float(self.MIN_N * 3))

    # ── 계층적 문맥 ──────────────────────────────────────────────────
    # ★같은 액션이라도 앱마다 답이 다르다★
    # 마인크래프트에서는 백그라운드 절전이 크게 듣고, 문서 작업 중에는
    # 아무 차이가 없을 수 있다. 그래서 문맥을 두 층으로 둔다.
    #   구체: "app:minecraft"   일반: "profile:game"
    # 판정은 구체 문맥에 표본이 충분하면 그걸 쓰고, 모자라면 일반 문맥의
    # 판정으로 물러난다(backoff). 기록은 ★양쪽 모두★ 에 남긴다 —
    # 그래야 처음 보는 앱도 일반 지식으로 시작하고, 쓸수록 그 앱만의
    # 답으로 갈라진다. 앱을 하나 열 때마다 처음부터 배우게 하면
    # 학습이 영원히 끝나지 않는다.
    def allow(self, ctx, action):
        """이번 사이클에 이 액션을 할 것인가. 선택은 기록해 둔다.

        ctx: 문자열 하나, 또는 구체→일반 순서의 문맥 목록.

        ★한 사이클이 아니라 블록 단위로 답한다★ 결정을 BLOCK 번
        유지해야 '안 한 상태'가 실제로 성립한다. 문맥이 바뀌면(다른 앱으로
        전환) 블록을 새로 연다 — 다른 앱의 상태를 이 앱의 표본으로
        쓰면 안 되기 때문이다."""
        if action not in self.LEARNABLE:
            return True
        keys = [ctx] if isinstance(ctx, str) else [k for k in (ctx or []) if k]
        if not keys:
            keys = ["any"]
        state = keys[0]
        with self._lk:
            b = self._block.get(action)
            if b is None or b["age"] >= self.BLOCK:
                prev_on = bool(b["on"]) if b else False
                on = self._decide(keys, action, state)
                b = self._block[action] = {
                    "on": bool(on), "age": 0, "keys": list(keys),
                    "release": bool(prev_on and not on), "taint": False}
            elif b["keys"] != keys:
                # ★블록 도중에 앱이 바뀌었다★ 결정은 그대로 둔다.
                # 여기서 결정을 다시 뽑으면 알트탭할 때마다 켰다 껐다를
                # 반복하게 되고(그때마다 되돌리기 비용이 든다), 그렇게
                # 얻은 표본은 어느 앱의 것인지도 불분명하다.
                # 대신 이 블록은 표본으로 쓰지 않는다.
                b["keys"] = list(keys)
                b["taint"] = True
            b["age"] += 1
            if b["age"] > self.WARMUP and not b.get("taint"):
                side = "on" if b["on"] else "off"
                for k in keys:
                    self._pending[self._key(k, action)] = side
            return bool(b["on"])

    def _decide(self, keys, action, state):
        v = None
        for k in keys:
            vv = self.verdict(k, action)
            if vv["state"] != "learning":
                v = vv
                break
        if v is None:
            v = self.verdict(keys[-1], action)
        arm = self._arm(state, action)
        n_on, n_off = len(self._fresh(arm["on"])), len(self._fresh(arm["off"]))
        if v["state"] == "learning":
            # ★학습 단계에서는 '적은 쪽'을 채운다(균형 배정)★
            # 순수 확률 탐색만 쓰면 보류 표본이 좀처럼 안 모여서
            # 판정이 한참 뒤로 밀린다. 두 무리를 비슷하게 채워야
            # 비교가 빨리 성립한다. 동수일 때만 동전을 던진다.
            if n_off < n_on:
                return 0
            if n_on < n_off:
                return 1
            return self._coin()
        pref = 1 if v["state"] == "helps" else 0
        # ★판정이 섰다고 비교를 끊으면 안 된다★ ε 탐색만 남기면 소수쪽
        # 표본이 수백 사이클에 한 번씩만 생기고, 그러면 두 무리가 서로
        # 다른 시간대에 놓여 짝지을 수가 없다(재현: 진짜 효과 검출률이
        # 70%에서 20%로 떨어졌다). 소수쪽이 오래 비면 강제로 채운다 —
        # 이게 측정의 유지비다.
        stale = self._stale_side(state, action)
        if stale is not None:
            return stale
        eps = self.explore_rate(state, action)
        # 확률 판정과 동전은 서로 다른 난수여야 한다(같은 시드의
        # 다른 비트를 쓰면 상관이 생겨 배정이 한쪽으로 쏠린다).
        if self._rand() < eps:
            return 1 - pref
        return pref

    def _stale_side(self, state, action):
        """최근 표본이 한쪽에만 쌓였으면 반대쪽을 돌려준다."""
        a = self._arm(state, action)
        last = {}
        for side in ("on", "off"):
            kv = self._fresh_kv(a[side])
            last[side] = max((q for q, _ in kv), default=None)
        if last["on"] is None or last["off"] is None:
            return None
        newest = max(last["on"], last["off"])
        if newest - last["off"] > self.REVISIT:
            return 0
        if newest - last["on"] > self.REVISIT:
            return 1
        return None

    def needs_release(self, action):
        """방금 '보류'로 뒤집혔으면 딱 한 번 True.

        ★호출부는 이때 실제로 되돌려야 한다★ 새로 걸지 않는 것만으로는
        이미 걸린 것이 풀리지 않는다. 되돌리지 않으면 보류 표본이
        '적용된 채 추가만 안 한' 상태가 되어 비교가 무의미해진다."""
        with self._lk:
            b = self._block.get(action)
            if b and b.get("release"):
                b["release"] = False
                return True
        return False

    def block_state(self, action):
        """화면·디버깅용 — 지금 이 액션이 어느 블록의 몇 번째인가."""
        with self._lk:
            b = self._block.get(action)
            if not b:
                return None
            return {"on": b["on"], "age": b["age"], "block": self.BLOCK}

    def _rand(self):
        self._seed = (self._seed * 1103515245 + 12345) & 0x7FFFFFFF
        return (self._seed >> 8) / float(1 << 23)

    def _coin(self):
        self._seed = (self._seed * 1103515245 + 12345) & 0x7FFFFFFF
        return (self._seed >> 16) & 1

    def jitter(self, n):
        """0 ~ n-1. 스케줄 위상을 흔드는 데 쓴다(고정 위상 교락 방지)."""
        try:
            n = int(n)
        except (TypeError, ValueError):
            return 0
        if n <= 1:
            return 0
        return int(self._rand() * n) % n

    def commit(self, outcome):
        """이번 사이클의 결과(낮을수록 좋음)를 이번 선택들에 기록한다."""
        try:
            o = float(outcome)
        except (TypeError, ValueError):
            with self._lk:
                self._pending.clear()
            return
        if o != o or o in (float("inf"), float("-inf")):
            with self._lk:
                self._pending.clear()
            return
        now = time.time()
        with self._lk:
            self._seq += 1
            sq = self._seq
            for k, side in self._pending.items():
                a = self._arms.setdefault(
                    k, {"on": [], "off": [], "t": now})
                a["t"] = now
                a[side].append([now, o, sq])
                if len(a[side]) > self.KEEP:
                    del a[side][0:len(a[side]) - self.KEEP]
            self._pending.clear()
            if now - self._last_prune > self.PRUNE_S:
                self._last_prune = now
                self._prune_locked(now)
        self.save()

    def _prune_locked(self, now):
        """만료 표본 제거 + 팔 총량 상한(앱마다 팔이 생기므로 필요)."""
        dead = []
        for k, a in self._arms.items():
            for side in ("on", "off"):
                a[side] = [p for p in a[side]
                           if isinstance(p, (list, tuple))
                           and now - p[0] <= self.SAMPLE_TTL_S]
            if not a["on"] and not a["off"]:
                dead.append(k)
        for k in dead:
            self._arms.pop(k, None)
        extra = len(self._arms) - self.MAX_ARMS
        if extra > 0:
            order = sorted(self._arms.items(),
                           key=lambda kv: kv[1].get("t", 0.0))
            for k, _ in order[:extra]:
                self._arms.pop(k, None)

    # ── 판정 ─────────────────────────────────────────────────────────
    @staticmethod
    def _spread(v):
        if len(v) < 3:
            return 0.0
        m = _median(v)
        return _median([abs(x - m) for x in v])

    def _paired_diffs(self, on_kv, off_kv):
        """★표류 대책 — 같은 시간대끼리만 비교한다★

        두 무리의 전체 중앙값을 그냥 빼면, 한쪽 표본이 특정 시간대에
        몰려 있을 때 그 시간대의 배경 부하가 그대로 '효과'로 둔갑한다.
        (600사이클 재현: 진짜 0.30코어짜리 효과를 0.61 로 부풀리고,
        효과가 전혀 없는 액션을 -0.27 '오히려 나쁨' 으로 오판했다.
        판정이 helps 로 굳으면 보류 표본이 드물어져 몇몇 시간대에만
        몰리기 때문에, 표본이 쌓일수록 오히려 심해진다.)

        그래서 보류 표본마다 시간상 가까운 적용 표본들의 중앙값과
        짝지어 차이를 낸다. 전역 변화는 두 값에 똑같이 실려 상쇄된다
        — 패치19 의 동시 대조군과 같은 논리를 시간축에 적용한 것."""
        if not on_kv or not off_kv:
            return []
        on_s, off_s = sorted(on_kv), sorted(off_kv)
        # ★두 무리가 같은 구간을 덮도록 먼저 자른다★
        # KEEP 상한 때문에 한쪽만 최근으로 잘리면, 남은 옛 표본이
        # 한참 뒤의 표본과 짝지어져 그 사이의 표류가 통째로 '효과'로
        # 들어온다(재현: 진짜 0.30 인데 0.12, 효과 0 인데 +0.13).
        lo = max(on_s[0][0], off_s[0][0])
        hi = min(on_s[-1][0], off_s[-1][0])
        on_s = [p for p in on_s if lo <= p[0] <= hi]
        off_s = [p for p in off_s if lo <= p[0] <= hi]
        if len(on_s) < 3 or len(off_s) < 3:
            return []
        # ★적은 쪽을 기준으로 짝을 짓는다★ 기준을 많은 쪽에 두면
        # 대부분의 표본이 짝을 못 찾아 버려진다(액션이 해로워서 거의
        # 항상 보류 중일 때 검출률이 반토막 났다).
        if len(off_s) <= len(on_s):
            anchor, other, sign = off_s, on_s, 1.0
        else:
            anchor, other, sign = on_s, off_s, -1.0
        gaps = [other[i + 1][0] - other[i][0] for i in range(len(other) - 1)]
        win = max(4.0, float(self.PAIR_K) * (_median(gaps) if gaps else 1.0))
        oq = [r for r, _ in other]
        groups, cur, prev = [], [], None
        j = 0                    # other 안에서 q 를 넘어선 첫 위치(두 포인터)
        for q, v in anchor:      # anchor·other 모두 순번 오름차순
            # ★앞뒤 양쪽에서 짝을 잡는다★ 한쪽만 쓰면 그 사이의 표류가
            # 통째로 차이에 실린다. 앞의 표본과 뒤의 표본을 평균 내면
            # 그 구간에서 일정하게 흐르는 변화는 상쇄된다.
            while j < len(other) and other[j][0] <= q:
                j += 1
            bef = [w for r, w in other[max(0, j - 3):j] if 0 < q - r <= win]
            aft = [w for r, w in other[j:j + 3] if 0 < r - q <= win]
            if not (bef and aft):
                prev = q
                continue
            d = sign * (v - (_median(bef) + _median(aft)) / 2.0)
            # ★블록 하나가 관측 하나다★ 같은 블록 안의 표본들은 같은
            # 상황에서 나온 값이라 독립이 아니다. 사이에 반대쪽 표본이
            # 끼어 있으면 다른 블록으로 본다. 블록마다 대표값을 하나만
            # 내야 문턱이 실제 불확실성(=블록 간 흔들림)을 반영한다.
            if cur and any(prev < r < q for r in oq):
                groups.append(_median(cur)); cur = []
            cur.append(d); prev = q
        if cur:
            groups.append(_median(cur))
        return groups

    def verdict(self, state, action):
        a = self._arm(state, action)
        on_kv, off_kv = self._fresh_kv(a["on"]), self._fresh_kv(a["off"])
        out = {"state": "learning", "delta": 0.0,
               "n_on": len(on_kv), "n_off": len(off_kv)}
        if len(on_kv) < self.MIN_N or len(off_kv) < self.MIN_N:
            return out
        diffs = self._paired_diffs(on_kv, off_kv)
        if len(diffs) < self.MIN_BLOCKS:
            # ★짝이 안 지어지면 판정하지 않는다★ 예전에는 여기서 전역
            # 비교로 물러났는데, 그건 바로 이 문제를 일으키는 계산이라
            # 물러날 곳이 못 된다. 아직 모른다고 말하는 편이 낫다 —
            # learning 이면 균형 배정이 다시 돌아 짝이 빨리 모인다.
            return out
        delta = _median(diffs)              # +면 적용 쪽이 더 낮다(좋다)
        spread = self._spread(diffs)
        n = float(len(diffs))
        out["delta"] = delta
        out["n_blocks"] = int(n)
        # ★문턱은 표본 수와 함께 내려간다★ 흔들림(MAD)을 그대로 문턱으로
        # 쓰면 부하가 종일 표류하는 PC 에서는 진짜 효과도 영원히 neutral
        # 이 되고, 그러면 그 액션은 중단된다. 흔들림이 커도 표본이 많으면
        # 중앙값의 위치는 그만큼 정확해진다.
        # n 은 표본 수가 아니라 ★블록 수★ 다(_paired_diffs 가 블록마다
        # 대표값 하나만 낸다). 표본 수로 나누면 같은 블록의 값들을 독립인
        # 것처럼 세게 되어, 효과가 전혀 없는 액션의 절반 이상을
        # helps/hurts 로 오판한다.
        noise = max(self.NOISE_FLOOR, self.NOISE_C * spread / math.sqrt(n))
        # ★부호가 일관되는지도 본다★ 흔들림(MAD)이 우연히 0 에 가깝게
        # 나오면 문턱도 0 이 되어 아무 차이나 통과한다. 블록 대부분이
        # 같은 방향을 가리킬 때만 방향을 말한다 — 크기 대신 방향을 보는
        # 이 조건은 표본이 적을 때 특히 안전하다.
        agree = sum(1 for d in diffs if (d > 0) == (delta > 0)) / n
        if abs(delta) < noise or agree < self.AGREE:
            out["state"] = "neutral"
        else:
            out["state"] = "helps" if delta > 0 else "hurts"
        return out

    def summary(self):
        """화면용 — 표본이 있는 (상태, 액션)만."""
        rows = []
        with self._lk:
            keys = list(self._arms.keys())
        for k in keys:
            st, _, act = k.partition("|")
            v = self.verdict(st, act)
            if v["n_on"] or v["n_off"]:
                rows.append({"state_key": st, "action": act, **v})
        rows.sort(key=lambda r: (-abs(r["delta"]), r["action"]))
        return rows

    def app_rows(self, prefix="app:"):
        """앱별로 갈라진 학습 결과만 추린다(화면용)."""
        return [r for r in self.summary()
                if r["state"] in ("helps", "hurts")
                and str(r["state_key"]).startswith(prefix)]

    def reset(self):
        with self._lk:
            self._arms = {}
            self._pending = {}
            self._block = {}
        self.save(force=True)

    # ── 영속 ─────────────────────────────────────────────────────────
    def save(self, force=False):
        now = time.time()
        with self._lk:
            if not force and now - self._last_save < self.SAVE_MIN_S:
                return
            self._last_save = now
            # 자릿수를 줄여 파일을 작게 유지한다(기동 시 통째로 읽는다).
            def _pack(seq):
                out = []
                for x in seq[-self.KEEP:]:
                    try:
                        out.append([int(x[0]), round(float(x[1]), 4),
                                    int(x[2]) if len(x) > 2 else 0])
                    except Exception:
                        continue
                return out
            data = {}
            for k, v in self._arms.items():
                data[k] = {"on": _pack(v["on"]), "off": _pack(v["off"]),
                           "t": int(v.get("t", now))}
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            tmp = self._path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f)
            os.replace(str(tmp), str(self._path))
        except Exception as _dx:
            DIAG.q("ActionLearner.save#0", _dx)

    @staticmethod
    def _load_side(raw, now):
        """[[t,v], ...] 를 읽는다. 구버전 파일([v, ...])도 받아준다."""
        out = []
        for x in (raw or []):
            try:
                if isinstance(x, (list, tuple)) and len(x) >= 3:
                    # ★순번을 반드시 보존한다★ 순번을 버리고 시각만 남기면
                    # 같은 초에 기록된 표본들이 전부 동순위가 되어 앞뒤
                    # 짝짓기가 무너진다(재시작하면 학습이 리셋된 것처럼 됨).
                    out.append([float(x[0]), float(x[1]), float(x[2])])
                elif isinstance(x, (list, tuple)) and len(x) >= 2:
                    out.append([float(x[0]), float(x[1])])
                else:
                    out.append([now, float(x)])
            except (TypeError, ValueError):
                continue
        return out

    def load(self):
        try:
            if not self._path.exists():
                return
            # 어떤 이유로든 파일이 비정상적으로 커졌으면 읽지 않는다
            # (기동 경로라 여기서 수백 ms 를 쓰면 창이 그만큼 늦게 뜬다).
            if self._path.stat().st_size > 4 * 1024 * 1024:
                try: self._path.unlink()
                except Exception as _dx: DIAG.q("ActionLearner.load#0", _dx)
                return
            with open(self._path, "r", encoding="utf-8") as f:
                data = json.load(f)
            now = time.time()
            arms = {}
            for k, v in (data or {}).items():
                on = self._load_side(v.get("on"), now)[-self.KEEP:]
                off = self._load_side(v.get("off"), now)[-self.KEEP:]
                arms[k] = {"on": on, "off": off,
                           "t": float(v.get("t", now) or now)}
            # ★순번 카운터를 이어붙인다★ 0 부터 다시 세면 새 표본이
            # 지난 실행 표본보다 '앞'에 놓여 시간순 비교가 뒤집힌다.
            top = 0.0
            for a in arms.values():
                for side in ("on", "off"):
                    for x in a[side]:
                        if len(x) > 2 and x[2] > top:
                            top = x[2]
            with self._lk:
                self._arms = arms
                self._seq = int(top) + 1
                self._prune_locked(now)
        except Exception as _dx:
            DIAG.q("ActionLearner.load#1", _dx)


# ══════════════════════════════════════════════════════════════════════
# ACTIVITY LOG — "무엇을 했고, 무엇을 왜 안 했는지" (PATCH26)
# ══════════════════════════════════════════════════════════════════════
# 기존 진행 로그의 한계가 셋이었다.
#   (a) 화면에 최근 8줄만, 그것도 AI 코어 화면을 보고 있을 때만 남았다.
#       모드를 멈추면 카드째 사라져 방금 무엇을 했는지 확인할 수 없었다.
#   (b) 파일로 남지 않아 "이렇게 돌았다"를 밖으로 내보낼 방법이 없었다.
#       테스트 결과를 주고받으려면 화면을 사진으로 찍는 수밖에 없었다.
#   (c) ★건너뛴 액션은 아무 기록도 남기지 않았다★ 학습 보류·주기 대기·
#       조건 미달·OS 미지원은 전부 '조용히 아무 일도 안 일어남'으로 보여서,
#       정상 동작과 고장을 구분할 수 없었다. 어떤 로그가 없는 것보다
#       나쁜 건, 있는데 실행만 적고 미실행은 안 적는 로그다.
#
# 그래서 실행(run) / 건너뜀(skip) / 실패(fail) / 사이클 요약(cycle) 네 종류를
# 같은 줄 형식으로 남긴다. 사이클 요약이 있으면 "이번 4초 동안 무엇을
# 하기로 했고 무엇을 미뤘는가"가 한 줄로 보인다.
#
# 비용: 사이클당 파일 쓰기 1~10줄(수 KB/분). 파일은 512KB 에서 .1 로 한 번
#       넘기고 그 이상은 버린다. 쓰기가 실패하면 파일 기록만 끄고 메모리
#       기록은 계속한다 — 로그가 앱을 멈추게 하면 안 된다.
class ActivityLog:
    KEEP = 400                 # 화면용 메모리 보관 줄 수
    FILE_MAX = 512 * 1024      # 이 크기를 넘으면 .1 로 회전

    def __init__(self):
        self._lk = threading.RLock()
        self._rows = deque(maxlen=self.KEEP)
        self._ver = 0
        self._file_ok = True
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "activity.log"

    # ── 기록 ─────────────────────────────────────────────────────────
    def record(self, kind, label, result="", ok=True, cycle=0, reason=""):
        """kind: run | skip | fail | cycle | mode"""
        row = {"ts": time.time(), "kind": str(kind), "label": str(label)[:120],
               "result": str(result)[:160], "ok": bool(ok),
               "cycle": int(cycle or 0), "reason": str(reason)[:40]}
        with self._lk:
            self._rows.append(row)
            self._ver += 1
        self._append_file(row)
        return row

    def cycle_summary(self, cycle, ran, skipped):
        """ran: [라벨...], skipped: {키: 사유}"""
        try:
            sk = ", ".join("%s(%s)" % (k, v) for k, v in sorted(skipped.items()))
        except Exception:
            sk = ""
        self.record("cycle", "cycle %d" % int(cycle or 0),
                    "ran=%d [%s] | skipped=[%s]"
                    % (len(ran), ", ".join(ran)[:100], sk[:120]),
                    ok=True, cycle=cycle)

    # ── 읽기 ─────────────────────────────────────────────────────────
    def version(self):
        with self._lk:
            return self._ver

    def rows(self, n=200):
        with self._lk:
            r = list(self._rows)
        return r[-int(n):] if n else r

    def text(self, n=400):
        """클립보드·파일용 원문. 라벨은 번역하지 않는다 —
        번역된 로그는 개발자가 코드와 대조할 수 없다."""
        out = []
        for r in self.rows(n):
            out.append(self._fmt(r))
        return "\n".join(out)

    @staticmethod
    def _fmt(r):
        try:
            ts = datetime.fromtimestamp(r["ts"]).strftime("%H:%M:%S")
        except Exception:
            ts = "--:--:--"
        mark = {"run": "OK", "skip": "--", "fail": "!!", "cycle": "##",
                "mode": ">>"}.get(r["kind"], "  ")
        if not r["ok"]:
            mark = "!!"
        line = "%s [%s] #%d %s" % (ts, mark, r["cycle"], r["label"])
        if r["reason"]:
            line += "  <%s>" % r["reason"]
        if r["result"]:
            line += "  -> %s" % r["result"]
        return line

    def path(self):
        return self._path

    def clear(self):
        with self._lk:
            self._rows.clear()
            self._ver += 1
        try:
            if self._path.exists():
                self._path.unlink()
        except Exception as _dx:
            DIAG.q("ActivityLog.clear#0", _dx)

    # ── 파일 ─────────────────────────────────────────────────────────
    def _append_file(self, row):
        if not self._file_ok:
            return
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            try:
                if self._path.exists() and self._path.stat().st_size > self.FILE_MAX:
                    bak = self._path.with_suffix(".1.log")
                    try:
                        if bak.exists():
                            bak.unlink()
                    except Exception as _dx:
                        DIAG.q("ActivityLog._append_file#0", _dx)
                    self._path.replace(bak)
            except Exception as _dx:
                DIAG.q("ActivityLog._append_file#1", _dx)
            with open(str(self._path), "a", encoding="utf-8") as f:
                f.write(self._fmt(row) + "\n")
        except Exception:
            # 한 번 실패하면 계속 실패할 가능성이 높다(권한·경로).
            # 로그 때문에 매 사이클 예외를 던지느니 파일 기록만 끈다.
            self._file_ok = False


ACTLOG = ActivityLog()


LEARN = ActionLearner()

# ----------------------------------------------------------------------------
# USAGE PREDICTOR — 이 PC 의 사용 패턴을 배워 다음에 쓸 앱을 예측한다
# ----------------------------------------------------------------------------
# ★왜 예측인가★
#   최적화는 언제나 늦게 온다. 게임이 이미 로딩을 끝낸 뒤에 프로필을
#   바꿔봐야 정작 제일 버벅이는 구간(로딩·셰이더 컴파일)은 지나간 뒤다.
#   무엇을 열지 미리 알면 그 전에 준비할 수 있다.
#
# ★모델★ 1차 마르코프 + 시간대 사전분포. 신경망이 아니라 세는 것이다.
#     P(다음 앱 | 지금 앱)      — 전이 횟수
#     P(앱 | 지금 시각대)        — 시간대(4시간 단위 6칸) 히스토그램
#   두 분포를 곱해 정규화한다. 표본이 적을 때 시간대 사전분포가
#   전이표의 빈틈을 메우고, 표본이 쌓이면 전이표가 지배한다.
#   이 정도가 '세어서 알 수 있는 것'의 정직한 한계다. 여기서 더 나가면
#   맞지도 않는 예측으로 사용자 PC 를 미리 건드리게 된다.
#
# ★안전 범위★ 예측으로 하는 일은 '프로필을 미리 고르는 것'뿐이다.
#   되돌릴 수 있는 힌트 수준이고, 예측이 틀려도 다음 사이클에 실제
#   포그라운드 앱이 그것을 덮어쓴다. 예측으로 파괴적 액션을 하지 않는다.
#
# ★기록되는 것★ 실행 파일 이름과 전환 시각뿐이다. 창 제목·경로·내용은
#   보지 않는다. 파일은 이 PC 안에만 있고 어디로도 보내지 않는다.
#   설정에서 끄면 즉시 수집을 멈추고 파일을 지운다.
# ----------------------------------------------------------------------------
class UsagePredictor:
    KEEP_APPS = 60          # 이만큼의 앱만 추적(오래된 것부터 정리)
    MIN_N = 6               # 이만큼 봐야 예측을 말한다
    MIN_DWELL_S = 20.0      # 이보다 짧게 스친 전환은 전이로 안 센다
    SLOTS = 6               # 하루를 4시간 6칸으로
    SAVE_MIN_S = 30.0

    def __init__(self):
        self._lk = threading.RLock()
        self._trans = {}        # "a>b" -> count
        self._hour = {}         # "app|slot" -> count
        self._cur = None
        self._since = 0.0
        self._last_tsum = 0
        self._total = 0
        self._last_save = 0.0
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        self._path = self._dir / "app_patterns.json"
        self.load()

    @staticmethod
    def _norm(name):
        n = (name or "").strip().lower()
        if n.endswith(".exe"):
            n = n[:-4]
        return n

    @staticmethod
    def _slot(ts=None):
        return int(time.localtime(ts or time.time()).tm_hour // 4) % 6

    def observe(self, app_name):
        """포그라운드 앱이 바뀔 때마다 호출. 같은 앱이면 아무 일도 없다."""
        n = self._norm(app_name)
        if not n:
            return
        now = time.time()
        with self._lk:
            if n == self._cur:
                return
            prev, dwell = self._cur, now - self._since
            self._cur, self._since = n, now
            self._hour["%s|%d" % (n, self._slot(now))] = \
                self._hour.get("%s|%d" % (n, self._slot(now)), 0) + 1
            self._total += 1
            # 스쳐 지나간 창(알트탭 중간 경유 등)은 전이로 세지 않는다.
            if prev and dwell >= self.MIN_DWELL_S:
                k = "%s>%s" % (prev, n)
                self._trans[k] = self._trans.get(k, 0) + 1
            if len(self._trans) > self.KEEP_APPS * 8:
                self._prune_locked()
        self.save()

    def _prune_locked(self):
        items = sorted(self._trans.items(), key=lambda kv: -kv[1])
        self._trans = dict(items[:self.KEEP_APPS * 4])

    def predict(self, current=None, top=3):
        """다음에 쓸 앱 후보. [(앱, 확률), ...] — 근거가 없으면 빈 목록."""
        with self._lk:
            cur = self._norm(current) if current else self._cur
            total = self._total
            trans = dict(self._trans)
            hour = dict(self._hour)
        if total < self.MIN_N:
            return []
        slot = self._slot()
        nxt = {}
        tsum = 0
        for k, c in trans.items():
            a, _, b = k.partition(">")
            if cur and a != cur:
                continue
            nxt[b] = nxt.get(b, 0) + c
            tsum += c
        prior = {}
        psum = 0
        for k, c in hour.items():
            app, _, sl = k.rpartition("|")
            if sl == str(slot):
                prior[app] = prior.get(app, 0) + c
                psum += c
        if not nxt and not prior:
            return []
        apps = set(nxt) | set(prior)
        out = []
        for a in apps:
            if a == cur:
                continue
            # 라플라스 평활 — 한 번도 못 본 조합에 0 을 주지 않는다.
            p_t = (nxt.get(a, 0) + 1.0) / (tsum + len(apps))
            p_h = (prior.get(a, 0) + 1.0) / (psum + len(apps)) if psum else 1.0
            out.append((a, p_t * p_h))
        # ★'그 밖의 것' 몫을 남겨 둔다★ 근거가 약할수록 이 몫이 커진다.
        # 이게 없으면 후보가 하나뿐일 때 무조건 100% 라고 말하게 된다.
        # (전이 표본이 0인데 확신하는 게 예측 기능의 대표적 거짓말이다)
        unknown = 1.0 / max(1, tsum)
        z = sum(v for _, v in out) + unknown
        out = [(a, v / z) for a, v in out]
        out.sort(key=lambda kv: -kv[1])
        self._last_tsum = tsum
        return out[:top]

    MIN_TRANS = 3            # 지금 앱에서 나가는 전이를 이만큼은 봐야 한다

    def confident(self, min_p=0.45):
        """확률이 충분히 높은 예측만. 애매하면 아무 말도 하지 않는다.

        시간대 분포만으로는 확신하지 않는다 — '이 시간에 자주 쓰는 앱'은
        '지금 이 앱 다음에 쓸 앱'과 다른 질문이다."""
        p = self.predict()
        if not p or p[0][1] < min_p:
            return None
        if getattr(self, "_last_tsum", 0) < self.MIN_TRANS:
            return None
        return p[0]

    def stats(self):
        with self._lk:
            return {"transitions": len(self._trans), "switches": self._total,
                    "current": self._cur}

    def reset(self):
        with self._lk:
            self._trans = {}; self._hour = {}; self._total = 0
        try:
            if self._path.exists():
                self._path.unlink()
        except Exception as _dx:
            DIAG.q("UsagePredictor.reset#0", _dx)

    def save(self, force=False):
        now = time.time()
        with self._lk:
            if not force and now - self._last_save < self.SAVE_MIN_S:
                return
            self._last_save = now
            data = {"t": self._trans, "h": self._hour, "n": self._total}
        try:
            self._dir.mkdir(parents=True, exist_ok=True)
            tmp = self._path.with_suffix(".tmp")
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f)
            os.replace(str(tmp), str(self._path))
        except Exception as _dx:
            DIAG.q("UsagePredictor.save#0", _dx)

    def load(self):
        try:
            if not self._path.exists():
                return
            with open(self._path, "r", encoding="utf-8") as f:
                d = json.load(f)
            with self._lk:
                self._trans = {str(k): int(v) for k, v in (d.get("t") or {}).items()}
                self._hour = {str(k): int(v) for k, v in (d.get("h") or {}).items()}
                self._total = int(d.get("n") or 0)
        except Exception as _dx:
            DIAG.q("UsagePredictor.load#0", _dx)


PREDICT = UsagePredictor()


# ============================================================================
# SAFETY GUARD
# ============================================================================
class SafetyGuard:
    def __init__(self):
        self.rollback_log = deque(maxlen=200)
        self.violations = 0

    def check_pid(self, pid):
        if not pid: return False, "no PID"
        try:
            p = psutil.Process(pid)
            name = p.name().lower()
            if name in SYSTEM_WHITELIST:
                return False, f"system: {name}"
            if any(k in name for k in SAFE_KEYWORDS):
                return False, f"protected: {name}"
            return True, "OK"
        except Exception as e:
            return False, str(e)

    def record(self, action, target, restore_fn=None):
        self.rollback_log.append({
            "ts": time.time(), "action": action,
            "target": target, "restore_fn": restore_fn,
        })

    def rollback_all(self):
        n = 0
        while self.rollback_log:
            entry = self.rollback_log.popleft()
            fn = entry.get("restore_fn")
            if fn:
                try: fn(); n += 1
                except Exception as _dx: DIAG.q("SafetyGuard.rollback_all#0", _dx)
        return n


# ============================================================================
# LATENCY OPTIMIZER (Burst executor for Auto loop)
# ============================================================================
class LatencyOptimizer:
    PROCESS_ALL  = 0x1F0FFF
    THREAD_SET   = 0x0020
    THREAD_QUERY = 0x0040
    TH_HIGHEST   = 2
    TH_ABOVE     = 1
    TH_NORMAL    = 0
    # ★수정★ 한 프로세스의 '모든' 스레드를 HIGHEST 로 올리면
    # (1) 프로세스 내부 상대 우선순위(오디오/렌더/워커 설계)가 뭉개지고
    # (2) 워커 스레드가 UI/입력 스레드를 밀어내 오히려 끊김이 생긴다.
    # 상위 N개만, 한 단계(ABOVE_NORMAL)만 올린다.
    MAX_BOOST_THREADS = 8
    IO_LOW       = 1
    IO_NORMAL    = 2
    IO_HIGH      = 3

    def __init__(self, guard):
        self.guard = guard
        self.k = kernel32; self.nt = ntdll; self.psapi = psapi
        try: self.mm = ctypes.windll.winmm
        except Exception: self.mm = None
        self._timer_active = False
        self._logical = psutil.cpu_count(logical=True) or 1
        # ★수정★ EcoQoS 장부를 전역 ECO 하나로 합쳤다. 예전엔 이 클래스와
        # CoreMode 가 각각 장부를 들고 있어서, 알트탭 때 포그라운드 트리를
        # 풀어주는 코드가 이쪽 장부를 못 봤다 — Auto 루프가 걸어둔
        # 크롬 렌더러·디스코드 헬퍼가 영영 저클럭에 묶인 직접 원인.
        self._ecoqos_pids = ECO

    # ★전면 재작성★ 기존 thread_burst 의 근본 문제: 듀티 사이클 3.75%
    #
    # BURST_INPUT_MS 는 150ms 인데 호출 주기는 3000~4000ms 였다. 즉 96%
    # 의 시간 동안 아무 효과가 없다. 그 3.75% 를 위해 매 사이클마다
    # 스레드 전체 열거 + 핸들 8개 오픈 + Timer 스레드 1개 생성을 했다.
    # 비용은 100% 내고 효과는 4% 만 받는 전형적인 플라세보였다.
    #
    # 새 방식: 포그라운드가 '바뀔 때만' 손대고, 바뀌기 전까지 유지한다.
    #   (1) 프로세스 우선순위 클래스를 ABOVE_NORMAL 로 (지속)
    #   (2) 같은 pid 가 계속 포그라운드면 아무 API 도 호출하지 않음(0 비용)
    #   (3) 포그라운드가 바뀌면 직전 앱을 원래 클래스로 복구
    # HIGH_PRIORITY_CLASS 는 쓰지 않는다 — 입력/오디오 스레드보다 위로
    # 올라가면 오히려 시스템 전체가 불안정해진다.
    ABOVE_NORMAL_CLASS = 0x00008000

    def thread_burst(self, fg_pid):
        ok, reason = self.guard.check_pid(fg_pid)
        if not ok:
            self._release_fg_boost()
            return f"Skipped: {reason}"

        if getattr(self, "_fg_boost_pid", None) == fg_pid:
            return "Foreground boost active (kept)"   # API 호출 0회

        self._release_fg_boost()      # 직전 포그라운드 복구

        prev = None
        try:
            p = psutil.Process(fg_pid)
            prev = p.nice()
            if prev in (psutil.NORMAL_PRIORITY_CLASS,
                        psutil.BELOW_NORMAL_PRIORITY_CLASS,
                        psutil.IDLE_PRIORITY_CLASS):
                p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
                self._fg_boost_pid = fg_pid
                self._fg_boost_prev = prev
                self.guard.record("fg_boost", str(fg_pid),
                                  self._release_fg_boost)
                return "Foreground → ABOVE_NORMAL"
            # 이미 높은 앱(게임이 스스로 올린 경우)은 건드리지 않는다.
            return "Already elevated (no change)"
        except Exception as e:
            return f"Skipped: {e}"

    def _release_fg_boost(self):
        pid = getattr(self, "_fg_boost_pid", None)
        if not pid: return
        prev = getattr(self, "_fg_boost_prev", psutil.NORMAL_PRIORITY_CLASS)
        self._fg_boost_pid = None
        self._fg_boost_prev = None
        try: psutil.Process(pid).nice(prev)
        except Exception as _dx: DIAG.q("LatencyOptimizer._release_fg_boost#0", _dx)

    # ★수정★ 기존엔 매 사이클(3~4초) 호출되면서 1.5초 뒤 원복했다.
    # 즉 포그라운드 앱의 IO 우선순위가 High↔Normal 로 계속 진동하고,
    # 백그라운드 상위 5개도 Low↔Normal 을 반복했다. IO 우선순위는 큐
    # 재정렬에 쓰이는 값이라 이렇게 흔들면 이득이 상쇄될 뿐 아니라,
    # 그 판정을 위해 프로세스 워크를 매번 다시 돌았다.
    # → 같은 포그라운드가 유지되는 동안 20초에 한 번만 재적용한다.
    IO_REAPPLY_S = 20.0

    def io_priority_boost(self, fg_pid):
        ok, reason = self.guard.check_pid(fg_pid)
        if not ok: return f"Skipped: {reason}"
        now = time.monotonic()
        if (getattr(self, "_io_fg_pid", None) == fg_pid and
                now - getattr(self, "_io_t", 0.0) < self.IO_REAPPLY_S):
            return "IO priority kept (no reapply)"
        self._io_fg_pid = fg_pid
        self._io_t = now
        try:
            h = _open_proc(fg_pid, ACC_SET_PRIORITY)
            if h:
                v = ctypes.c_ulong(self.IO_HIGH)
                self.nt.NtSetInformationProcess(h, 33, ctypes.byref(v),
                                                ctypes.sizeof(v))
                _close(h)
        except Exception as _dx: DIAG.q("LatencyOptimizer.io_priority_boost#0", _dx)
        lowered = 0
        lowered_pids = []   # ★수정★ 낮춘 대상을 기억해야 되돌릴 수 있다
        try:
            # ★수정(남아있던 최대 비용원)★
            # 기존: process_iter(["pid","name","io_counters"]).
            # io_counters 는 _GlobalProcCache._FULL_ATTRS 에 없어서 몽키패치
            # 조건을 통과하지 못하고 매번 '원본' process_iter 로 떨어졌다.
            # 즉 전체 프로세스를 다시 걷고, 프로세스마다 핸들을 열어 IO
            # 카운터를 조회했다. Hard 모드는 모든 프로필 분기에서 이걸 매
            # 사이클(4초) 호출한다 → 캐시를 만들어둔 의미가 없었다.
            # 이제 캐시된 목록에서 후보를 먼저 좁히고(메모리/상태 기준),
            # 그 소수에 대해서만 io_counters 를 조회한다.
            cands = []
            for inf in PROC_CACHE.info_list():
                pid = inf.get("pid")
                if not is_target(pid, inf.get("name") or ""): continue
                if inf.get("status") == "stopped": continue
                mi = inf.get("memory_info")
                rss = mi.rss if mi else 0
                cands.append((rss, pid))
            cands.sort(reverse=True)
            procs = []
            for _, pid in cands[:24]:      # 상위 24개만 실측
                try:
                    io = psutil.Process(pid).io_counters()
                    procs.append((io.read_bytes + io.write_bytes, pid))
                except Exception as _dx: DIAG.q("LatencyOptimizer.io_priority_boost#1", _dx)
            procs.sort(reverse=True)
            for _, pid in procs[:5]:
                try:
                    h = _open_proc(pid, ACC_SET_PRIORITY)
                    if h:
                        v = ctypes.c_ulong(self.IO_LOW)
                        self.nt.NtSetInformationProcess(
                            h, 33, ctypes.byref(v), ctypes.sizeof(v))
                        _close(h)
                        lowered += 1; lowered_pids.append(pid)
                except Exception as _dx: DIAG.q("LatencyOptimizer.io_priority_boost#2", _dx)
        except Exception as _dx: DIAG.q("LatencyOptimizer.io_priority_boost#3", _dx)
        done = [False]
        def restore():
            if done[0]: return
            done[0] = True
            try:
                h = _open_proc(fg_pid, ACC_SET_PRIORITY)
                if h:
                    v = ctypes.c_ulong(self.IO_NORMAL)
                    self.nt.NtSetInformationProcess(
                        h, 33, ctypes.byref(v), ctypes.sizeof(v))
                    _close(h)
            except Exception as _dx: DIAG.q("LatencyOptimizer.restore#0", _dx)
            # 낮춰둔 백그라운드 IO 우선순위도 반드시 되돌린다.
            for pid in lowered_pids:
                try:
                    h2 = _open_proc(pid, ACC_SET_PRIORITY)
                    if h2:
                        v2 = ctypes.c_ulong(self.IO_NORMAL)
                        self.nt.NtSetInformationProcess(
                            h2, 33, ctypes.byref(v2), ctypes.sizeof(v2))
                        _close(h2)
                except Exception as _dx: DIAG.q("LatencyOptimizer.restore#1", _dx)
            lowered_pids.clear()
        SCHED.call_later(BURST_IO_MS/1000.0, restore)
        self.guard.record("io_priority", str(fg_pid), restore)
        return f"FG IO->High, {lowered} BG->Low"

    def mmcss_register(self, fg_pid, fg_type):
        """★비활성 — 원래부터 효과가 0이었던 코드★

        AvSetMmThreadCharacteristicsW 는 '호출한 스레드'를 MMCSS 에
        등록하는 API 다. 인자로 프로세스나 pid 를 받지 않는다. 즉 기존
        코드는 게임이 아니라 OMEGA X 자신의 워커 스레드를 'Games' 태스크로
        등록하고 있었다. 대상 게임에는 아무 일도 일어나지 않는다.

        더 나쁜 건 복구 경로였다. 등록은 워커 스레드에서 하고
        AvRevertMmThreadCharacteristics 는 1.5초 뒤 threading.Timer 의
        '다른 스레드'에서 호출했다. MMCSS 핸들은 스레드에 묶여 있어서
        다른 스레드에서의 Revert 는 미정의 동작이고, 실패하면 MMCSS
        등록이 누수된 채 남는다.

        외부 프로세스를 MMCSS 에 등록하는 공개 API 는 존재하지 않는다.
        게임의 프레임 안정성에 실제로 기여하는 건 GPU 큐 우선순위
        (ModernOptimizer.gpu_priority_boost)와 백그라운드 정리 쪽이므로,
        여기서는 거짓 성공 문자열을 돌려주지 않고 정직하게 no-op 한다.
        """
        return "N/A (cannot register MMCSS for external process)"

    def bg_throttle(self, fg_pid):
        throttled = []; original = {}
        try:
            for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
                try:
                    info = p.info; pid = info["pid"]
                    if pid == fg_pid: continue
                    # ★수정★ is_safe_to_modify → is_target
                    # (포그라운드 프로세스 트리·자기 자신·안티치트 제외)
                    if not is_target(pid, info.get("name") or ""): continue
                    if info.get("cpu_percent", 0) < 1.0: continue
                    cur_nice = p.nice()
                    # ★수정★ 이미 낮은 프로세스를 다시 잡으면 '원래값'이
                    # BELOW_NORMAL 로 오염돼 복구해도 안 돌아온다.
                    if cur_nice == psutil.BELOW_NORMAL_PRIORITY_CLASS: continue
                    original[pid] = cur_nice
                    p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
                    throttled.append(pid)
                    if len(throttled) >= 8: break
                except Exception as _dx: DIAG.q("LatencyOptimizer.bg_throttle#0", _dx)
        except Exception as _dx: DIAG.q("LatencyOptimizer.bg_throttle#1", _dx)
        done = [False]
        def restore():
            if done[0]: return
            done[0] = True
            for pid in throttled:
                try:
                    psutil.Process(pid).nice(
                        original.get(pid, psutil.NORMAL_PRIORITY_CLASS))
                except Exception as _dx: DIAG.q("LatencyOptimizer.restore#2", _dx)
        if throttled:
            SCHED.call_later(BURST_THROTTLE_MS/1000.0, restore)
            self.guard.record("bg_throttle", "multi", restore)
        return f"Throttled {len(throttled)} BG"

    def affinity_hint(self, fg_pid):
        """★비활성★ 하이브리드 CPU 에서 성능을 확실히 깎던 동작.

        기존 구현은 포그라운드 프로세스의 '모든' 스레드에
        SetThreadIdealProcessor(h, 0) 을 걸어 전부 코어 0 을 선호하게 만들었다.
        결과: 12~24 스레드가 한 코어에 몰려 스케줄러가 매번 밀어내기를
        반복 → 프레임 드랍/입력 지연. P-코어를 골라 분산하지 않는 한
        이 힌트는 이득이 없으므로 no-op 로 둔다.
        (원본 코드는 아래 주석으로 보존)
        """
        return "Disabled (was pinning all threads to core 0)"
        # --- 원본 보존 (사용 금지) ---------------------------------
        # if not IS_HYBRID: return "Skipped"
        # ok, reason = self.guard.check_pid(fg_pid)
        # if not ok: return f"Skipped: {reason}"
        # n = 0
        # try:
        #     for t in psutil.Process(fg_pid).threads():
        #         h = self.k.OpenThread(self.THREAD_SET | self.THREAD_QUERY,
        #                               False, t.id)
        #         if h:
        #             self.k.SetThreadIdealProcessor(h, 0)
        #             self.k.CloseHandle(h); n += 1
        # except Exception: pass
        # return f"Hinted {n} threads"

    def timer_burst(self):
        """★수정★ timeBeginPeriod 참조계수 누수 차단.

        기존: 사이클마다 timeBeginPeriod(1) 을 다시 호출하는데 복구는
        _timer_active 플래그 하나로만 판단 → 앞 호출의 restore 가 플래그를
        내리면 뒤 호출의 restore 는 아무것도 안 함. 결과적으로 시스템 타이머
        해상도가 1ms 에 영구히 고정되어(참조계수가 안 내려감) 유휴 전력·
        C-state 진입이 망가지고 노트북 배터리·발열이 악화된다.
        이제 이미 활성이면 재호출하지 않고, 정확히 1:1 로만 짝을 맞춘다.
        """
        if not self.mm: return "winmm N/A"
        if not hasattr(self, "_timer_lk"):
            self._timer_lk = threading.Lock()
        with self._timer_lk:
            if self._timer_active:
                return "Timer 1ms (already active)"
            try:
                r = self.mm.timeBeginPeriod(1)
            except Exception:
                return "Timer error"
            if r != 0:
                return "Timer denied"
            self._timer_active = True

        done = [False]
        def restore():
            if done[0]: return
            done[0] = True
            with self._timer_lk:
                if not self._timer_active: return
                try: self.mm.timeEndPeriod(1)
                except Exception as _dx: DIAG.q("LatencyOptimizer.restore#3", _dx)
                self._timer_active = False

        SCHED.call_later(BURST_TIMER_MS/1000.0, restore)
        self.guard.record("timer_burst", "system", restore)
        return "Timer 1ms"

    def apply_ecoqos(self, fg_pid):
        if not IS_WIN11_22H2: return "Needs Win11 22H2+"
        class PTS(ctypes.Structure):
            _fields_ = [("Version", ctypes.c_ulong),
                       ("ControlMask", ctypes.c_ulong),
                       ("StateMask", ctypes.c_ulong)]
        applied = 0
        # ★패치23★ 포그라운드 '트리 전체' 를 먼저 해제한다.
        # 예전엔 아래 fg_pid 한 줄뿐이었다. 크롬·일렉트론·게임은
        # 실제 일을 자식 프로세스가 하므로 본체만 풀어봐야 소용없다.
        try:
            FG.refresh(fg_pid, None)
        except Exception as _dx: DIAG.q("LatencyOptimizer.apply_ecoqos#0", _dx)
        release_fg_ecoqos()
        # 포그라운드로 승격된 프로세스는 즉시 해제
        if fg_pid and fg_pid in self._ecoqos_pids:
            self._set_ecoqos_state(PTS, fg_pid, False)
            self._ecoqos_pids.discard(fg_pid)
        try:
            for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
                try:
                    info = p.info; pid = info["pid"]
                    if pid == fg_pid: continue
                    if pid in self._ecoqos_pids: continue   # ★수정★ 중복 적용 방지
                    if not is_target(pid, info.get("name") or ""): continue
                    if info.get("cpu_percent", 0) < 0.5: continue
                    if self._set_ecoqos_state(PTS, pid, True):
                        applied += 1
                        self._ecoqos_pids.add(pid)
                    if applied >= 10: break
                except Exception as _dx: DIAG.q("LatencyOptimizer.apply_ecoqos#1", _dx)
        except Exception as _dx: DIAG.q("LatencyOptimizer.apply_ecoqos#2", _dx)
        if applied:
            # 앱 종료/롤백 시 반드시 풀리도록 등록
            self.guard.record("ecoqos", "multi", self.revert_ecoqos_all)
        return f"EcoQoS: {applied}"

    def _set_ecoqos_state(self, PTS, pid, enable):
        """EcoQoS on/off — 실제 처리는 전역 장부(ECO)가 한다.

        ★해제는 ControlMask=0 / StateMask=0★ 이어야 한다. 예전 코드처럼
        ControlMask=1 / StateMask=0 으로 두면 '기본값 복귀'가 아니라
        '영구 절전 금지'가 되어, Windows 가 알아서 절전시켰어야 할
        프로세스까지 고성능에 묶인다(발열·전력이 오히려 는다).
        """
        if enable:
            return ECO.apply(pid)
        return ECO.release(pid)

    def revert_ecoqos_all(self):
        """걸어둔 EcoQoS 를 전부 해제한다(모드 종료·앱 종료 시)."""
        return ECO.release_all()
    def idle_cleanup(self):
        vm = psutil.virtual_memory()
        if vm.percent < RAM_WARN: return f"RAM {vm.percent:.0f}% - skip"
        cleaned = 0
        for p in psutil.process_iter(["pid", "name", "cpu_percent",
                                      "memory_percent", "status"]):
            try:
                info = p.info
                name = (info.get("name") or "").lower()
                if not is_target(info.get("pid"), name): continue
                # ★수정★ status=="sleeping" 은 Windows 에서 절대 참이 아니다.
                if not proc_is_idle(info, 0.1): continue
                if info.get("memory_percent", 0) < 1.5: continue
                if info.get("cpu_percent", 0) > 0.1: continue
                h = _open_proc(info["pid"], ACC_TRIM_WS)
                if h:
                    self.psapi.EmptyWorkingSet(h)
                    _close(h); cleaned += 1
                if cleaned >= 5: break
            except Exception as _dx: DIAG.q("LatencyOptimizer.idle_cleanup#0", _dx)
        return f"Trimmed {cleaned}"

    def execute(self, action, fg_pid, fg_type):
        if action == "thread_burst":   return self.thread_burst(fg_pid)
        elif action == "io_priority":  return self.io_priority_boost(fg_pid)
        elif action == "mmcss":        return self.mmcss_register(fg_pid, fg_type)
        elif action == "bg_throttle":  return self.bg_throttle(fg_pid)
        elif action == "timer_burst":  return self.timer_burst()
        elif action == "ecoqos":       return self.apply_ecoqos(fg_pid)
        elif action == "idle_cleanup": return self.idle_cleanup()
        elif action == "affinity":     return self.affinity_hint(fg_pid)
        return f"Unknown"


# ============================================================================
# MODERN OPTIMIZER — Windows 10 1607+ / 11 22H2+ 전용 신형 API 묶음
# ============================================================================
# 여기 들어있는 기법은 전부 '커널에게 힌트를 주는' 방식이다. 강제 핀 고정·
# 워킹셋 강제 축출처럼 스케줄러/메모리 관리자와 싸우는 방식이 아니라,
# 커널이 이미 하고 있는 판단에 우선순위 정보를 얹어준다. 그래서
# (1) 부작용이 작고 (2) 되돌리기가 확실하며 (3) 실제로 효과가 남는다.
#
#  1) CPU Sets (SetProcessDefaultCpuSets)
#     하이브리드 CPU 에서 포그라운드 앱은 P코어, 백그라운드는 E코어를
#     '선호'하게 만든다. 어피니티 마스크와 달리 소프트 힌트라 부하가 몰리면
#     커널이 알아서 무시한다 → 코어0 몰림 같은 사고가 원천적으로 없다.
#     구 affinity_hint 의 정식 대체품(Win10 1607+).
#
#  2) Memory Priority (ProcessMemoryPriorityInformation)
#     EmptyWorkingSet 처럼 페이지를 강제로 밀어내는 대신, 백그라운드
#     프로세스의 '메모리 우선순위'를 낮춰둔다. 메모리가 실제로 부족해질 때
#     커널이 알아서 그쪽 페이지부터 회수한다. 하드 폴트 폭증 없이 같은
#     목적을 달성하는, 훨씬 안전하고 효과가 지속되는 방식.
#
#  3) Timer Resolution 하이재킹 차단 (Win11)
#     PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION. 브라우저·런처·
#     채팅앱이 제멋대로 timeBeginPeriod(1) 을 걸어 시스템 전체 타이머를
#     1ms 로 끌어내리는 것을 프로세스 단위로 무시한다. 유휴 전력·발열·
#     C-state 진입에 직접 효과가 있고, 노트북에서 체감이 크다.
#
#  4) GPU 스케줄링 우선순위 (D3DKMTSetProcessSchedulingPriorityClass)
#     게임/렌더 프로세스의 GPU 큐 우선순위를 한 단계 올린다. 다른 앱이
#     GPU 를 같이 쓸 때 프레임타임 편차가 줄어든다.
#
#  5) 자기 자신 절전 (Self EcoQoS)
#     최적화 도구가 정작 자기 CPU 를 먹으면 의미가 없다. 창이 최소화되면
#     OMEGA X 자신에게 EcoQoS 를 걸어 E코어/저클럭으로 내려간다.
# ============================================================================
class ModernOptimizer:
    # SetProcessInformation class ids
    PROC_MEMORY_PRIORITY   = 0
    PROC_POWER_THROTTLING  = 4

    # MEMORY_PRIORITY_*
    MEM_VERY_LOW      = 1
    MEM_LOW           = 2
    MEM_MEDIUM        = 3
    MEM_BELOW_NORMAL  = 4
    MEM_NORMAL        = 5

    # PROCESS_POWER_THROTTLING_*
    THROTTLE_EXECUTION_SPEED      = 0x1
    THROTTLE_IGNORE_TIMER_RES     = 0x4   # Win11+

    PROCESS_SET_INFORMATION       = 0x0200
    PROCESS_QUERY_LIMITED_INFO    = 0x1000
    PROCESS_ALL                   = 0x1F0FFF

    class MEMORY_PRIORITY_INFORMATION(ctypes.Structure):
        _fields_ = [("MemoryPriority", wintypes.ULONG)]

    class PROCESS_POWER_THROTTLING_STATE(ctypes.Structure):
        _fields_ = [("Version",     wintypes.ULONG),
                    ("ControlMask", wintypes.ULONG),
                    ("StateMask",   wintypes.ULONG)]

    def __init__(self, guard):
        self.guard = guard
        self.k = kernel32
        # 기능 가용성 — 없으면 조용히 no-op
        self.has_cpu_sets = bool(IS_HYBRID) and hasattr(
            self.k, "SetProcessDefaultCpuSets")
        self.has_mem_prio = hasattr(self.k, "SetProcessInformation")
        self.has_timer_guard = IS_WIN11 and hasattr(
            self.k, "SetProcessInformation")
        try:
            self._gdi = ctypes.windll.gdi32
            self.has_gpu_prio = hasattr(
                self._gdi, "D3DKMTSetProcessSchedulingPriorityClass")
        except Exception:
            self._gdi = None
            self.has_gpu_prio = False

        # 되돌리기용 상태
        self._cpuset_pids = set()     # DefaultCpuSets 를 지정한 pid
        self._memprio_pids = set()    # 메모리 우선순위를 낮춘 pid
        self._timerguard_pids = set() # 타이머 하이재킹 차단을 건 pid
        self._gpu_pids = {}           # pid -> 이전 GPU 우선순위
        self._self_eco = False
        self._lk = threading.Lock()

    # ── 내부 유틸 ─────────────────────────────────────────────
    def _open(self, pid, access=None):
        try:
            return self.k.OpenProcess(
                access if access is not None else
                (self.PROCESS_SET_INFORMATION | self.PROCESS_QUERY_LIMITED_INFO),
                False, pid)
        except Exception:
            return None

    # ── 1) CPU Sets ───────────────────────────────────────────
    def set_cpu_set_preference(self, pid, want="p"):
        """pid 가 선호할 코어 그룹 지정. want: 'p' | 'e' | None(해제)."""
        if not self.has_cpu_sets or not pid:
            return False
        ids = None
        if want == "p":   ids = P_CORE_SETS
        elif want == "e": ids = E_CORE_SETS
        h = self._open(pid)
        if not h:
            return False
        try:
            if ids:
                arr = (wintypes.ULONG * len(ids))(*ids)
                ok = self.k.SetProcessDefaultCpuSets(h, arr, len(ids))
            else:
                ok = self.k.SetProcessDefaultCpuSets(h, None, 0)
            if ok:
                with self._lk:
                    if ids: self._cpuset_pids.add(pid)
                    else:   self._cpuset_pids.discard(pid)
            return bool(ok)
        except Exception:
            return False
        finally:
            try: self.k.CloseHandle(h)
            except Exception as _dx: DIAG.q("ModernOptimizer.set_cpu_set_preference#0", _dx)

    def apply_core_split(self, fg_pid, max_bg=20):
        """포그라운드 → P코어 선호, 무거운 백그라운드 → E코어 선호."""
        if not self.has_cpu_sets:
            return "CPU Sets N/A (non-hybrid)"
        moved = 0
        if fg_pid and self.set_cpu_set_preference(fg_pid, "p"):
            moved += 1
        for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
            if moved > max_bg: break
            try:
                info = p.info; pid = info["pid"]
                if pid == fg_pid: continue
                if pid in self._cpuset_pids: continue
                if not is_target(pid, info.get("name") or ""): continue
                if (info.get("cpu_percent", 0) or 0) < 0.5: continue
                if self.set_cpu_set_preference(pid, "e"):
                    moved += 1
            except Exception as _dx: DIAG.q("ModernOptimizer.apply_core_split#0", _dx)
        if moved:
            self.guard.record("cpu_sets", "multi", self.revert_cpu_sets)
        return f"P/E core split: {moved} processes"

    def revert_cpu_sets(self):
        n = 0
        for pid in list(self._cpuset_pids):
            h = self._open(pid)
            if not h:
                self._cpuset_pids.discard(pid); continue
            try:
                if self.k.SetProcessDefaultCpuSets(h, None, 0): n += 1
            except Exception as _dx: DIAG.q("ModernOptimizer.revert_cpu_sets#0", _dx)
            finally:
                try: self.k.CloseHandle(h)
                except Exception as _dx: DIAG.q("ModernOptimizer.revert_cpu_sets#1", _dx)
            self._cpuset_pids.discard(pid)
        return n

    # ── 2) Memory Priority ────────────────────────────────────
    def set_memory_priority(self, pid, level):
        if not self.has_mem_prio or not pid:
            return False
        h = self._open(pid)
        if not h:
            return False
        try:
            mpi = ModernOptimizer.MEMORY_PRIORITY_INFORMATION()
            mpi.MemoryPriority = level
            ok = self.k.SetProcessInformation(
                h, self.PROC_MEMORY_PRIORITY,
                ctypes.byref(mpi), ctypes.sizeof(mpi))
            return bool(ok)
        except Exception:
            return False
        finally:
            try: self.k.CloseHandle(h)
            except Exception as _dx: DIAG.q("ModernOptimizer.set_memory_priority#0", _dx)

    def lower_bg_memory_priority(self, fg_pid, max_count=25):
        """백그라운드 프로세스 메모리 우선순위 하향.

        EmptyWorkingSet 의 안전한 대체재. 페이지를 지금 당장 뺏지 않고,
        '메모리가 부족해지면 이쪽부터 회수하라'고 커널에 표시만 한다.
        하드 폴트 폭증이 없고 효과는 계속 유지된다.
        """
        if not self.has_mem_prio:
            return "Memory priority N/A"
        n = 0
        # 포그라운드는 항상 정상 우선순위로 되돌린다
        if fg_pid and fg_pid in self._memprio_pids:
            self.set_memory_priority(fg_pid, self.MEM_NORMAL)
            self._memprio_pids.discard(fg_pid)
        for p in psutil.process_iter(["pid", "name", "memory_info", "status"]):
            if n >= max_count: break
            try:
                info = p.info; pid = info["pid"]
                if pid == fg_pid: continue
                if pid in self._memprio_pids: continue
                if not is_target(pid, info.get("name") or ""): continue
                mi = info.get("memory_info")
                if not mi or mi.rss < 40 * 1024 * 1024: continue
                # ★수정★ Windows 에는 'sleeping' 상태가 없어 이 액션은
                # 지금까지 항상 0개를 처리했다.
                if not proc_is_idle(info, 0.5): continue
                if self.set_memory_priority(pid, self.MEM_BELOW_NORMAL):
                    self._memprio_pids.add(pid); n += 1
            except Exception as _dx: DIAG.q("ModernOptimizer.lower_bg_memory_priority#0", _dx)
        if n:
            self.guard.record("mem_priority", "multi",
                              self.revert_memory_priority)
        return f"Memory priority lowered: {n} processes"

    def revert_memory_priority(self):
        n = 0
        for pid in list(self._memprio_pids):
            if self.set_memory_priority(pid, self.MEM_NORMAL): n += 1
            self._memprio_pids.discard(pid)
        return n

    # ── 3) Timer resolution 하이재킹 차단 ──────────────────────
    def _set_power_throttle(self, pid, control, state):
        h = self._open(pid)
        if not h:
            return False
        try:
            st = ModernOptimizer.PROCESS_POWER_THROTTLING_STATE()
            st.Version = 1
            st.ControlMask = control
            st.StateMask = state
            ok = self.k.SetProcessInformation(
                h, self.PROC_POWER_THROTTLING,
                ctypes.byref(st), ctypes.sizeof(st))
            return bool(ok)
        except Exception:
            return False
        finally:
            try: self.k.CloseHandle(h)
            except Exception as _dx: DIAG.q("ModernOptimizer._set_power_throttle#0", _dx)

    def block_timer_hijack(self, fg_pid, max_count=25):
        """백그라운드 앱이 시스템 타이머 해상도를 끌어내리지 못하게 한다."""
        if not self.has_timer_guard:
            return "Win11 required"
        n = 0
        for p in psutil.process_iter(["pid", "name"]):
            if n >= max_count: break
            try:
                info = p.info; pid = info["pid"]
                if pid == fg_pid: continue
                if pid in self._timerguard_pids: continue
                if not is_target(pid, info.get("name") or ""): continue
                if self._set_power_throttle(pid,
                                            self.THROTTLE_IGNORE_TIMER_RES,
                                            self.THROTTLE_IGNORE_TIMER_RES):
                    self._timerguard_pids.add(pid); n += 1
            except Exception as _dx: DIAG.q("ModernOptimizer.block_timer_hijack#0", _dx)
        if n:
            self.guard.record("timer_guard", "multi", self.revert_timer_hijack)
        return f"Timer hijack blocked: {n} processes"

    def revert_timer_hijack(self):
        n = 0
        for pid in list(self._timerguard_pids):
            # ControlMask 만 남기고 StateMask 0 → 시스템 기본 동작 복귀
            if self._set_power_throttle(pid,
                                        self.THROTTLE_IGNORE_TIMER_RES, 0):
                n += 1
            self._timerguard_pids.discard(pid)
        return n

    # ── 4) GPU 스케줄링 우선순위 ───────────────────────────────
    def gpu_priority_boost(self, fg_pid, level=3):
        """D3DKMT 로 GPU 큐 우선순위 상향. level 3 = ABOVE_NORMAL.

        4(HIGH) 이상은 컴포지터(dwm)와 경합할 수 있어 쓰지 않는다.
        """
        if not self.has_gpu_prio or not fg_pid:
            return "GPU priority N/A"
        if fg_pid in self._gpu_pids:
            return "Already applied"
        ok, reason = self.guard.check_pid(fg_pid)
        if not ok:
            return f"Skipped: {reason}"
        h = self._open(fg_pid, ACC_GPU_PRIO)
        if not h:
            return "Handle failed"
        try:
            prev = ctypes.c_int(2)   # NORMAL 기본값
            try:
                self._gdi.D3DKMTGetProcessSchedulingPriorityClass(
                    h, ctypes.byref(prev))
            except Exception as _dx:
                DIAG.q("ModernOptimizer.gpu_priority_boost#0", _dx)
            r = self._gdi.D3DKMTSetProcessSchedulingPriorityClass(
                h, ctypes.c_int(level))
            if r == 0:
                self._gpu_pids[fg_pid] = prev.value
                self.guard.record("gpu_priority", str(fg_pid),
                                  self.revert_gpu_priority)
                return "GPU priority raised"
            return "GPU priority denied"
        except Exception:
            return "GPU priority error"
        finally:
            try: self.k.CloseHandle(h)
            except Exception as _dx: DIAG.q("ModernOptimizer.gpu_priority_boost#1", _dx)

    def revert_gpu_priority(self):
        if not self.has_gpu_prio:
            return 0
        n = 0
        for pid, prev in list(self._gpu_pids.items()):
            h = self._open(pid, ACC_GPU_PRIO)
            if h:
                try:
                    if self._gdi.D3DKMTSetProcessSchedulingPriorityClass(
                            h, ctypes.c_int(prev)) == 0:
                        n += 1
                except Exception as _dx: DIAG.q("ModernOptimizer.revert_gpu_priority#0", _dx)
                finally:
                    try: self.k.CloseHandle(h)
                    except Exception as _dx: DIAG.q("ModernOptimizer.revert_gpu_priority#1", _dx)
            self._gpu_pids.pop(pid, None)
        return n

    # ── 5) 자기 자신 절전 ──────────────────────────────────────
    def set_self_efficiency(self, on: bool):
        """창이 최소화되면 OMEGA X 자신을 절전 모드로 내린다."""
        if not IS_WIN11_22H2 or self._self_eco == on:
            return False
        try:
            h = ctypes.c_void_p(-1)      # GetCurrentProcess 의사 핸들
            st = ModernOptimizer.PROCESS_POWER_THROTTLING_STATE()
            st.Version = 1
            st.ControlMask = self.THROTTLE_EXECUTION_SPEED
            st.StateMask = self.THROTTLE_EXECUTION_SPEED if on else 0
            ok = self.k.SetProcessInformation(
                h, self.PROC_POWER_THROTTLING,
                ctypes.byref(st), ctypes.sizeof(st))
            if ok:
                self._self_eco = on
            return bool(ok)
        except Exception:
            return False

    # ── 전체 되돌리기 ─────────────────────────────────────────
    def revert_all(self):
        out = 0
        for fn in (self.revert_cpu_sets, self.revert_memory_priority,
                   self.revert_timer_hijack, self.revert_gpu_priority):
            try: out += (fn() or 0)
            except Exception as _dx: DIAG.q("ModernOptimizer.revert_all#0", _dx)
        try: self.set_self_efficiency(False)
        except Exception as _dx: DIAG.q("ModernOptimizer.revert_all#1", _dx)
        return out

    def release_pids(self, pids):
        """★신규★ 지정한 pid 집합에 걸린 강등을 즉시 전부 해제.

        포그라운드가 바뀌었을 때 호출한다. 기존에는 백그라운드일 때
        걸어둔 E코어 선호·메모리 우선순위 하향·타이머 가드가 그 앱이
        포그라운드로 올라와도 그대로 남아 있었다. 사용자가 알트탭으로
        돌아온 바로 그 앱이 여전히 E코어에 묶인 채 도는 상태였다.
        """
        n = 0
        for pid in list(pids):
            if pid in self._memprio_pids:
                if self.set_memory_priority(pid, self.MEM_NORMAL): n += 1
                self._memprio_pids.discard(pid)
            if pid in self._cpuset_pids:
                # 백그라운드로 E코어에 묶여 있던 것을 P코어 선호로 전환
                if self.set_cpu_set_preference(pid, "p"): n += 1
            if pid in self._timerguard_pids:
                if self._set_power_throttle(
                        pid, self.THROTTLE_IGNORE_TIMER_RES, 0): n += 1
                self._timerguard_pids.discard(pid)
        return n

    def prune_dead(self):
        """종료된 pid 를 추적 집합에서 제거(재사용 pid 오판 방지)."""
        try:
            alive = set(psutil.pids())
        except Exception:
            return
        self._cpuset_pids &= alive
        self._memprio_pids &= alive
        self._timerguard_pids &= alive
        for pid in list(self._gpu_pids):
            if pid not in alive:
                self._gpu_pids.pop(pid, None)




# ============================================================================
# AI CORE MODE — Lite Core / Hard Core (the headline feature)
# ============================================================================
# ----------------------------------------------------------------------------
# EFFECT ESTIMATOR — 같은 시간대에 대조군을 두는 방식(동시 대조)
# ----------------------------------------------------------------------------
# ★이전 측정 방식이 왜 틀렸나 (설계 결함이지 튜닝 문제가 아니다)★
#
#  (1) 대조군을 '다른 시간'에 쟀다.
#      15사이클마다 최적화를 전부 풀고 1초를 재서 그걸 기준으로 삼았다.
#      그런데 PC 의 백그라운드 부하는 정상 상태가 아니다(non-stationary).
#      1분 사이에 Windows Update 가 깨어나고, 크롬 탭이 타이머를 돌리고,
#      백신이 스캔을 시작한다. 45초 떨어진 두 창을 비교하면 그 차이의
#      대부분은 '우리가 한 일'이 아니라 '그 사이에 일어난 일'이다.
#      표본을 아무리 median 으로 다듬어도 교란 자체는 안 없어진다.
#
#  (2) 그 대조군 측정이 구조적으로 편향돼 있었다.
#      _release_all_soft() 로 60개 프로세스의 EcoQoS 를 풀자마자 1초를
#      쟀다. 억눌려 있던 프로세스들이 밀린 일을 몰아서 처리하는 바로 그
#      구간이다. '껐을 때'가 실제보다 나쁘게 나오도록 만들어진 측정이다.
#      우리에게 유리한 방향의 편향이라 더 나쁘다.
#
#  (3) 잰 것이 사용자가 궁금해하는 것이 아니었다.
#      백그라운드 CPU 코어 수는 체감 반응속도가 아니다. 32스레드 PC 에서
#      백그라운드 0.3코어를 줄여도 게임 프레임은 그대로다.
#
#  (4) 그걸 다시 0~100 점수로 합산했다(PIS). 못 믿을 값 여러 개를
#      평균 내면 못 믿을 값 하나가 될 뿐인데, 화면에는 그럴듯한 점수로
#      보였다. 늘 50 근처(중간)에 머문 건 지표가 고장 났다는 신호였다.
#
# ★이번 방식 — 대조군을 같은 시간대에 둔다★
#   EcoQoS 대상으로 뽑힌 프로세스 중 약 1/CONTROL_EVERY 를 무작위로
#   '비교군'으로 남겨 두고 건드리지 않는다. 그리고 처리군과 비교군의
#   CPU 사용률 변화를 ★같은 창에서★ 비교한다.
#     · Windows Update 가 깨어나면 두 그룹이 같이 올라간다 → 상쇄
#     · 시스템이 조용해지면 두 그룹이 같이 내려간다 → 상쇄
#     · 우리 조치의 효과만 두 그룹의 차이로 남는다
#   같은 프로세스의 전/후를 비교하므로(paired) 프로세스 구성이 바뀌는
#   교란도 들어오지 않는다.
#
#   비용: 백그라운드 앱 몇 개가 절전에서 빠진다. 그게 '측정할 수 있는
#   상태'의 대가다. 측정 못 하는 최적화는 주장일 뿐이다.
#
# ★그래도 못 하는 말★
#   이 값은 "백그라운드 부하를 이만큼 줄였다" 까지다. "PC 가 몇 % 빨라
#   졌다" 는 여전히 말할 수 없고, 말하지 않는다.
# ----------------------------------------------------------------------------
class EffectEstimator:
    CONTROL_EVERY = 7        # 대상 7개 중 1개는 비교군으로 남긴다
    MIN_T = 6                # 처리군 최소 프로세스 수
    MIN_C = 3                # 비교군 최소 프로세스 수
    MIN_DELTA_CORES = 0.002  # 프로세스당 이보다 작은 차이는 무의미
    K_SIGMA = 3.0            # ★패치29★ 데드밴드 = K x 중앙값 표준오차
    _SE_MED = 1.2533         # 중앙값 표준오차의 정규 근사 상수
    BLOCK_S = 60.0           # ★패치23★ 앵커 재설정·그룹 재배정 주기
    KEEP_BLOCKS = 10         # 판정에 쓰는 최근 블록 수(약 10분)

    # ★패치23 — "오래 켜면 무조건 차이 없음" 의 원인★
    # 예전에는 _first 가 pid 당 최초 1회만 기록되고 영원히 고정이었다.
    # 판정식은
    #     per   = median(drops_t) - median(drops_c)      ← 진짜 효과, 상수
    #     noise = MAD(drops_t) + MAD(drops_c)            ← 데드밴드
    #     if abs(per) < noise: "차이 없음"
    # 인데 drops = first - now 이므로, 앵커가 고정이면 시간이 갈수록
    # 각 프로세스의 now 가 몇 시간 전 앵커에서 독립적으로 표류해
    # 두 그룹의 MAD 가 단조 증가한다. per 은 그대로인데 데드밴드만
    # 자라므로 실행 시간이 충분히 길어지면 어떤 진짜 효과도 반드시
    # "차이 없음" 으로 떨어졌다. 처음 몇 분은 판정이 나오다가 오래
    # 켜두면 0 으로 굳는 증상이 정확히 이것이다.
    #
    # 앵커를 블록(90초)마다 새로 잡으면 drops 의 분산이 블록 길이에
    # 묶여 데드밴드가 자라지 않는다. 패치22 ActionLearner v2 가 쓰는
    # 블록 개념과 같은 것이다.

    def __init__(self):
        self._lk = threading.Lock()
        self._n = 0
        self.reset()

    def reset(self):
        with self._lk:
            self._grp = {}      # pid -> "t" | "c"
            self._first = {}    # pid -> 이번 블록 시작 시점 CPU(코어)
            self._now = {}      # pid -> 최근 CPU 사용률(코어)
            self._blocks = deque(maxlen=self.KEEP_BLOCKS)  # 마감된 블록들
            self._block_t = time.monotonic()
            self._phase = 0
            self._flip_out = set()

    # ── 블록 마감 ─────────────────────────────────────────
    def _roll_locked(self, now):
        dt, dc = [], []
        for pid, g in self._grp.items():
            f = self._first.get(pid)
            n = self._now.get(pid)
            if f is None or n is None:
                continue
            # ★패치30★ 라벨이 "c" 라도 EcoQoS 가 실제로 안 풀렸으면
            # 비교군이 아니다. _flip_out 에 남아 있다는 것은 해제
            # 시도가 아직 성공하지 못했다는 뜻이다.
            if g == "c" and pid in self._flip_out:
                continue
            (dt if g == "t" else dc).append(f - n)
        if dt or dc:
            self._blocks.append((dt, dc))
        # (1) 앵커 재설정 — 지금 값이 다음 블록의 기준이다
        self._first = dict(self._now)
        # (2) 그룹 재배정 — 같은 프로세스가 세션 내내 같은 편에 남으면
        #     프로세스별 고정 편향이 그대로 '효과' 로 새어 든다. 예전
        #     assign() 은 pid 당 그룹을 영구 고정했다.
        self._phase += 1
        for i, pid in enumerate(sorted(self._grp)):
            old = self._grp[pid]
            # ★i + 1★ — assign() 의 _n 은 1부터 세고 여기 i 는 0부터 센다.
            # 이 한 칸을 안 맞추면 phase 1(=첫 롤)이 초기 배정과 정확히
            # 겹쳐 그룹이 하나도 안 바뀐다. 첫 블록이 통째로 회전 없이
            # 지나가고, 상수를 조정하면 언제든 다시 물릴 수 있는
            # 우연한 정렬이었다.
            new = "c" if ((i + 1 + self._phase) % self.CONTROL_EVERY == 0) else "t"
            self._grp[pid] = new
            if old == "t" and new == "c":
                # ★실제로 풀어줘야 비교군이 된다★ 장부에만 'c' 라고
                # 적고 EcoQoS 를 안 풀면 그건 비교군이 아니라 그냥
                # 라벨만 바뀐 처리군이다(패치22 캐리오버와 같은 함정).
                self._flip_out.add(pid)
            elif old == "c" and new == "t":
                self._flip_out.discard(pid)
        self._block_t = now

    def _maybe_roll_locked(self):
        now = time.monotonic()
        if (now - self._block_t) >= self.BLOCK_S:
            self._roll_locked(now)

    def flip_pending(self):
        """처리군→비교군으로 바뀌어 아직 EcoQoS 를 못 푼 pid 사본.

        ★읽어도 지우지 않는다★ 처음에는 읽는 순간 비우게 만들었는데,
        호출부에서 예외가 한 번만 나도(실제로 났다 — set & EcoQoSLedger
        는 TypeError 다) 그 pid 들이 영구 유실되어 '비교군 라벨을 달고
        EcoQoS 는 걸린 채'로 남았다. 그러면 비교군이 오염되고, 그건
        패치22 를 못 쓰게 만들었던 캐리오버와 같은 상태다.
        실제로 푼 것만 flip_done() 으로 알린다. ECO.release 가 실패분을
        장부에 남기는 것과 같은 규칙이다.
        """
        with self._lk:
            return set(self._flip_out)

    def flip_done(self, pids):
        """실제로 EcoQoS 해제에 성공한 pid 만 대기열에서 지운다."""
        with self._lk:
            self._flip_out -= set(pids)

    def assign(self, pid):
        """이 pid 를 처리군/비교군 중 어디에 넣을지 정한다(한 번만).

        반환값 True = 처리군(=EcoQoS 를 걸어도 되는 대상).
        무작위 대신 카운터를 쓰는 이유: 재현 가능하고, 비율이 정확히
        1/CONTROL_EVERY 로 유지된다.
        """
        with self._lk:
            self._maybe_roll_locked()
            g = self._grp.get(pid)
            if g is not None:
                return g == "t"
            self._n += 1
            g = "c" if (self._n % self.CONTROL_EVERY == 0) else "t"
            self._grp[pid] = g
            return g == "t"

    def observe(self, pid, rate_cores):
        """이 pid 의 현재 CPU 사용률(코어 단위)을 기록한다."""
        try:
            r = float(rate_cores)
        except (TypeError, ValueError):
            return
        if r != r or r < 0:
            return
        with self._lk:
            self._maybe_roll_locked()
            if pid not in self._grp:
                return
            if pid not in self._first:
                self._first[pid] = r      # 이번 블록의 앵커
            self._now[pid] = r

    def forget(self, pid):
        with self._lk:
            self._grp.pop(pid, None)
            self._first.pop(pid, None)
            self._now.pop(pid, None)
            self._flip_out.discard(pid)

    def tracked(self):
        with self._lk:
            return list(self._grp.keys())

    @staticmethod
    def _spread(vals):
        if len(vals) < 3:
            return 0.0
        med = _median(vals)
        return _median([abs(v - med) for v in vals])

    def result(self):
        """화면이 그대로 쓰는 판정.

        state: idle / collecting / none / better / worse
        delta_cores: 우리 조치로 줄어든 총 부하(코어). 비교군이 겪은
                     자연 감소분을 뺀 값이다.
        """
        with self._lk:
            self._maybe_roll_locked()
            drops_t, drops_c = [], []
            for dt, dc in self._blocks:
                drops_t.extend(dt)
                drops_c.extend(dc)
            if not self._blocks:
                # 첫 블록이 마감되기 전(<90초)에는 진행 중인 값을 쓴다.
                # 블록이 하나라도 쌓인 뒤에는 쓰지 않는다 — 롤 직후에는
                # first == now 라 0 이 무더기로 섞여 양쪽 중앙값을 함께
                # 0 으로 끌어당긴다(=효과를 지운다).
                for pid, g in self._grp.items():
                    f = self._first.get(pid)
                    n = self._now.get(pid)
                    if f is None or n is None:
                        continue
                    if g == "c" and pid in self._flip_out:
                        continue      # ★패치30★ 해제 확인 전
                    (drops_t if g == "t" else drops_c).append(f - n)
            n_treated = sum(1 for g in self._grp.values() if g == "t")
            n_unreleased = len(self._flip_out)   # ★패치30★ 해제 대기 중
            # ★PATCH28★ 지금 대상들이 실제로 쓰고 있는 부하. 이것이
            # '잴 수 있는 최대치' 다 — CPU 를 0 으로 만들어도 감소분은
            # 이 값을 넘을 수 없다.
            lvl_t = [self._now[p] for p, g in self._grp.items()
                     if g == "t" and p in self._now]
        out = {"state": "idle", "n_t": len(drops_t), "n_c": len(drops_c),
               "need_t": self.MIN_T, "delta_cores": 0.0,
               "per_proc": 0.0, "drift": 0.0,
               # ★PATCH28★ headroom = 대상들이 실제로 쓰는 부하의 중앙값.
               # 이보다 큰 감소는 물리적으로 불가능하다.
               "headroom": _median(lvl_t) if lvl_t else 0.0,
               # ★패치30★ 비교군 라벨은 달았지만 아직 EcoQoS 를 못 푼
               # 프로세스 수. 이게 계속 크면 비교군이 오염되고 있다.
               "unreleased": n_unreleased,
               "floor": self.MIN_DELTA_CORES}
        if not drops_t and not drops_c:
            return out
        if len(drops_t) < self.MIN_T or len(drops_c) < self.MIN_C:
            # ★패치30★ 비교군이 모자란 이유가 '아직 안 모임' 인지
            # '해제가 안 돼서 못 씀' 인지 구별한다. 후자를 measuring 으로
            # 덮으면 영원히 끝나지 않는 진행 표시가 된다.
            if len(drops_c) < self.MIN_C and n_unreleased >= self.MIN_C:
                out["state"] = "control_blocked"
            else:
                out["state"] = "collecting"
            return out
        med_t = _median(drops_t)
        med_c = _median(drops_c)
        per = med_t - med_c          # 비교군이 겪은 변화를 뺀 순효과
        out["per_proc"] = per
        out["drift"] = med_c
        # ★블록을 합치면 표본 수가 프로세스 수의 몇 배가 된다.★
        # 총량은 표본 수가 아니라 '지금 처리 중인 프로세스 수' 로 낸다.
        out["delta_cores"] = per * n_treated
        # ★패치29★ 하한은 '산포' 가 아니라 '중앙값의 표준오차' 다.
        # MAD 합을 그대로 쓰면 표본이 6개든 300개든 하한이 같아, 모을수록
        # 손해였다. 방해가 만드는 건 가짜 성공이 아니라 '못 봄' 이다
        # (판정이 차분이라 공통 부하는 상쇄된다).
        # 근거와 시뮬 수치: docs/ARCHITECTURE.md 함정 (41)
        se = self.K_SIGMA * self._SE_MED * (
            self._spread(drops_t) / math.sqrt(len(drops_t))
            + self._spread(drops_c) / math.sqrt(len(drops_c)))
        floor = max(self.MIN_DELTA_CORES, se)
        out["floor"] = floor
        # ★패치28★ "효과 없음" 과 "잴 수 없음" 은 다른 말이다. 대상
        # 선정(proc_is_idle 0.3%)이 만드는 감소량 상한이 판정 하한보다
        # 작으면 어떤 진짜 효과도 통과 못 한다 → 그때는 unmeasurable.
        # 근거와 시뮬 수치: docs/ARCHITECTURE.md 함정 (40)
        if abs(per) < floor and out["headroom"] < floor:
            out["state"] = "unmeasurable"
        elif abs(per) < floor:
            out["state"] = "none"
        else:
            out["state"] = "better" if per > 0 else "worse"
        return out


EFFECT = EffectEstimator()


class CoreMode:
    """Executes Lite or Hard Core optimization with measurable, real results.

    Both modes report:
        - Actual RAM freed (working set delta, measured)
        - CPU% before vs after (measured)
        - BG processes throttled (count)
        - Each step's individual result

    Lite Core: 5 steps, ~35% effect of Hard Core, fully reversible
    Hard Core: 14 steps, deeper but mostly still reversible
    """

    def __init__(self, observer, guard, executor):
        self.observer = observer
        self.guard = guard
        self.executor = executor
        self.k = kernel32
        self.psapi = psapi
        self._timer_handles = []  # For Hard Core temp timer
        # ── ★추가 상태★ (성능 회귀 방지용) ──────────────────────
        # pid -> 우리가 손대기 전의 '진짜' 우선순위. 사이클이 겹쳐도
        # 절대 덮어쓰지 않는다(우선순위 오염 방지).
        self._nice_orig = {}
        # EcoQoS 장부 — 전역 ECO 하나를 LatencyOptimizer 와 공유한다.
        # (따로 들고 있으면 포그라운드 해제가 반쪽만 된다)
        self._ecoqos_pids = ECO
        # 워킹셋 트림 쿨다운(pid -> 마지막 트림 시각). 같은 프로세스를
        # 매 사이클 비우면 하드 폴트만 늘고 체감은 더 나빠진다.
        self._trim_cool = {}
        self._last_standby_purge = 0.0
        self._services_paused_once = False
        # ★신규★ 최신 Windows API 최적화 묶음
        self.modern = ModernOptimizer(guard)
        self._modern_prune_t = 0.0

        # ★신규★ 우리가 직접 재는 CPU 표본(캐시 미사용)
        self._bg_cpu_prev = {}
        self._sys_cpu_prev = None
        self._cores = psutil.cpu_count(logical=True) or 1
        self._last_self_cpu_pct = 0.0
        self._last_bg_cores = 0.0
        self._bg_cores_hist = deque(maxlen=20)
        self._cpu_meas_n = 0
        # ★신규★ 홀드아웃(대조군) 표본 — 아래 _run_cycle 참조
        self._holdout_samples = []
        self._last_pis_dominant = "none"
        self._last_pis_tier = "pis_tier_nodata"
        self._last_pis_measured = 0

        # ─── Continuous mode state ────────────────────────────────
        self._cont_run = False
        self._cont_mode = None     # "lite" or "hard"
        self._cont_thread = None
        self._cont_lock = threading.Lock()
        # Baseline (taken at start) — used to compute improvement %
        self._baseline_ram_mb = 0
        self._baseline_cpu_pct = 0
        # Running total of RAM freed across all cycles
        self._cont_ram_freed_mb = 0
        self._cont_cycles = 0
        self._due_next = {}
        self._cont_progress_cb = None
        self._cycle_skips = {}          # ★PATCH26★ 액션키 -> 미실행 사유
        self._cycle_ran = []            # ★PATCH26★ 이번 사이클 실행 라벨
        self._cont_status_cb = None  # called each cycle with stats dict
        # 전원 계획 변경 전 원래 활성 구성표 GUID 를 보관한다.
        # High Performance 로 바꾼 뒤 모드 종료/앱 종료 시 반드시 원복한다.
        self._saved_power_scheme = None

    def _measure_ram_used(self):
        """Returns (used_mb, free_mb)."""
        vm = psutil.virtual_memory()
        return (vm.total - vm.available) // (1024 * 1024), \
               vm.available // (1024 * 1024)

    # 백그라운드 CPU 를 직접 잴 때 표본으로 삼는 프로세스 수.
    # 전체(약 300~500개)를 매번 열면 비용이 크고, CPU 를 쓰는 프로세스는
    # 항상 상위 소수에 몰려 있으므로 상위 N + 직전 표본만 본다.
    BG_SAMPLE_N = 40

    # ★백그라운드 부하 하한(코어 단위)★
    # 상대 변화율은 분모가 작으면 거짓말을 한다. 대표님 PC 는 논리코어
    # 32개라 bg_cpu_pct 가 '코어 32개 용량 대비 %' 로 나온다 — 백그라운드가
    # 코어 0.3개를 쓰고 있어도 화면상으론 겨우 0.9% 다. 이 값을 분모로
    # 쓰면 0.3%p 짜리 잡음 하나가 곧바로 ±33% 로 증폭된다.
    # 기존 하한 0.3(%)은 코어 수를 고려하지 않은 값이라 32스레드에서는
    # 사실상 아무것도 걸러내지 못했다.
    MIN_BG_CORES = 0.10        # 이보다 작으면 아예 '잴 부하가 없었다'
    BG_DEADBAND_CORES = 0.05   # 잡음 하한(적응형 추정이 없을 때의 기본값)
    BG_MAX_DEADBAND = 0.5      # 적응형 데드밴드 상한(코어, 최소치)
    # ★패치23★ 상한을 코어 수에 비례시킨다.
    # 패치15·16 에서 하한(MIN_BG_CORES)은 코어 단위로 고쳤는데 상한만
    # 0.5 코어 고정으로 남았다. 32스레드에서 0.5코어는 1.5%p 라
    # "평소 5% 돌다가 7% 로 뛰는" 정도의 흔들림이 그대로 통과해
    # -24.6% → PIS 42~45점(="소폭 역효과")으로 찍혔다. 우리가 한 일이
    # 아니라 크롬 탭 하나·디펜더 스캔이 만든 값이다.
    BG_DEADBAND_FRAC = 0.04    # 전체 용량의 4%(=4%p) 까지는 흔들림
    # ★분모 완충 상수(코어)★
    # 하한만으로는 부족하다. 하한 바로 위에서는 여전히 '작은 분모'라,
    # 데드밴드를 겨우 넘긴 변화가 곧바로 20~30% 로 튄다(0% → 25% 절벽).
    # 그래서 비율을 (base - cur) / (base + K) 로 계산한다.
    #  · 부하가 작으면 K 가 분모를 지배해 비율이 눌린다(잡음 증폭 차단)
    #  · 부하가 커지면 K 의 영향이 사라져 실제 비율로 수렴한다
    # 부작용은 '실제 개선을 과소 표기'하는 쪽이다. 과대 표기보다 이쪽이
    # 낫다 — 이 앱은 계기판이 잘 나오게 만드는 걸 목표로 하지 않는다.
    # 값을 '코어 1개' 로 잡은 근거: 백그라운드가 코어 1개도 안 쓰고 있었다면
    # 그건 애초에 최적화로 크게 좋아질 여지가 없는 상태다. 그런 구간에서
    # 나오는 큰 %는 성과가 아니라 잡음이다.
    BG_K_CORES = 1.0

    @classmethod
    def bg_rel_change(cls, base_pct, cur_pct, cores, noise_cores=None):
        """백그라운드 CPU 상대 변화율(%). 잴 수 없으면 None.

        ★대표님 PC 에서 'CPU 개선율 -50%' 가 고정으로 뜬 직접 원인 중
        하나가 이 계산이었다.★ 기존 식은

            if base_bg > 0.3: (base_bg - cur_bg) / base_bg * 100

        인데, 32스레드에서 base_bg 는 유휴 시 1% 안팎이다. 여기에
        OMEGA X 자신이 쓰는 CPU(사이클마다 프로세스 순회·측정, 코어
        0.1~0.3개 = 0.3~0.9%p)가 '백그라운드 부하' 로 함께 집계되면서
        분자에 그대로 얹혔고, -50% 부근이 세션 내내 중앙값으로 굳었다.
        즉 화면의 -50% 는 '시스템이 절반 나빠졌다'가 아니라
        '작은 분모 + 자기 자신 포함' 이 만든 착시였다.

        코어가 적은 PC 에서는 같은 부하가 큰 %로 잡혀 이 문제가 잘
        드러나지 않는다. '나 같은 CPU 에서만' 보였던 이유가 그것이다.

        ★그리고 하한/데드밴드만으로는 부족하다★ 부하 자체가 원래 작으면
        (평소에 CPU 를 조금만 쓰는 PC) 하한을 갓 넘긴 상태에서 아주 작은
        변화가 여전히 큰 %로 보인다. 그래서 분모에 완충 상수 K 를 더한
        형태로 계산하고, 데드밴드는 실제 측정 흔들림(noise_cores)에서
        구한다. 아래 두 장치가 함께 걸려야 숫자가 안정된다.

        noise_cores: 최근 측정의 흔들림 추정치(코어). None 이면 기본값.
        """
        try:
            cores = max(1, int(cores or 1))
            base_c = float(base_pct or 0.0) * cores / 100.0
            cur_c = float(cur_pct or 0.0) * cores / 100.0
        except Exception:
            return None
        if base_c < cls.MIN_BG_CORES:
            return None                     # 잴 부하가 없었다
        try:
            dead = float(noise_cores)
        except (TypeError, ValueError):
            dead = cls.BG_DEADBAND_CORES
        # ★패치23★ 상한은 코어 수에 비례한다. 코어가 많을수록 같은 %p
        # 흔들림이 더 많은 '코어' 로 환산되기 때문이다.
        hi = max(cls.BG_MAX_DEADBAND, cores * cls.BG_DEADBAND_FRAC)
        dead = max(cls.BG_DEADBAND_CORES, min(hi, dead))
        if abs(base_c - cur_c) < dead:
            return 0.0                      # 측정 흔들림보다 작은 변화
        return (base_c - cur_c) / (base_c + cls.BG_K_CORES) * 100.0

    def bg_noise_cores(self):
        """최근 백그라운드 측정의 흔들림(코어). 중앙값 절대편차(MAD) 기반.

        표본이 부족하면 None. 평균편차 대신 MAD 를 쓰는 이유는 스파이크
        한 번에 추정치가 끌려가지 않게 하기 위해서다(_median 과 같은 이유).
        """
        h = list(getattr(self, "_bg_cores_hist", []))
        if len(h) < 5:
            return None
        med = _median(h)
        mad = _median([abs(x - med) for x in h])
        hi = max(self.BG_MAX_DEADBAND,
                 getattr(self, "_cores", 1) * self.BG_DEADBAND_FRAC)
        return max(self.BG_DEADBAND_CORES, min(hi, mad * 1.5))

    def _sample_bg_cpu(self):
        """백그라운드 CPU 부하를 '직접' 측정한다. 반환 (전체 대비 %, 개수).

        ★수정(측정이 안 변하던 원인)★
        기존 코드는 psutil.process_iter(["pid","cpu_percent","name"]) 로
        값을 읽었는데, 이 파일은 process_iter 를 PROC_CACHE(TTL 5초)로
        몽키패치해 두었다. 코어 사이클은 1.5~4초이므로 연속된 두 번의
        측정이 '같은 캐시 세대'의 값을 그대로 읽어 델타가 정확히 0 이
        되는 일이 잦았다. 시작 시점 baseline 과 초반 3사이클(워밍업
        1.5초 간격)은 거의 항상 같은 값이었다.

        또 기존 코드는 fg_pid 하나만 제외했다. 크롬·일렉트론·게임의
        자식 프로세스는 전부 '백그라운드 부하'로 집계되어, 사용자가
        무엇을 하든 그 활동이 우리 점수를 깎았다.

        이제 (1) 우리가 직접 cpu_times 델타를 재고 (2) 구간이 정확히
        사이클 간격이며 (3) 포그라운드 트리 전체를 제외한다.
        """
        now = time.time()
        prev = getattr(self, "_bg_cpu_prev", None)
        if prev is None:
            prev = {}
        cur = {}
        total_cores_busy = 0.0
        n = 0
        try:
            infos = PROC_CACHE.info_list()
        except Exception:
            infos = []
        cand = sorted(infos, key=lambda i: (i.get("cpu_percent") or 0),
                      reverse=True)[:self.BG_SAMPLE_N]
        cand_pids = set()
        for i in cand:
            if i.get("pid"): cand_pids.add(i["pid"])
        pids = set(cand_pids)
        pids |= set(prev.keys())
        self_busy = 0.0
        rates = {}
        keep = set(pids)
        for pid in pids:
            if pid in (0, 4): continue
            try:
                if FG.is_protected(pid): continue
            except Exception as _dx: DIAG.q("CoreMode._sample_bg_cpu#0", _dx)
            try:
                ct = psutil.Process(pid).cpu_times()
                busy = ct.user + ct.system
            except Exception:
                continue
            cur[pid] = (busy, now)
            pb, pt = prev.get(pid, (None, None))
            if pb is None: continue
            dt = now - pt
            if dt <= 0.05: continue
            d = (busy - pb) / dt        # 1.0 = 코어 1개를 100% 점유
            # ★수정(개선율이 늘 음수로 나오던 직접 원인)★
            # OMEGA X 자신이 '백그라운드 부하' 로 집계되고 있었다.
            # 우리는 매 사이클 프로세스를 순회하고 측정하느라 코어
            # 0.1~0.3개를 쓴다. 그걸 '우리가 못 없앤 부하' 로 세면,
            # 액션을 다 풀고 조용히 재는 홀드아웃(기준)보다 실행 구간의
            # 부하가 항상 커 보인다 — 32스레드처럼 분모가 작은 PC 에서는
            # 그 차이만으로 -50% 가 나온다.
            # 자기 자신은 부하에서 빼되, 값은 따로 남겨 숨기지 않는다.
            if pid == SELF_PID:
                if d > 0:
                    self_busy = d
                continue
            if d > 0.005:
                total_cores_busy += d
                n += 1
            rates[pid] = d          # 프로세스별 사용률(코어) — 효과 측정용
            if d <= 0.005 and pid not in cand_pids:
                keep.discard(pid)   # 부하도 없고 후보도 아니면 추적 중단
        # ★추적 집합 상한★ 기존엔 pids = 상위N ∪ 직전표본 이라 집합이
        # 사이클마다 단조 증가했다(프로세스가 죽어야만 빠진다). 세션이
        # 길어질수록 아주 작은 델타를 가진 프로세스가 계속 누적돼 현재값이
        # 기준값보다 구조적으로 커졌다 — 이것도 개선율을 음수 쪽으로
        # 미는 요인이었다.
        if len(cur) > self.BG_SAMPLE_N * 2:
            cur = {p: v for p, v in cur.items() if p in keep}
        self._bg_cpu_prev = cur
        cores = max(1, psutil.cpu_count(logical=True) or 1)
        self._last_self_cpu_pct = (self_busy / cores) * 100.0
        # 흔들림 추정용 원시 이력(코어 단위). 데드밴드를 고정 상수가 아니라
        # 이 PC 에서 실제로 관측되는 잡음 폭에서 구한다.
        h = getattr(self, "_bg_cores_hist", None)
        if h is None:
            h = self._bg_cores_hist = deque(maxlen=20)
        h.append(total_cores_busy)
        self._last_bg_rates = rates
        self._last_bg_cores = total_cores_busy
        return (total_cores_busy / cores) * 100.0, n

    def _sample_sys_cpu(self):
        """시스템 전체 CPU 사용률. psutil.cpu_percent(interval=0.1) 은
        0.1초 창이라 편차가 ±20%p 로 크고, interval=None 은 다른 코드
        (Observer·GUI)가 먼저 호출하면 구간이 오염된다. 우리 전용
        cpu_times 스냅샷으로 사이클 구간 정확히 잰다."""
        try:
            t = psutil.cpu_times()
        except Exception:
            return 0.0
        prev = getattr(self, "_sys_cpu_prev", None)
        self._sys_cpu_prev = t
        if prev is None:
            return 0.0
        try:
            idle_d = t.idle - prev.idle
            all_d = sum(t) - sum(prev)
            if all_d <= 0: return 0.0
            return max(0.0, min(100.0, (1.0 - idle_d / all_d) * 100.0))
        except Exception:
            return 0.0

    def _measure_full(self):
        """AI 점수(PIS)가 보는 측정 벡터.

        ★변경점★
          · bg_cpu_pct = '머신 전체 용량 대비 백그라운드 CPU %'(0~100).
            기존 bg_cpu_norm 은 프로세스별 cpu_percent 합을 논리코어수로
            나눈 값이었는데, 대표님 PC 는 논리코어 32개라 백그라운드가
            40%p 줄어도 이 값은 1.25 밖에 안 움직였다. 점수식이 여기에
            ×4 를 곱해도 5점, 가중치 0.25 를 거치면 최종 점수 +2 였다.
            PIS 에서 25% 지분을 가진 항목이 사실상 죽어 있었다.
          · pdh_ok 를 함께 실어 보낸다. PDH 가 죽었으면 큐/폴트 기반
            컴포넌트를 '0'이 아니라 '측정 불가'로 처리해야 한다.
        """
        cpu = self._sample_sys_cpu()
        vm = psutil.virtual_memory()
        ram_used_mb = (vm.total - vm.available) // (1024 * 1024)
        ram_pct = vm.percent
        bg_cpu_pct, bg_proc_count = self._sample_bg_cpu()
        fg_name, fg_pid = get_foreground_info()
        perf = self.observer.perf

        return {
            "cpu_pct":         cpu,
            "ram_used_mb":     ram_used_mb,
            "ram_pct":         ram_pct,
            "page_faults":     perf.page_faults,
            "ctx_switches":    perf.ctx_switches,
            "cpu_queue":       perf.cpu_queue,
            "disk_queue":      perf.disk_queue,
            "disk_busy":       getattr(perf, "disk_busy", 0.0),
            "hard_faults":     getattr(perf, "hard_faults", 0.0),
            "bg_cpu_pct":      bg_cpu_pct,
            # 하위 호환(기존 코드가 참조) — 같은 의미의 값을 넣어둔다
            "bg_cpu_norm":     bg_cpu_pct,
            "bg_proc_count":   bg_proc_count,
            # OMEGA X 자신이 쓰는 CPU(전체 용량 대비 %). 부하 계산에서는
            # 빼지만 값 자체는 남긴다 — 우리 비용을 숨기지 않는다.
            "self_cpu_pct":    getattr(self, "_last_self_cpu_pct", 0.0),
            "pdh_ok":          bool(getattr(perf, "ok", False)),
            "fg_pid":          fg_pid,
            "ts":              time.time(),
        }

    # 각 컴포넌트의 기본 가중치. 실제로 측정된 것만 남기고 합이 1.0 이
    # 되도록 매 사이클 재정규화한다(★핵심 수정★).
    PIS_WEIGHTS = {
        "memory":     0.30,
        "bg_cpu":     0.30,
        "responsive": 0.18,
        "disk":       0.10,
        "thrashing":  0.12,
    }

    @staticmethod
    def _rel_drop(base, cur, floor):
        """감소율(%). base 가 floor 미만이면 '잴 부하가 없었다' → None."""
        if base is None or cur is None: return None
        if base < floor: return None
        return (base - cur) / float(base) * 100.0

    def _compute_pis(self, baseline: dict, current: dict) -> dict:
        """Performance Improvement Score (0-100). 50 = 변화 없음.

        ★전면 재설계 이유★
        이전 버전은 모든 컴포넌트를 '절대 델타 × 상수'로 계산했다.
        그 결과 실제 하드웨어에서 점수가 50 근처에 붙어 움직이지 않았다.
        대표님 PC(32스레드/16GB) 기준 실측 계산:

          · bg_cpu   : 백그라운드를 80% 줄여도 컴포넌트 4.0/25 → 점수 +1.7
          · cpu      : 배율이 0.8 로 다른 항목(4~10)보다 10배 작아 사실상 0
          · thrashing: Page Faults/sec 는 평시 수천~수만이라 /100×2 가
                       항상 ±20 클램프에 포화 → 순수 노이즈
          · responsive/disk/thrashing : PDH 등록 실패 시 영구 0
                       (= 가중치 0.40 이 상시 사망, 최대 점수 76점)

        실측 시뮬레이션: '아주 잘 된 경우'조차 65점, 평범한 경우 56점.
        즉 최적화가 성공해도 실패해도 화면 숫자가 거의 같았다.

        ★새 설계★
          (1) 모든 컴포넌트를 '상대 변화율(%)'로 계산한다.
              코어 수·RAM 용량에 무관하게 같은 의미를 갖는다.
          (2) 측정되지 않은 컴포넌트는 0 이 아니라 None(제외)이고,
              남은 컴포넌트로 가중치를 재정규화한다.
              → PDH 가 죽어도 점수 범위가 눌리지 않는다.
          (3) 포그라운드 CPU 는 컴포넌트에서 뺐다. 사용자가 무엇을
              하느냐에 따라 변하는 값이지 우리 성과가 아니다.
              (RAM/CPU 개선% 표시에서 이미 같은 원칙을 적용했다)
        """
        b = baseline or {}
        c = current or {}
        comp = {}

        # 1) 메모리 사용량 감소율 — 1% 감소당 3점, ±30 클램프
        r = self._rel_drop(b.get("ram_used_mb"), c.get("ram_used_mb"), 512)
        if r is not None:
            comp["memory"] = max(-30.0, min(30.0, r * 3.0))

        # 2) 백그라운드 CPU 감소율 — 1% 감소당 0.35점, ±30 클램프
        #    (100% 제거 = 35 → 30 으로 클램프)
        # ★하한을 코어 단위로★ 기존 0.3(%) 은 32스레드에서 코어 0.1개도
        # 안 되는 값이라 사실상 아무것도 못 걸렀다. bg_rel_change 참조.
        # ★패치23 — 대조군 기반으로 교체★
        # 기존 계산은 '홀드아웃 중앙값(5~13분 전) vs 지금' 이라 시간분리
        # 비교였다. 패치19 에서 폐기한 방식 그대로다. 그래서 그 사이에
        # 크롬 탭이 하나 늘거나 디펜더가 스캔을 돌면 그게 전부 우리
        # 점수로 계상됐다. 32스레드에서 배경이 5%→7% 로 오르는 정도
        # (=0.64코어)만으로 -24.6% → 42~45점("소폭 역효과")이 찍혔다.
        #
        # 데드밴드로는 못 고친다. 0.64코어는 측정 흔들림이 아니라
        # 진짜 부하 증가이고, 데드밴드는 '작은 변화' 를 거를 뿐
        # '원인이 우리가 아닌 변화' 를 구분하지 못한다. 같은 창에서
        # 같이 굴린 비교군만이 구분할 수 있다.
        r = None
        try:
            ef = EFFECT.result()
        except Exception:
            ef = None
        if ef and ef.get("state") in ("better", "worse", "none"):
            if ef["state"] == "none":
                r = 0.0            # 비교군과 차이가 없었다
            else:
                cores = max(1, getattr(self, "_cores", 1))
                base_c = float(b.get("bg_cpu_pct") or 0.0) * cores / 100.0
                r = (ef.get("delta_cores", 0.0)
                     / (base_c + self.BG_K_CORES) * 100.0)
        if r is None:
            # 대조군 표본이 아직 없을 때만(모드 시작 직후) 기존 계산.
            r = self.bg_rel_change(b.get("bg_cpu_pct", b.get("bg_cpu_norm")),
                                   c.get("bg_cpu_pct", c.get("bg_cpu_norm")),
                                   getattr(self, "_cores", 1),
                                   self.bg_noise_cores())
        if r is not None:
            comp["bg_cpu"] = max(-30.0, min(30.0, r * 0.35))

        # 3~5) PDH 기반 지표.
        # ★수정(대표님 PC 실측 반영)★
        # 등록 성공 여부만 보는 걸로는 부족하다. 등록에 성공해도 값 자체가
        # 상시 0 이면(32스레드에서 Processor Queue Length, NVMe 에서
        # Current Disk Queue Length) 그 컴포넌트는 '변화 없음(0점)'이
        # 아니라 '측정 불가'로 빼야 한다. 0점으로 넣으면 가중치만 잡아먹고
        # 전체 점수를 50 쪽으로 끌어내린다 — 이게 점수가 안 움직인 이유의
        # 큰 축이다.
        pdh = bool(b.get("pdh_ok")) and bool(c.get("pdh_ok"))
        if pdh:
            # (a) 응답성 — 프로세서 큐. 양쪽 다 사실상 0 이면 잴 게 없다.
            qb = b.get("cpu_queue", 0) or 0
            qc = c.get("cpu_queue", 0) or 0
            if max(qb, qc) >= 0.5:
                comp["responsive"] = max(-25.0, min(25.0, (qb - qc) * 8.0))

            # (b) 디스크 — Current Disk Queue Length 대신 사용률(%)을 쓴다.
            #     구값(disk_queue)밖에 없으면 그때만 폴백.
            db = b.get("disk_busy")
            dc = c.get("disk_busy")
            if db is not None and dc is not None and max(db, dc) >= 2.0:
                comp["disk"] = max(-20.0, min(20.0, (db - dc) * 0.4))
            else:
                qdb = b.get("disk_queue", 0) or 0
                qdc = c.get("disk_queue", 0) or 0
                if max(qdb, qdc) >= 0.2:
                    comp["disk"] = max(-20.0, min(20.0, (qdb - qdc) * 10.0))

            # (c) 스래싱 — Pages Input/sec(하드 폴트)만 본다.
            #     Page Faults/sec 는 소프트 폴트 포함이라 유휴에도 8만이
            #     나오고 1.5초에 43% 요동친다 = 노이즈. 절대 쓰지 않는다.
            hb = b.get("hard_faults")
            hc = c.get("hard_faults")
            if hb is not None and hc is not None and max(hb, hc) >= 20.0:
                r = self._rel_drop(max(hb, 1.0), hc, 1.0)
                if r is not None:
                    comp["thrashing"] = max(-20.0, min(20.0, r * 0.20))

        if not comp:
            return {"score": 50, "components": {}, "weights": {},
                    "dominant": "none", "tier_key": "pis_tier_nodata",
                    "measured": 0, "pdh_ok": pdh}

        # ★가중치 재정규화★ — 측정된 항목만으로 합이 1.0 이 되게 한다.
        wsum = sum(self.PIS_WEIGHTS[k] for k in comp)
        weights = {k: self.PIS_WEIGHTS[k] / wsum for k in comp}
        weighted = sum(comp[k] * weights[k] for k in comp)

        # ★신뢰도 감쇠★ 재정규화만 하면 측정 가능한 신호가 2개뿐일 때도
        # 100점/0점이 나올 수 있다. 신호가 적을수록 50(=판단 보류) 쪽으로
        # 당긴다. PDH 가 살아나면(5개 전부) 감쇠가 사라진다.
        conf = 0.6 + 0.4 * (len(comp) / float(len(self.PIS_WEIGHTS)))
        score = int(max(0, min(100, round(50 + weighted * 1.67 * conf))))

        positives = {k: v for k, v in comp.items() if v > 0.5}
        dominant = max(positives, key=positives.get) if positives else "none"

        # ★수정★ 기존 등급 문구는 35~49 구간(=실제로는 악화)을
        # "소폭 — 작은 개선"으로 표시했다. 50 이 '변화 없음'이므로
        # 그 아래는 개선이 아니라 악화다. 구간과 문구를 맞춘다.
        if score >= 72:
            tier_key = "pis_tier_excellent"
        elif score >= 58:
            tier_key = "pis_tier_good"
        elif score >= 45:
            tier_key = "pis_tier_stable"
        elif score >= 32:
            tier_key = "pis_tier_minor"
        else:
            tier_key = "pis_tier_idle"

        return {
            "score":      score,
            "components": comp,
            "weights":    weights,
            "dominant":   dominant,
            "tier_key":   tier_key,
            "measured":   len(comp),
            "pdh_ok":     pdh,
        }

    # 같은 프로세스를 다시 트림하기까지의 최소 간격(초)
    TRIM_COOLDOWN_S = 90.0

    def _trim_bg_processes(self, aggressive=False):
        """Trim working sets of background processes. Returns (count, mb_freed).

        ★수정(핵심 성능 회귀 원인)★
        기존: 사이클(3~4초)마다 최대 60개 프로세스에 EmptyWorkingSet.
        EmptyWorkingSet 은 RAM 을 '해제'하는 게 아니라 워킹셋을 스탠바이/
        페이지파일로 밀어내는 동작이다. 밀려난 프로세스가 다시 동작하는
        순간 하드 페이지 폴트가 폭증해 디스크 I/O 와 끊김을 만든다.
        분당 900회 수준으로 돌리면 '표시되는 여유 RAM' 만 늘고 체감은
        반드시 나빠진다. → 대상 수 축소 + pid 별 쿨다운을 둔다.
        """
        cleaned = 0
        before_total_mb = 0
        after_total_mb = 0
        targets = []
        now_ts = time.time()
        # 만료된 쿨다운 정리 (메모리 누수 방지)
        if len(self._trim_cool) > 400:
            self._trim_cool = {k: v for k, v in self._trim_cool.items()
                               if now_ts - v < self.TRIM_COOLDOWN_S}

        # Find candidates
        for p in psutil.process_iter(["pid", "name", "cpu_percent",
                                      "memory_percent", "memory_info",
                                      "status"]):
            try:
                info = p.info
                name = (info.get("name") or "").lower()
                if not is_target(info.get("pid"), name): continue

                # ★수정★ pid 별 쿨다운 — 같은 프로세스 반복 트림 금지
                if now_ts - self._trim_cool.get(info["pid"], 0.0) < self.TRIM_COOLDOWN_S:
                    continue

                mem_mb = info["memory_info"].rss // (1024 * 1024) if info.get("memory_info") else 0
                # ★수정★ 임계값 복원: 작은 프로세스를 긁어봐야 회수량은
                # 미미하고 폴트 비용만 든다. hard 50MB / lite 100MB 이상만.
                if mem_mb < (50 if aggressive else 100): continue

                cpu = info.get("cpu_percent", 0)
                status = info.get("status", "")

                # Lite: sleeping OR low-cpu (기존엔 AND → 너무 빡빡함)
                if not aggressive:
                    if status not in ("sleeping", "stopped") and cpu > 0.5:
                        continue
                # Hard: cpu < 2% (기존 1% → 더 많이 잡음)
                else:
                    if cpu > 2.0: continue

                targets.append((info["pid"], name, mem_mb))
            except Exception as _dx: DIAG.q("CoreMode._trim_bg_processes#0", _dx)

        # ★수정★ 상한 대폭 축소 (hard 60→12, lite 20→6)
        targets.sort(key=lambda x: -x[2])
        targets = targets[:12 if aggressive else 6]

        # 1단계: before 측정 (한 번에 모음)
        proc_list = []
        for pid, name, mem_mb in targets:
            try:
                p_obj = psutil.Process(pid)
                before_mb = p_obj.memory_info().rss // (1024 * 1024)
                before_total_mb += before_mb
                proc_list.append((pid, p_obj, before_mb))
            except Exception as _dx: DIAG.q("CoreMode._trim_bg_processes#1", _dx)

        # 2단계: EmptyWorkingSet 전체 실행 (병렬 효과)
        for pid, _, _ in proc_list:
            try:
                # ★수정★ ALL_ACCESS(0x1F0FFF) → EmptyWorkingSet 에 실제로
                # 필요한 권한만. 전권을 요구하면 관리자 권한으로도 상당수
                # 프로세스에서 OpenProcess 가 실패해 조용히 아무 일도
                # 일어나지 않았다.
                h = _open_proc(pid, ACC_TRIM_WS)
                if h:
                    self.psapi.EmptyWorkingSet(h)
                    _close(h)
                    cleaned += 1
                    self._trim_cool[pid] = now_ts   # 쿨다운 기록
            except Exception as _dx: DIAG.q("CoreMode._trim_bg_processes#2", _dx)

        # 3단계: OS가 페이지 회수할 시간 줌 (이게 없으면 freed_mb가 0으로 측정됨)
        try: time.sleep(0.2)   # ★수정★ 0.3 → 0.2
        except Exception as _dx: DIAG.q("CoreMode._trim_bg_processes#3", _dx)

        # 4단계: after 측정
        for pid, p_obj, before_mb in proc_list:
            try:
                after_mb = p_obj.memory_info().rss // (1024 * 1024)
                after_total_mb += after_mb
            except Exception:
                after_total_mb += before_mb

        freed_mb = max(0, before_total_mb - after_total_mb)
        return cleaned, freed_mb

    def _prune_timers(self):
        """끝난 Timer 객체를 목록에서 제거. 예전엔 무한히 쌓여
        장시간 실행 시 리스트가 수천 개로 불어났다."""
        try:
            self._timer_handles = [t for t in self._timer_handles
                                   if t.is_alive()][-64:]
        except Exception:
            self._timer_handles = []

    def _throttle_bg_cpu(self, duration_s=10, aggressive=False):
        """Throttle BG CPU consumers. Returns count throttled.

        ★수정(영구 저우선순위 고착 버그)★
        사이클 간격은 3~4초인데 복구 예약은 8~12초 뒤였다. 즉 다음 사이클이
        먼저 돌면서 '현재 값'(이미 BELOW_NORMAL)을 original 로 다시 저장 →
        복구를 해도 BELOW_NORMAL 로 되돌아간다. 오래 켜둘수록 백그라운드
        프로세스들이 영구히 저우선순위로 굳어 브라우저 탭·디스코드·
        런처류가 눈에 띄게 느려진다. 이제 pid 별 최초 값만 한 번 기록하고,
        이미 조정 중인 pid 는 건드리지 않는다.
        """
        max_count = 15 if aggressive else 5
        cpu_threshold = 0.5 if aggressive else 1.5
        newly = []

        for p in psutil.process_iter(["pid", "name", "cpu_percent"]):
            try:
                info = p.info; pid = info["pid"]
                if pid in self._nice_orig: continue       # 이미 조정 중
                # ★수정★ 포그라운드 프로세스 트리 보호.
                # 기존엔 fg_pid 하나만 빠져서, 크롬 렌더러·게임 워커처럼
                # 실제로 일하는 자식 프로세스가 BELOW_NORMAL 로 내려갔다.
                if not is_target(pid, info.get("name") or ""): continue
                if info.get("cpu_percent", 0) < cpu_threshold: continue

                p_obj = psutil.Process(pid)
                cur = p_obj.nice()
                if cur == psutil.BELOW_NORMAL_PRIORITY_CLASS: continue
                self._nice_orig[pid] = cur                # 진짜 원래값 1회 기록
                p_obj.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
                newly.append(pid)
                if len(newly) >= max_count: break
            except Exception as _dx: DIAG.q("CoreMode._throttle_bg_cpu#0", _dx)

        done = [False]
        def restore():
            if done[0]: return
            done[0] = True
            for pid in newly:
                # ★없으면 건너뛴다★ 예전엔 기본값 NORMAL 로 되돌렸는데,
                # _restore_all_nice(모드 종료·홀드아웃·학습 보류)가 먼저
                # 원복하고 장부를 비운 뒤 이 예약이 뒤늦게 돌면, 원래
                # IDLE 이던 프로세스를 NORMAL 로 '올려'놓게 된다.
                # 모르는 원래값을 추측해서 쓰면 가역성이 깨진다.
                orig = self._nice_orig.pop(pid, None)
                if orig is None:
                    continue
                try:
                    psutil.Process(pid).nice(orig)
                except Exception as _dx: DIAG.q("CoreMode.restore#0", _dx)

        if newly:
            SCHED.call_later(duration_s, restore)
            self.guard.record("core_throttle", "multi", restore)
        return len(newly)

    def _restore_all_nice(self):
        """모드 종료 시 남아있는 우선순위 조정을 전부 원복."""
        for pid, orig in list(self._nice_orig.items()):
            try: psutil.Process(pid).nice(orig)
            except Exception as _dx: DIAG.q("CoreMode._restore_all_nice#0", _dx)
        self._nice_orig.clear()

    class _PTS(ctypes.Structure):
        _fields_ = [("Version", ctypes.c_ulong),
                   ("ControlMask", ctypes.c_ulong),
                   ("StateMask", ctypes.c_ulong)]

    def _set_ecoqos(self, pid, enable: bool) -> bool:
        """EcoQoS on/off — 전역 장부(ECO) 경유. 해제는 성공을 재조회로
        확인했을 때만 장부에서 지운다(실패분은 다음 사이클에 재시도)."""
        if enable:
            return ECO.apply(pid)
        return ECO.release(pid)

    def _apply_ecoqos_bulk(self):
        """Apply EcoQoS to eligible BG processes. Returns count.

        ★수정(영구 저클럭 고착 버그)★
        EcoQoS 는 프로세스를 E-코어/저클럭 모드로 강등한다. 기존 코드는
        StateMask=0x1(켜기)만 있고 되돌리는 경로가 아예 없었다. 즉 한 번
        걸린 프로세스는 '그 프로세스가 종료될 때까지' 계속 느려진 채로
        남는다. 사용자가 나중에 그 앱(브라우저 헬퍼·디스코드·런처·
        컴파일러)을 실제로 쓰기 시작해도 계속 느리다. 이제
        (1) 이미 건 pid 는 다시 걸지 않고 (2) 목록을 보관해 모드 종료 시
        전부 해제하며 (3) 포그라운드로 올라온 프로세스는 즉시 해제한다.
        """
        if not IS_WIN11_22H2: return 0
        applied = 0
        fg_name, fg_pid = get_foreground_info()

        # 종료된 pid 정리 — 안 하면 집합이 계속 불어나고, 재사용된 pid 가
        # '이미 적용됨'으로 오판돼 새 프로세스에 적용이 안 된다.
        if len(self._ecoqos_pids) > 300:
            try:
                alive = set(psutil.pids())
                self._ecoqos_pids &= alive
            except Exception:
                self._ecoqos_pids.clear()

        # 포그라운드로 올라온 프로세스는 즉시 EcoQoS 해제
        if fg_pid and fg_pid in self._ecoqos_pids:
            if self._set_ecoqos(fg_pid, False):
                self._ecoqos_pids.discard(fg_pid)

        # ★수정(체감 성능 하락의 최대 원인)★
        # 기존 루프에는 조건이 사실상 is_safe_to_modify 하나뿐이었다.
        # CPU 사용량도, 상태도, 총량 상한도 보지 않았다. 그래서 안전목록
        # 밖의 프로세스는 무조건 EcoQoS(저클럭 + E코어 강등) 대상이 됐고,
        # 사이클마다 25개씩 누적되며 해제는 모드 종료 때뿐이었다.
        # 5분만 켜두면 시스템의 사용자 프로세스 거의 전부가 저클럭에
        # 묶인다. '최적화를 켰더니 PC 전체가 느려진다'의 정확한 원인이다.
        #
        # 참고로 같은 앱의 LatencyOptimizer.apply_ecoqos 에는 원래부터
        # cpu_percent >= 0.5 필터와 상한 10 이 있었다. 이쪽에만 빠져 있던
        # 명백한 누락이다. 이제 조건을 맞추고, 더 엄격하게 간다.
        #
        # 새 기준 — '지금 놀고 있는데 메모리만 붙잡고 있는' 것만 대상:
        #   · 잠자는(sleeping) 상태이고
        #   · CPU 를 거의 안 쓰고 (< 0.3%)
        #   · RSS 30MB 이상 (아주 작은 건 걸어도 이득이 없다)
        #   · 포그라운드 트리·자기 자신·안티치트·오디오 제외
        #   · 동시 적용 총량 상한 (기본 60개)
        MAX_TRACKED = 60
        room = MAX_TRACKED - len(self._ecoqos_pids)
        if room <= 0:
            return 0
        for inf in PROC_CACHE.info_list():
            try:
                pid = inf.get("pid")
                if pid is None or pid == fg_pid: continue
                if pid in self._ecoqos_pids: continue     # 이미 적용됨
                if not is_target(pid, inf.get("name") or ""): continue
                # ★수정★ 'sleeping' 조건 때문에 EcoQoS 가 한 번도 적용되지
                # 않았다. CPU 사용률로 유휴 여부를 직접 판정한다.
                if not proc_is_idle(inf, 0.3): continue
                mi = inf.get("memory_info")
                if not mi or mi.rss < 30 * 1024 * 1024: continue
                # ★동시 대조군★ 대상 7개 중 1개는 일부러 건드리지 않고
                # 비교군으로 남긴다. 이 몇 개가 없으면 "우리 조치의 효과"
                # 와 "그 사이 시스템이 조용해진 것"을 영영 구분할 수 없다.
                # 조치 '직전' 사용률을 먼저 기록해야 전/후 비교가 성립한다.
                rate0 = (getattr(self, "_last_bg_rates", {}) or {}).get(pid, 0.0)
                treated = EFFECT.assign(pid)
                EFFECT.observe(pid, rate0)
                if not treated:
                    continue
                if self._set_ecoqos(pid, True):
                    applied += 1
                    self._ecoqos_pids.add(pid)
                if applied >= min(15, room): break
            except Exception as _dx: DIAG.q("CoreMode._apply_ecoqos_bulk#0", _dx)
        return applied

    def _release_effect_flips(self):
        """블록 경계에서 처리군→비교군으로 바뀐 프로세스의 EcoQoS 해제.

        ★패치23-b★ 처음에는 이 해제를 _apply_ecoqos_bulk 안에 넣었는데
        틀린 자리였다. 그 함수는

            IS_WIN11_22H2 and self._due("ecoqos", 3) and self._learn_ok("ecoqos")

        세 조건을 다 통과해야 돈다. 특히 _learn_ok 는 학습 보류 블록
        동안 False 이고, ecoqos 가 neutral 로 판정되면 영구 False 다.
        그러면 비교군으로 라벨만 바뀐 프로세스가 EcoQoS 를 계속 달고
        있게 된다 — 비교군이 아니라 '라벨만 바뀐 처리군'이고, 이건
        패치22 에서 학습기를 못 쓰게 만들었던 캐리오버 그 자체다.
        측정의 무결성은 액션 스케줄에 의존하면 안 되므로 사이클 선두에서
        무조건 처리한다.
        """
        try:
            # ★set(...) 로 감싼다★ self._ecoqos_pids 는 ECO(EcoQoSLedger)
            # 이지 set 이 아니다. set & Ledger 는 TypeError 다.
            pending = EFFECT.flip_pending() & set(self._ecoqos_pids)
        except Exception:
            return 0
        done, n = [], 0
        for pid in pending:
            try:
                if self._set_ecoqos(pid, False):
                    done.append(pid); n += 1
            except Exception as _dx: DIAG.q("CoreMode._release_effect_flips#0", _dx)
        # 성공한 것만 대기열에서 뺀다. 실패분(핸들을 못 연 경우)은
        # 다음 사이클에 다시 시도한다 — 한 번 실패했다고 영영 놔두면
        # 그 프로세스는 '비교군 라벨 + EcoQoS 적용' 상태로 굳는다.
        try: EFFECT.flip_done(done)
        except Exception as _dx: DIAG.q("CoreMode._release_effect_flips#1", _dx)
        return n

    def _release_fg_tree(self):
        """★신규★ 포그라운드 프로세스 트리에 걸린 모든 강등을 즉시 해제.

        매 사이클 맨 앞에서 호출한다. 알트탭 직후를 생각하면 왜 필요한지
        분명하다. 백그라운드였을 때 EcoQoS(저클럭) + BELOW_NORMAL +
        메모리 우선순위 하향 + E코어 선호를 전부 맞은 앱이, 사용자가
        전환한 순간부터 '포그라운드인데 4중으로 강등된 상태'로 돌아간다.
        기존 코드는 _apply_ecoqos_bulk 가 도는 3~4 사이클마다, 그것도
        fg_pid 하나만 풀어줬다. 자식 프로세스는 영영 풀리지 않았다.
        """
        try:
            tree = FG.tree()
        except Exception:
            return 0
        if not tree:
            return 0
        n = 0
        # (1) EcoQoS 해제 — ★실패한 pid 는 장부에 남긴다★
        #     예전엔 실패해도 discard 했다. 핸들을 한 번 못 열면 그
        #     프로세스는 영원히 풀 기회를 잃었다. 이제 ECO.release 가
        #     성공을 확인했을 때만 지우고, 실패분은 다음 사이클에 다시
        #     시도한다. (장부는 LatencyOptimizer 와 공유 — 알트탭 한 번에
        #     양쪽에서 건 EcoQoS 가 전부 풀린다)
        try:
            n += ECO.release_pids(tree & set(ECO))
        except Exception as _dx: DIAG.q("CoreMode._release_fg_tree#0", _dx)
        # (2) 우선순위 클래스 복구
        for pid in tree & set(self._nice_orig.keys()):
            orig = self._nice_orig.pop(pid, None)
            if orig is None: continue
            try:
                psutil.Process(pid).nice(orig); n += 1
            except Exception as _dx: DIAG.q("CoreMode._release_fg_tree#1", _dx)
        # (3) 메모리 우선순위 / CPU Set / 타이머 가드 해제
        try:
            n += self.modern.release_pids(tree)
        except Exception as _dx: DIAG.q("CoreMode._release_fg_tree#2", _dx)
        return n

    def _revert_ecoqos_all(self):
        """모드 종료 시 EcoQoS 를 전부 해제한다."""
        try:
            return ECO.release_all()
        except Exception:
            return 0

    def _disable_gamedvr(self):
        """Disable GameDVR background recording. Real, measurable FPS impact."""
        try:
            import winreg
            # HKCU\System\GameConfigStore\GameDVR_Enabled = 0
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                    r"System\GameConfigStore",
                                    0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "GameDVR_Enabled", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
            except Exception as _dx: DIAG.q("CoreMode._disable_gamedvr#0", _dx)
            # HKCU\Software\Microsoft\Windows\CurrentVersion\GameDVR\AppCaptureEnabled = 0
            try:
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\GameDVR",
                    0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, "AppCaptureEnabled", 0, winreg.REG_DWORD, 0)
                winreg.CloseKey(key)
            except Exception as _dx: DIAG.q("CoreMode._disable_gamedvr#1", _dx)
            return True
        except Exception: return False

    def _pause_bg_services(self):
        """Pause non-critical Windows BG tasks for ~5min via service stop.
        Returns list of paused service names."""
        # Note: We DON'T disable services permanently — we use sc stop on
        # specific known-safe services that auto-restart later.
        # ★수정★ 대부분의 대상 서비스는 PAUSE 컨트롤을 받지 않아
        # sc pause 가 실패(1052/1061)한다. 그런데도 8 사이클마다(약 32초)
        # sc.exe 프로세스를 3개씩 띄우고 있었다 — 순수 낭비.
        # 세션당 1회만 시도한다.
        if self._services_paused_once:
            return []
        self._services_paused_once = True
        paused = []
        # Only target well-known safe services
        safe_services = [
            ("WSearch", "Windows Search"),
            ("DiagTrack", "Connected User Experiences and Telemetry"),
            ("SysMain", "SysMain (Superfetch)"),
        ]
        for svc, label in safe_services:
            try:
                r = subprocess_run(["sc", "pause", svc], timeout=2)
                if r and r.returncode == 0:
                    paused.append(label)
            except Exception as _dx: DIAG.q("CoreMode._pause_bg_services#0", _dx)
        if paused:
            # Schedule resume after 5 minutes
            def resume():
                for svc, _ in safe_services:
                    try: subprocess_run(["sc", "continue", svc], timeout=2)
                    except Exception as _dx: DIAG.q("CoreMode.resume#0", _dx)
            SCHED.call_later(300.0, resume)
            self.guard.record("bg_services", "multi", resume)
        return paused

    # ★삭제됨 — _clean_temp_files()★
    #
    # 임시 파일 자동 삭제를 최적화 사이클에서 완전히 들어냈다. 이유:
    #
    #  (1) C:\Windows\Prefetch 를 지우고 있었다. 프리페치는 Windows 가
    #      앱 시작을 빠르게 하려고 쌓아둔 데이터다. 지우면 다음 실행이
    #      "느려진다" — 최적화가 아니라 성능 저하다. 이 프로젝트는 이미
    #      '프리패치 삭제 같은 플라세보/역효과 기법은 쓰지 않는다'는
    #      원칙을 세웠는데 이 함수만 옛 코드로 남아 있었다.
    #  (2) C:\Windows\Temp 는 시스템 서비스 영역이다. 관리자 권한으로
    #      돌기 때문에 실제로 지워지고, Windows Update·드라이버 설치가
    #      중간 상태로 남겨둔 파일까지 날아갈 수 있다.
    #  (3) 판정 기준이 '수정 시각이 하루 지났으면 삭제'뿐이었다. 이건
    #      "안 쓰는 파일"을 전혀 보장하지 않는다. 며칠째 켜둔 IDE 의 세션
    #      파일, 중단된 설치 프로그램의 재개용 파일, Office/Adobe 자동복구
    #      파일이 전부 여기 해당한다 — 미저장 작업이 사라질 수 있다.
    #  (4) 이 앱의 다른 액션(EcoQoS·우선순위·전원 계획)은 전부 원복
    #      가능하다. 파일 삭제만 유일하게 되돌릴 수 없다.
    #  (5) 성능 점수(PIS)의 5개 컴포넌트(memory/bg_cpu/responsive/disk/
    #      thrashing) 어디에도 기여하지 않는다. 즉 측정되는 이득은 0인데
    #      위험만 있는 액션이었다.
    #  (6) 8초 예산 안에 %TEMP% 재귀 순회가 끝나지 않아 매번 다른 지점에서
    #      잘렸다 — 무엇이 지워질지 실행할 때마다 달랐다.
    #
    # 디스크 정리가 필요하면 저장소 탭에서 사용자가 직접 실행한다
    # (CleanupEngine.clean_temp — 대상은 %TEMP% 하나로 축소했다).

    def run_lite(self, progress_cb=None):
        """Lite Core — 5 quick, fully reversible actions."""
        steps = []
        before_used_mb, before_free_mb = self._measure_ram_used()
        before_cpu = psutil.cpu_percent(interval=0.3)

        def step(msg, fn):
            try:
                result = fn()
                steps.append({"label": msg, "result": result, "ok": True})
            except Exception as e:
                steps.append({"label": msg, "result": str(e), "ok": False})
            if progress_cb:
                try: progress_cb(steps[-1])
                except Exception as _dx: DIAG.q("CoreMode.step#0", _dx)

        # 1. Trim sleeping BG processes (conservative)
        step("Trim idle background processes",
             lambda: (lambda c, m: f"Trimmed {c} processes ({m}MB)")(
                 *self._trim_bg_processes(aggressive=False)))

        # 2. Apply EcoQoS to BG (Win11 22H2+)
        step("Apply EcoQoS to background apps",
             lambda: f"Applied to {self._apply_ecoqos_bulk()} processes"
                     if IS_WIN11_22H2 else "Win11 22H2+ required")

        # 3. Throttle BG CPU consumers (10s)
        step("Throttle background CPU usage",
             lambda: f"Throttled {self._throttle_bg_cpu(10, False)} processes (10s)")

        # 4. Boost foreground threads
        fg_name, fg_pid = get_foreground_info()
        step("Boost foreground app priority",
             lambda: self.executor.thread_burst(fg_pid))

        # 5. Foreground IO priority
        step("Elevate foreground I/O priority",
             lambda: self.executor.io_priority_boost(fg_pid))

        # Measure after (small wait for OS to settle)
        time.sleep(0.4)
        after_used_mb, after_free_mb = self._measure_ram_used()
        after_cpu = psutil.cpu_percent(interval=0.3)

        ram_freed_mb = max(0, before_used_mb - after_used_mb)
        cpu_delta = max(0, before_cpu - after_cpu)

        return {
            "mode": t("mode_name_lite"),
            "steps": steps,
            "before": {"ram_used_mb": before_used_mb, "ram_free_mb": before_free_mb,
                      "cpu_pct": before_cpu},
            "after":  {"ram_used_mb": after_used_mb, "ram_free_mb": after_free_mb,
                      "cpu_pct": after_cpu},
            "ram_freed_mb": ram_freed_mb,
            "cpu_delta": cpu_delta,
            "step_count": len(steps),
        }

    def run_hard(self, progress_cb=None):
        """Hard Core — 14 deeper actions with bigger measurable effect."""
        steps = []
        before_used_mb, before_free_mb = self._measure_ram_used()
        before_cpu = psutil.cpu_percent(interval=0.3)

        def step(msg, fn):
            try:
                result = fn()
                steps.append({"label": msg, "result": result, "ok": True})
            except Exception as e:
                steps.append({"label": msg, "result": str(e), "ok": False})
            if progress_cb:
                try: progress_cb(steps[-1])
                except Exception as _dx: DIAG.q("CoreMode.step#1", _dx)
            time.sleep(0.05)  # tiny delay for visual rhythm

        fg_name, fg_pid = get_foreground_info()

        # 1. Aggressive working set trim
        step("Deep memory trim (aggressive)",
             lambda: (lambda c, m: f"Trimmed {c} processes ({m}MB freed)")(
                 *self._trim_bg_processes(aggressive=True)))

        # 2. EcoQoS bulk
        step("EcoQoS for all background apps",
             lambda: f"Applied to {self._apply_ecoqos_bulk()} processes"
                     if IS_WIN11_22H2 else "Win11 22H2+ required")

        # 3. Throttle BG CPU (15s, aggressive)
        step("Throttle high-CPU background tasks",
             lambda: f"Throttled {self._throttle_bg_cpu(15, True)} processes (15s)")

        # 4. Pause Windows background services (5min)
        step("Pause Windows background services",
             lambda: f"Paused: {', '.join(self._pause_bg_services()) or 'none'} (5min)")

        # 5. Disable GameDVR
        step("Disable GameDVR background recording",
             lambda: "Disabled" if self._disable_gamedvr() else "Failed")

        # 7. FG thread burst
        step("Boost foreground threads",
             lambda: self.executor.thread_burst(fg_pid))

        # 8. FG IO priority
        step("Elevate foreground I/O",
             lambda: self.executor.io_priority_boost(fg_pid))

        # 9. MMCSS register if applicable
        snap = self.observer.last_snap or self.observer.snapshot()
        step("Register MMCSS scheduler hint",
             lambda: self.executor.mmcss_register(fg_pid, snap.get("fg_type", "general")))

        # 10. Affinity hint (hybrid CPU only)
        step("Apply hybrid CPU hint",
             lambda: self.executor.affinity_hint(fg_pid)
                     if IS_HYBRID else "Hybrid CPU not detected")

        # 11. Set High Performance power plan
        step("Switch to High Performance power",
             lambda: self._set_power_high())

        # 12. Empty system file cache (via SetSystemFileCacheSize)
        step("Trim system file cache",
             lambda: self._trim_system_cache())

        # 13. Clear DNS cache
        step("Flush DNS cache",
             lambda: self._flush_dns())

        # 14. Standby list flush (Win11)
        step("Compact standby memory list",
             lambda: self._compact_standby())

        time.sleep(0.5)
        after_used_mb, after_free_mb = self._measure_ram_used()
        after_cpu = psutil.cpu_percent(interval=0.3)

        ram_freed_mb = max(0, before_used_mb - after_used_mb)
        cpu_delta = max(0, before_cpu - after_cpu)

        return {
            "mode": t("mode_name_hard"),
            "steps": steps,
            "before": {"ram_used_mb": before_used_mb, "ram_free_mb": before_free_mb,
                      "cpu_pct": before_cpu},
            "after":  {"ram_used_mb": after_used_mb, "ram_free_mb": after_free_mb,
                      "cpu_pct": after_cpu},
            "ram_freed_mb": ram_freed_mb,
            "cpu_delta": cpu_delta,
            "step_count": len(steps),
        }

    def _set_power_high(self):
        try:
            # ── 원복용: 현재 활성 전원 구성표 GUID 를 먼저 저장한다.
            # 이미 저장돼 있으면(이번 세션에서 이미 바꿨으면) 덮어쓰지 않는다.
            # 이 단계가 없으면 사용자의 전원 계획이 High 로 영구히 남아
            # 노트북 배터리·발열이 악화된다(실손해 소지).
            if self._saved_power_scheme is None:
                try:
                    import re
                    q = subprocess_run(["powercfg", "/getactivescheme"], timeout=3)
                    if q and q.stdout:
                        m = re.search(
                            r"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}"
                            r"-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})", q.stdout)
                        if m:
                            cur = m.group(1).lower()
                            # 이미 High 였다면 굳이 원복할 필요가 없으니
                            # 균형(POWER_BAL)을 안전한 기본값으로 보관한다.
                            self._saved_power_scheme = (
                                POWER_BAL if cur == POWER_HIGH.lower() else cur)
                except Exception:
                    self._saved_power_scheme = POWER_BAL
            r = subprocess_run(["powercfg", "/setactive", POWER_HIGH], timeout=3)
            return "High Performance set" if r and r.returncode == 0 else "Failed"
        except Exception: return "Error"

    def _restore_power_scheme(self):
        """High Performance 로 바꾼 전원 계획을 원래 구성표로 되돌린다.
        모드 종료·앱 종료 시 호출된다. 멱등(idempotent): 저장된 값이
        없으면 아무것도 하지 않는다. 절대 예외를 던지지 않는다."""
        scheme = self._saved_power_scheme
        if not scheme:
            return
        try:
            subprocess_run(["powercfg", "/setactive", scheme], timeout=3)
        except Exception as _dx:
            DIAG.q("CoreMode._restore_power_scheme#0", _dx)
        finally:
            # 한 번 원복하면 표식을 지워 중복 실행을 막는다.
            self._saved_power_scheme = None

    def _trim_system_cache(self):
        """★비활성★ SetSystemFileCacheSize 로 시스템 파일 캐시를 비우던 동작.

        Creative 프로필에서 4 사이클마다(약 16초) 호출됐다. 영상/사진 편집처럼
        큰 파일을 반복해서 읽는 작업에서 파일 캐시를 계속 날리는 것은
        정확히 반대 방향의 최적화다 — 프리뷰 스크럽·프로젝트 로딩이 느려진다.
        (원본 코드는 아래 주석으로 보존)
        """
        return "Disabled (file cache purge hurt read-heavy work)"
        # --- 원본 보존 (사용 금지) ---------------------------------
        # try:
        #     sz = ctypes.c_size_t(-1)
        #     r = self.k.SetSystemFileCacheSize(sz, sz, 0)
        #     return "System cache trimmed" if r else "No-op"
        # except Exception: return "Unsupported"

    def _flush_dns(self):
        try:
            r = subprocess_run(["ipconfig", "/flushdns"], timeout=3)
            return "DNS cache cleared" if r and r.returncode == 0 else "Failed"
        except Exception: return "Error"

    def _compact_standby(self):
        """Purge Windows Standby List — 실제로 RAM을 확 빼주는 핵심 동작.
        EmptyWorkingSet은 페이지 폴트로 금방 돌아오지만, Standby List는
        즉시 free RAM으로 환원됨. RAMMap·Mem Reduct 등이 사용하는 방식.
        관리자 권한 + SeProfileSingleProcessPrivilege 필요.
        실패하면 조용히 폴백 (권한 부족 등)."""
        # ★수정(체감 성능 하락의 두 번째 주범)★
        # PurgeStandbyList 는 스탠바이 목록 = 윈도우 파일 캐시를 통째로
        # 버리는 동작이다. '여유 RAM' 숫자는 확 늘지만, 방금 버린 캐시를
        # OS 가 디스크에서 다시 읽어야 하므로 직후 몇 초~수십 초 동안
        # 디스크 큐가 치솟고 앱 전환·게임 로딩이 눈에 띄게 느려진다.
        # 12초마다 돌리면 시스템이 캐시를 회복할 틈이 없다.
        # → 실제로 메모리가 부족할 때만, 그리고 5분에 한 번만 수행한다.
        now_ts = time.time()
        try:
            vm_before = psutil.virtual_memory()
            before_avail_mb = vm_before.available // (1024 * 1024)
        except Exception:
            vm_before = None
            before_avail_mb = 0

        if vm_before is not None and vm_before.percent < 85.0:
            return "Skipped: enough free RAM (keeping cache is faster)"
        if now_ts - self._last_standby_purge < 300.0:
            return "Skipped: rate-limited (5 min interval)"
        self._last_standby_purge = now_ts

        # ── 1단계: 권한 활성화 (한 번만 enable되면 캐시됨)
        if not getattr(self, "_standby_priv_enabled", False):
            try:
                self._enable_privilege("SeProfileSingleProcessPrivilege")
                self._enable_privilege("SeIncreaseQuotaPrivilege")
                self._standby_priv_enabled = True
            except Exception as _dx:
                DIAG.q("CoreMode._compact_standby#0", _dx)

        # ── 2단계: NtSetSystemInformation으로 Standby List 비우기
        # SystemMemoryListInformation = 80
        # Commands: 2=EmptyWorkingSets, 3=FlushModifiedList,
        #           4=PurgeStandbyList, 5=PurgeLowPriorityStandbyList
        purged = False
        try:
            SystemMemoryListInformation = 80
            ntdll = ctypes.windll.ntdll
            # 우선 modified list flush (dirty 페이지 디스크로) — 부드러움
            try:
                cmd_flush = ctypes.c_int(3)
                ntdll.NtSetSystemInformation(
                    SystemMemoryListInformation,
                    ctypes.byref(cmd_flush),
                    ctypes.sizeof(cmd_flush))
            except Exception as _dx: DIAG.q("CoreMode._compact_standby#1", _dx)
            # 그 다음 standby list purge (RAM 확 빠지는 부분)
            cmd_purge = ctypes.c_int(4)
            status = ntdll.NtSetSystemInformation(
                SystemMemoryListInformation,
                ctypes.byref(cmd_purge),
                ctypes.sizeof(cmd_purge))
            purged = (status == 0)
        except Exception:
            purged = False

        # ── 3단계: OS가 페이지 회수할 시간 약간 줌
        try: time.sleep(0.4)
        except Exception as _dx: DIAG.q("CoreMode._compact_standby#2", _dx)

        # ── 4단계: 결과 측정
        try:
            vm_after = psutil.virtual_memory()
            after_avail_mb = vm_after.available // (1024 * 1024)
            freed_mb = max(0, after_avail_mb - before_avail_mb)
        except Exception:
            freed_mb = 0

        if purged:
            return f"Standby list purged ({freed_mb}MB returned)"
        elif freed_mb > 0:
            return f"Partial cleanup ({freed_mb}MB freed)"
        else:
            return "Requires admin privileges"

    def _enable_privilege(self, name: str) -> bool:
        """현재 프로세스 토큰에 특정 권한 활성화. admin 필요."""
        try:
            SE_PRIVILEGE_ENABLED = 0x2
            TOKEN_ADJUST_PRIVILEGES = 0x20
            TOKEN_QUERY = 0x8

            class LUID(ctypes.Structure):
                _fields_ = [("LowPart", wintypes.DWORD),
                           ("HighPart", wintypes.LONG)]

            class LUID_AND_ATTRIBUTES(ctypes.Structure):
                _fields_ = [("Luid", LUID),
                           ("Attributes", wintypes.DWORD)]

            class TOKEN_PRIVILEGES(ctypes.Structure):
                _fields_ = [("PrivilegeCount", wintypes.DWORD),
                           ("Privileges", LUID_AND_ATTRIBUTES * 1)]

            advapi = ctypes.windll.advapi32
            kernel = ctypes.windll.kernel32

            h_token = wintypes.HANDLE()
            if not advapi.OpenProcessToken(
                    kernel.GetCurrentProcess(),
                    TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY,
                    ctypes.byref(h_token)):
                return False

            luid = LUID()
            if not advapi.LookupPrivilegeValueW(
                    None, name, ctypes.byref(luid)):
                kernel.CloseHandle(h_token)
                return False

            tp = TOKEN_PRIVILEGES()
            tp.PrivilegeCount = 1
            tp.Privileges[0].Luid = luid
            tp.Privileges[0].Attributes = SE_PRIVILEGE_ENABLED

            ok = advapi.AdjustTokenPrivileges(
                h_token, False, ctypes.byref(tp), 0, None, None)
            kernel.CloseHandle(h_token)
            return bool(ok)
        except Exception:
            return False

    # ─────────────────────────────────────────────────────────────
    #  CONTINUOUS MODE — runs every ~5s while toggled on
    # ─────────────────────────────────────────────────────────────
    def is_running(self):
        with self._cont_lock:
            return self._cont_run

    def get_continuous_mode(self):
        with self._cont_lock:
            return self._cont_mode

    def start_continuous(self, mode, progress_cb=None, status_cb=None):
        """Start continuous optimization in 'lite' or 'hard' mode.
        progress_cb(step_dict) called for each individual action.
        status_cb(stats_dict) called once per cycle with cumulative stats.

        Lite 와 Hard 는 강도 차이일 뿐 잠금 관계가 아니다. 어떤 호출자든
        요청한 모드로 그대로 실행된다."""
        with self._cont_lock:
            if self._cont_run:
                return False
            self._cont_run = True
            self._cont_mode = mode
            self._cont_progress_cb = progress_cb
            self._cont_status_cb = status_cb
            self._cont_cycles = 0
            # ★사이클 번호를 0 으로 되돌리면 예약도 같이 비운다★
            # 안 비우면 지난 세션의 '다음 실행 시점'(수백 사이클 뒤)이
            # 남아 그 액션이 이번 세션 내내 한 번도 실행되지 않는다.
            self._due_next = {}
            self._cont_ram_freed_mb = 0
            self._cont_pis_history = []  # track PIS scores over time
            self._holdout_samples = []
            EFFECT.reset()
            self._bg_cpu_prev = {}
            self._bg_cores_hist = deque(maxlen=20)
            self._cpu_meas_n = 0
            self._sys_cpu_prev = None
            self._cont_ram_history = []  # session-wide RAM improvement %
            self._cont_cpu_history = []  # session-wide CPU improvement %
            # Take baseline (full AI measurement vector)
            psutil.cpu_percent(interval=None)
            time.sleep(0.3)
            self._baseline_full = self._measure_full()
            self._baseline_ram_mb = self._baseline_full["ram_used_mb"]
            self._baseline_cpu_pct = max(1.0, self._baseline_full["cpu_pct"])

        self._cont_thread = threading.Thread(target=self._cont_loop,
                                             daemon=True)
        self._cont_thread.start()
        return True

    def stop_continuous(self):
        with self._cont_lock:
            was_running = self._cont_run
            self._cont_run = False
        # 모드를 멈출 때 바꿔둔 전원 계획을 원래대로 되돌린다.
        self._restore_power_scheme()
        # ★추가★ 예전엔 EcoQoS 와 우선순위 강등이 그대로 남아
        # 모드를 꺼도 시스템이 계속 느린 상태였다. 전부 원복한다.
        try: self._revert_ecoqos_all()
        except Exception as _dx: DIAG.q("CoreMode.stop_continuous#0", _dx)
        try: self.modern.revert_all()
        except Exception as _dx: DIAG.q("CoreMode.stop_continuous#1", _dx)
        try: self._restore_all_nice()
        except Exception as _dx: DIAG.q("CoreMode.stop_continuous#2", _dx)
        # ★추가★ 지속형 포그라운드 부스트도 반드시 원복
        try: self.executor._release_fg_boost()
        except Exception as _dx: DIAG.q("CoreMode.stop_continuous#3", _dx)
        try: self._prune_timers()
        except Exception as _dx: DIAG.q("CoreMode.stop_continuous#4", _dx)
        return was_running

    def _cont_loop(self):
        """Main loop — runs cycle every ~3s (lite) or ~4s (hard).
        첫 3 사이클은 warm-up: 간격 1.5초로 짧게 → 시작 직후 RAM 확 빠지는 체감.
        그 이후는 정상 간격."""
        while True:
            with self._cont_lock:
                if not self._cont_run: break
                mode = self._cont_mode
                cyc = self._cont_cycles

            # Warm-up 구간: 첫 3 사이클은 매우 짧은 간격으로 강하게
            if cyc < 3:
                interval = 1.5
            else:
                interval = 3.0 if mode == "lite" else 4.0

            try:
                self._run_cycle(mode)
            except Exception as _dx:
                DIAG.q("CoreMode._cont_loop#0", _dx)

            # Sleep but check cancel flag every 0.3s
            slept = 0.0
            while slept < interval:
                with self._cont_lock:
                    if not self._cont_run: return
                time.sleep(0.3)
                slept += 0.3

    # 홀드아웃(대조군) 측정 주기. 0 이면 비활성(=기존 동작).
    # ★15 → 40★ 홀드아웃은 최적화를 전부 풀고 1초를 재는 사이클이다.
    # 즉 사용자 PC 를 주기적으로 '최적화 안 된 상태'로 되돌린다. 이걸
    # 효과 판정의 근거로 쓰지 않기로 한 이상(EffectEstimator 주석 참조),
    # 그 비용을 15사이클마다 치를 이유가 없다. PIS·보고서 기준값으로만
    # 쓰이므로 훨씬 드물게 돈다.
    HOLDOUT_EVERY = 40
    # 보관할 홀드아웃 표본 수(중앙값용)
    HOLDOUT_KEEP = 5

    def _release_all_soft(self):
        """홀드아웃 측정을 위해 되돌릴 수 있는 최적화를 전부 해제한다.
        전원 계획·GameDVR 처럼 시스템 전역 설정은 건드리지 않는다
        (되돌리는 비용이 크고 측정 구간이 짧다)."""
        for fn in (self._revert_ecoqos_all,
                   self.modern.revert_all,
                   self._restore_all_nice,
                   self.executor._release_fg_boost):
            try: fn()
            except Exception as _dx: DIAG.q("CoreMode._release_all_soft#0", _dx)

    def _run_holdout_cycle(self, mode):
        """최적화를 끈 상태의 대조군 표본을 만든다."""
        cyc = self._cont_cycles + 1
        try:
            ACTLOG.record("run", "Control measurement (optimizations off)",
                          "all optimizations released for 1.0s", cycle=cyc)
        except Exception as _dx:
            DIAG.q("CoreMode._run_holdout_cycle#0", _dx)
        step = {"label": "Control measurement (optimizations off)",
                "result": "sampling 1.0s", "ok": True, "cycle": cyc}
        if self._cont_progress_cb:
            try: self._cont_progress_cb(step)
            except Exception as _dx: DIAG.q("CoreMode._run_holdout_cycle#1", _dx)

        self._release_all_soft()
        # cpu_times 델타 기준점을 이 시점으로 다시 잡는다.
        self._bg_cpu_prev = {}
        self._sys_cpu_prev = None
        self._measure_full()
        time.sleep(1.0)
        sample = self._measure_full()

        self._holdout_samples.append(sample)
        if len(self._holdout_samples) > self.HOLDOUT_KEEP:
            self._holdout_samples.pop(0)
        # ★여기서 EFFECT 에 넣지 않는다★ 이 표본은 45초 전 다른 시간대의
        # 값이고, 게다가 방금 60개 프로세스의 절전을 푼 직후라 구조적으로
        # 편향돼 있다(밀린 일이 몰리는 구간). 효과 판정은 동시 대조군
        # (EffectEstimator)이 맡는다. 이 표본은 PIS·보고서용으로만 남긴다.

        with self._cont_lock:
            self._cont_cycles += 1
        if self._cont_status_cb:
            try:
                self._cont_status_cb(self._build_stats_snapshot(mode))
            except Exception as _dx: DIAG.q("CoreMode._run_holdout_cycle#2", _dx)

    def _learn_ctx(self):
        """학습 문맥 — 구체(앱)에서 일반(프로필) 순서.

        앱 이름을 앞에 두면 "마인크래프트에서는 듣는데 문서 작업 중엔
        아무 차이 없더라" 같은 앱별 답이 갈라져 나온다. 뒤의 프로필
        문맥은 처음 보는 앱의 출발점이 된다."""
        keys = []
        try:
            name = getattr(self, "_last_fg_name", "") or ""
            n = UsagePredictor._norm(name)
            if n:
                keys.append("app:" + n[:24])
        except Exception as _dx:
            DIAG.q("CoreMode._learn_ctx#0", _dx)
        keys.append("profile:" + str(getattr(self, "_last_profile_key", "any")))
        return keys

    def _learn_ok(self, action):
        """이 액션을 이번 사이클에 할지 학습기에 묻는다.

        ★보류(=하지 않음)도 데이터다★ 가끔 일부러 건너뛰어야
        '했을 때'와 '안 했을 때'를 비교할 수 있다. 매번 전부 하면
        효과를 영원히 알 수 없다.

        ★새로 걸지 않는 것만으로는 '안 한 상태'가 되지 않는다★
        보류로 뒤집히는 순간 이미 걸어둔 것을 실제로 되돌린다."""
        try:
            ok = LEARN.allow(self._learn_ctx(), action)
        except Exception:
            return True
        if not ok:
            # ★PATCH26★ 보류도 기록한다. 이게 없으면 사용자에게는
            # '액션이 사라진 것'으로만 보인다(고장과 구분 불가).
            self._skip(action, "learn_hold")
            try:
                if LEARN.needs_release(action):
                    self._undo_action(action)
            except Exception as _dx:
                DIAG.q("CoreMode._learn_ok#0", _dx)
        return ok

    # ── ★PATCH26★ 미실행 사유 기록 ────────────────────────────────
    def _skip(self, key, reason):
        """이번 사이클에 이 액션을 안 한 이유를 남긴다.

        사이클마다 한 줄로 모아 내보낸다(액션마다 즉시 쓰면 4초에
        10줄씩 쌓여 정작 실행 기록이 묻힌다)."""
        try:
            self._cycle_skips.setdefault(str(key), str(reason))
        except Exception as _dx:
            DIAG.q("CoreMode._skip#0", _dx)

    def _cond(self, key, ok, reason):
        """조건으로 걸러진 액션도 사유를 남기고 통과 여부를 돌려준다."""
        if not ok:
            self._skip(key, reason)
        return bool(ok)

    def _undo_action(self, action):
        """학습기가 이 액션을 보류로 뒤집었을 때 잔존 효과를 되돌린다.

        ★이게 없으면 학습 자체가 성립하지 않는다★ 이번 사이클에 새로
        걸지 않아도 지난 사이클에 걸어둔 EcoQoS·메모리 우선순위·nice·
        CPU 세트는 프로세스가 죽을 때까지 살아 있다. 그 상태로 모은
        '보류' 표본은 사실 '적용' 표본이라 두 무리의 차이가 사라진다.
        (600사이클 재현에서 진짜 0.30코어짜리 효과가 0.15 로 줄어
        표류 잡음에 묻혔다.)

        trim·standby 는 1회성 동작이라 되돌릴 것이 없다."""
        fn = {
            "ecoqos":       self._revert_ecoqos_all,
            "mem_priority": self.modern.revert_memory_priority,
            "affinity":     self.modern.revert_cpu_sets,
            "bg_throttle":  self._restore_all_nice,
        }.get(action)
        if fn is None:
            return 0
        try:
            return fn() or 0
        except Exception:
            return 0

    def _due(self, key, period):
        """고정 위상(cyc % N == k) 대신 '최소 간격 + 지터'.

        ★cyc % 3 == 0 과 cyc % 3 == 1 은 절대 같은 사이클에 오지 않는다★
        그러면 두 액션이 항상 서로의 잔여 효과 위에서만 평가돼 결과가
        교락된다(어느 쪽 공로인지 영원히 못 가린다). 위상을 흔들어
        액션 조합이 골고루 섞이게 한다."""
        try:
            period = int(period)
        except (TypeError, ValueError):
            return True
        if period <= 1:
            return True
        cyc = self._cont_cycles
        nx = self._due_next.get(key)
        if nx is None:
            nx = self._due_next[key] = cyc + LEARN.jitter(period)
        if cyc < nx:
            self._skip(key, "not_due")
            return False
        span = max(1, period // 3)
        self._due_next[key] = cyc + max(1, period - span) + LEARN.jitter(2 * span + 1)
        return True

    def _observe_effect(self):
        """추적 중인 프로세스들의 현재 사용률을 효과 측정기에 넘긴다.

        사용률 표에 없는 pid 는 '0 에 가깝다'는 뜻이므로 0 으로 기록한다
        (빼버리면 잘 눌린 프로세스만 통계에서 사라져 효과가 과소평가된다).
        죽은 프로세스는 전/후 비교가 성립하지 않으므로 추적에서 뺀다."""
        # ★패치23-b★ EcoQoS 가 하나도 안 걸려 있으면 이번 사이클은
        # 표본이 아니다. 홀드아웃(_release_all_soft)과 학습 보류
        # (_undo_action → _revert_ecoqos_all)는 걸어둔 것을 전부 푼다.
        # 그 구간의 값을 처리군 표본으로 세면 '적용했는데 효과가 없는
        # 것'처럼 보인다 — 패치22 캐리오버의 거울상이다.
        # '그냥 세기 / 블록 폐기 / 안 세기' 셋 중 안 세는 것만 정답이었다.
        # 근거: docs/ARCHITECTURE.md 함정 (32)
        if not self._ecoqos_pids:
            return
        rates = getattr(self, "_last_bg_rates", None) or {}
        for pid in EFFECT.tracked():
            r = rates.get(pid)
            if r is None:
                try:
                    if not psutil.pid_exists(pid):
                        EFFECT.forget(pid)
                        continue
                except Exception:
                    continue
                r = 0.0
            EFFECT.observe(pid, r)

    def _evidence(self, snap=None):
        """화면이 쓰는 '사실' 묶음. 전부 세거나 잰 값이고 비율이 아니다."""
        snap = snap or {}
        try:
            eco_n = len(ECO)
        except Exception:
            eco_n = 0
        try:
            vm = psutil.virtual_memory()
            avail_gb = vm.available / (1024 ** 3)
        except Exception:
            avail_gb = 0.0
        return {
            "eco_count":     eco_n,
            "bg_cores_now":  getattr(self, "_last_bg_cores", 0.0),
            "self_cpu_pct":  getattr(self, "_last_self_cpu_pct", 0.0),
            "self_cores":    getattr(self, "_last_self_cpu_pct", 0.0)
                             * self._cores / 100.0,
            "avail_gb":      avail_gb,
            "effect":        EFFECT.result(),
            "predict":       (PREDICT.predict(top=1) or [(None, 0.0)])[0],
            "predict_stats": PREDICT.stats(),
        }

    def _pis_reference(self):
        """PIS 의 기준값. 홀드아웃 표본이 있으면 그 중앙값을,
        없으면 세션 시작 baseline 을 쓴다."""
        if not self._holdout_samples:
            return self._baseline_full
        keys = ("ram_used_mb", "ram_pct", "bg_cpu_pct", "bg_cpu_norm",
                "cpu_pct", "cpu_queue", "disk_queue", "page_faults",
                "ctx_switches", "disk_busy", "hard_faults")
        ref = {}
        for k in keys:
            vals = [s.get(k) for s in self._holdout_samples
                    if s.get(k) is not None]
            if vals:
                ref[k] = _median(vals)
        ref["pdh_ok"] = all(s.get("pdh_ok") for s in self._holdout_samples)
        return ref

    def _build_stats_snapshot(self, mode):
        """홀드아웃 사이클에서도 UI 가 멈춰 보이지 않게 최신 통계를 낸다."""
        with self._cont_lock:
            hist = list(self._cont_pis_history)
            return {
                "cycles":             self._cont_cycles,
                "total_ram_freed_mb": self._cont_ram_freed_mb,
                "current_ram_mb":     self._baseline_ram_mb,
                "ram_improve_pct":    _median(getattr(self, "_cont_ram_history", [])),
                "cpu_improve_pct":    _median(getattr(self, "_cont_cpu_history", [])),
                "actions_this_cycle": 0,
                "mode":               mode,
                "profile_label":      t(getattr(self, "_last_profile_key",
                                                "profile_general")),
                "pis_score":          hist[-1] if hist else 50,
                "pis_avg":            int(sum(hist) / max(1, len(hist))) if hist else 50,
                "pis_dominant":       self._last_pis_dominant,
                "holdout":            True,
                **self._evidence(),
            }

    # Friendly name for the detected app type (for progress log)
    # ★수정★ 기존엔 영문 문자열을 그대로 저장해 화면(활성 프로필 / 프로필
    # 전환 토스트)에 한국어 모드에서도 "Gaming", "Multitask" 로 나왔다.
    # i18n 키만 저장하고, 표시 직전에 t() 로 번역한다.
    PROFILE_KEYS = {
        "game":     "profile_game",
        "creative": "profile_creative",
        "dev":      "profile_dev",
        "browser":  "profile_browser",
        "office":   "profile_office",
        "general":  "profile_general",
    }

    def _predicted_profile(self):
        """예측된 다음 앱이 '이미 떠 있는데 아직 포그라운드가 아닌' 상태
        (=로딩 중)면 그 앱의 프로필을 미리 고른다.

        ★왜 이 조건인가★ 예측만으로 프로필을 바꾸면 틀렸을 때 엉뚱한
        앱을 위해 튜닝한다. '그 앱이 실제로 실행되기 시작했다'는 사실을
        하나 더 확인하면, 남는 위험은 '조금 이르게 준비한다' 뿐이다.
        게임은 로딩·셰이더 컴파일 구간이 제일 버벅이는데, 포그라운드로
        올라온 뒤에 준비하면 그 구간은 이미 지나간 뒤다.
        """
        try:
            if not SETTINGS.get("ai_learn_apps", True):
                return None
            p = PREDICT.confident(0.5)
            if not p:
                return None
            name = p[0]
            fg = UsagePredictor._norm(getattr(self, "_last_fg_name", ""))
            if not name or name == fg:
                return None
            running = False
            for inf in PROC_CACHE.info_list_nowait():
                if UsagePredictor._norm(inf.get("name") or "") == name:
                    running = True
                    break
            if not running:
                return None
            kind = self.observer._classify_fg(name)
            return None if kind == "general" else (kind, name, p[1])
        except Exception:
            return None

    def _detect_profile(self, snap):
        """Decide which profile to apply based on foreground app + system load."""
        fg_type = snap.get("fg_type", "general")
        # If user is idle (low CPU, no input), conserve resources
        if (snap.get("cpu_pct", 0) < 8.0 and
            snap.get("threads_ratio", 1.0) < 0.5 and
            fg_type == "general"):
            return "idle"
        return fg_type  # game / creative / dev / browser / office / general

    def _run_cycle(self, mode):
        """Execute one optimization cycle.

        Lite Core (FREE tier — limited):
          - 3 actions per cycle, conservative thresholds
          - No deep memory trim, no temp file cleanup
          - No bg service pause, no GameDVR disable
          - Profile-aware but uses gentle settings

        Hard Core (full):
          - 6-9 actions per cycle, aggressive thresholds
          - Profile-specific deep tuning (Game/Creative/Working/Multitask)
          - Temp file cleanup, bg service pause every N cycles
          - Power plan switch, MMCSS, IO priority deep tuning
          - Auto-detects foreground app and adapts in real time
        """
        before_used_mb = self._measure_ram_used()[0]
        cycle_steps = []
        # ★PATCH26★ 이번 사이클의 실행/미실행 집계
        self._cycle_skips = {}
        self._cycle_ran = []

        def step(label, fn):
            try:
                result = fn()
                s = {"label": label, "result": result, "ok": True,
                     "cycle": self._cont_cycles + 1}
            except Exception as e:
                s = {"label": label, "result": str(e), "ok": False,
                     "cycle": self._cont_cycles + 1}
            cycle_steps.append(s)
            # ★PATCH26★ 화면 콜백과 별개로 기록을 남긴다. 콜백은 창이
            # 닫혀 있거나 다른 화면이면 버려지지만 기록은 남아야 한다.
            try:
                ACTLOG.record("run" if s["ok"] else "fail", label,
                              s.get("result", ""), ok=s["ok"],
                              cycle=s.get("cycle", 0))
                self._cycle_ran.append(str(label)[:40])
            except Exception as _dx:
                DIAG.q("CoreMode.step#2", _dx)
            if self._cont_progress_cb:
                try: self._cont_progress_cb(s)
                except Exception as _dx: DIAG.q("CoreMode.step#3", _dx)

        # ══════════════════════════════════════════════════════════
        # ★신규★ 홀드아웃(대조군) 사이클
        # ══════════════════════════════════════════════════════════
        # 기존 PIS 는 '지금 상태'를 '모드를 켠 순간의 상태'와 비교했다.
        # 그건 우리 효과가 아니라 그 사이 사용자가 무엇을 했는지를 잰다.
        # 예: Hard Core 를 켜고 게임을 실행하면 RAM 이 3GB 늘어 점수가
        # 37점으로 곤두박질친다. 앱이 가장 열심히 일하는 순간에 가장
        # 낮은 점수가 나오는 구조였다. 대표님이 "효과가 안 나온다"고
        # 느낀 근본 원인이 이것이다.
        #
        # 인과를 재려면 대조군이 필요하다. N 사이클마다 한 번은
        # 최적화를 전부 풀고 그 상태를 측정한다. 점수는
        #   '최적화 켠 상태' vs '방금 잰 최적화 끈 상태'
        # 를 비교한다. 이게 "이 앱이 실제로 효과가 있는가"에 대한
        # 유일하게 정직한 답이다.
        #
        # 비용: HOLDOUT_EVERY 사이클마다 약 1초간 최적화가 풀린다.
        #       Hard(4초 주기) 기준 60초에 한 번. 끄려면 아래를 0 으로.
        if self.HOLDOUT_EVERY and (self._cont_cycles + 1) % self.HOLDOUT_EVERY == 0:
            try:
                self._run_holdout_cycle(mode)
            except Exception as _dx:
                DIAG.q("CoreMode._run_cycle#0", _dx)
            return

        fg_name, fg_pid = get_foreground_info()
        # ★신규★ 포그라운드 프로세스 트리 갱신 → 그 트리에 걸린 강등을
        # 먼저 전부 풀어준다. 이 두 줄이 이번 개선의 핵심이다.
        # 이게 없으면 아래의 모든 액션이 사용자가 지금 쓰는 앱의 자식
        # 프로세스를 백그라운드로 오인해 계속 깎아내린다.
        try:
            FG.refresh(fg_pid, fg_name)
            self._release_fg_tree()
        except Exception as _dx: DIAG.q("CoreMode._run_cycle#1", _dx)
        # ★패치23-b★ 측정 무결성은 액션 스케줄과 무관해야 한다.
        self._release_effect_flips()
        snap = self.observer.snapshot()
        # 학습 문맥과 사용 패턴이 쓰는 값 — 액션 결정보다 먼저 정해둔다.
        self._last_fg_name = fg_name or ""
        detected = self._detect_profile(snap)
        # 지금 쓰는 앱이 특별할 게 없을 때만 예측을 쓴다. 실제 포그라운드
        # 앱이 있으면 언제나 그쪽이 이긴다 — 예측이 현실을 덮지 않는다.
        self._predicted = None
        if detected == "general":
            pr = self._predicted_profile()
            if pr:
                detected, self._predicted = pr[0], pr
        profile_key = self.PROFILE_KEYS.get(detected, "profile_general")
        profile_label = t(profile_key)
        cyc = self._cont_cycles + 1

        # Always log: what we detected (every cycle, so user sees it adapt)
        # Friendly app name shortened
        app_short = fg_name.replace(".exe", "") if fg_name else "?"
        if self._predicted:
            step(t("predict_prewarm", app=self._predicted[1][:18],
                   pct=int(self._predicted[2] * 100)),
                 lambda: f"Profile: {profile_label}")
        else:
            step(f"Detected: {app_short[:18]} → {profile_label} mode",
                 lambda: f"Profile: {profile_label}")

        # ──────────────────────────────────────────────────────────
        #  LITE CORE — FREE TIER (~40% of Hard's effect)
        # ──────────────────────────────────────────────────────────
        if mode == "lite":
            # Action 1: Foreground boost (always)
            step("Boost foreground app threads",
                 lambda: self.executor.thread_burst(fg_pid))

            # Action 2: Light memory trim
            # ★수정★ 55% → 80%. 55% 는 평시 대부분의 PC 가 항상 넘는 값이라
            # 사실상 '매 사이클 워킹셋 강제 축출'이 되어 하드 폴트를 유발했다.
            if (self._cond("trim", snap.get("ram_pct", 0) > 80, "ram_ok")
                    and self._learn_ok("trim")):
                step("Light memory trim",
                     lambda: (lambda c, m: f"Trimmed {c} processes ({m}MB)")(
                         *self._trim_bg_processes(aggressive=False)))

            # Action 3: BG throttle every 2nd cycle (기존 3rd → 더 자주)
            if self._due("bg_throttle", 2) and self._learn_ok("bg_throttle"):
                step("Lower background CPU usage (8s)",
                     lambda: f"Throttled {self._throttle_bg_cpu(8, False)} processes")

            # Action 4 (NEW for Lite 40%): Light EcoQoS every 3rd cycle (기존 4th)
            if (self._cond("ecoqos", IS_WIN11_22H2, "os_unsupported")
                    and self._due("ecoqos", 3)
                    and self._learn_ok("ecoqos")):
                step("Light energy-save (background)",
                     lambda: f"Applied to {self._apply_ecoqos_bulk()} processes")

            # Action 4.5 (NEW): 메모리 우선순위 하향 — EmptyWorkingSet 대체
            # 페이지를 강제로 뺏지 않고 '부족하면 여기부터 회수하라'고
            # 표시만 하므로 하드 폴트가 생기지 않는다. Lite 에서도 안전.
            if self._due("mem_priority", 3) and self._learn_ok("mem_priority"):
                step("Background memory priority",
                     lambda: self.modern.lower_bg_memory_priority(fg_pid, 12))

            # Action 5 (NEW): Standby list purge every 5th cycle (가벼운 체감용)
            # — RAM 확 빠지는 시각 효과. 안전성 위해 lite는 5사이클마다만
            if self._due("standby", 20) and self._learn_ok("standby"):
                step("Reclaim standby memory",
                     lambda: self._compact_standby())

            # Still NO: IO priority, MMCSS, temp cleanup, service pause,
            # power plan, profile-specific tuning, GameDVR disable.
            # That's the FREE tier — basic optimization only.

        # ──────────────────────────────────────────────────────────
        #  HARD CORE — full power, profile-aware
        # ──────────────────────────────────────────────────────────
        else:
            # Action 1: Aggressive memory trim (lower threshold)
            # ★수정★ 45% → 75%. 45% 개입은 항상 참이라 사실상 무조건 실행.
            if (self._cond("trim", snap.get("ram_pct", 0) > 75, "ram_ok")
                    and self._learn_ok("trim")):
                step("Deep memory trim (aggressive)",
                     lambda: (lambda c, m: f"Trimmed {c} processes ({m}MB freed)")(
                         *self._trim_bg_processes(aggressive=True)))

            # Action 1.5 (Hard): Standby list purge
            # ★수정★ 3 사이클(~12초) → 15 사이클(~60초). 게다가 함수 내부에
            # RAM 85% 미만이면 skip / 5분 레이트리밋이 걸려 있다.
            if self._due("standby", 15) and self._learn_ok("standby"):
                step("Reclaim standby memory",
                     lambda: self._compact_standby())

            # Action 2: EcoQoS for background apps (Win11 22H2+)
            # ★수정★ 매 사이클 전체 프로세스 워크 + OpenProcess 25회는 과했다.
            # 이제 적용분은 추적되므로 4 사이클마다 신규 대상만 훑는다.
            if (self._cond("ecoqos", IS_WIN11_22H2, "os_unsupported")
                    and self._due("ecoqos", 4)
                    and self._learn_ok("ecoqos")):
                step("Energy-save mode for background apps",
                     lambda: f"Applied to {self._apply_ecoqos_bulk()} processes")

            # Action 3: Foreground thread boost
            step("Boost foreground app threads",
                 lambda: self.executor.thread_burst(fg_pid))

            # Action 4: BG CPU throttle (longer duration than Lite)
            step("Lower background CPU usage (12s)",
                 lambda: f"Throttled {self._throttle_bg_cpu(12, True)} processes")

            # ─── ★신규★ 최신 API 액션 (Hard 공통) ────────────────
            # (a) 하이브리드 CPU: 포그라운드 P코어 / 백그라운드 E코어 선호
            if (self._cond("affinity", IS_HYBRID, "no_hybrid_cpu")
                    and self._due("affinity", 3)
                    and self._learn_ok("affinity")):
                step("P/E core scheduling hint",
                     lambda: self.modern.apply_core_split(fg_pid))

            # (b) 백그라운드 메모리 우선순위 하향 (EmptyWorkingSet 대체)
            if self._due("mem_priority", 2) and self._learn_ok("mem_priority"):
                step("Background memory priority",
                     lambda: self.modern.lower_bg_memory_priority(fg_pid, 25))

            # (c) 백그라운드의 시스템 타이머 하이재킹 차단 (Win11)
            if IS_WIN11 and cyc % 6 == 1:
                step("Block timer-resolution hijacking",
                     lambda: self.modern.block_timer_hijack(fg_pid))

            # 죽은 pid 정리 (60초마다)
            if time.time() - self._modern_prune_t > 60.0:
                self._modern_prune_t = time.time()
                try: self.modern.prune_dead()
                except Exception as _dx: DIAG.q("CoreMode._run_cycle#2", _dx)

            # ─── PROFILE-SPECIFIC ACTIONS ─
            if detected == "game":
                # Gaming: maximize input responsiveness
                step("Gaming I/O priority boost",
                     lambda: self.executor.io_priority_boost(fg_pid))
                step("Gaming scheduler hint (MMCSS)",
                     lambda: self.executor.mmcss_register(fg_pid, "game"))
                # ★신규★ GPU 큐 우선순위 — 프레임타임 편차 감소
                step("GPU queue priority",
                     lambda: self.modern.gpu_priority_boost(fg_pid))
                if cyc % 2 == 0:
                    step("Gaming: switch to High Performance power",
                         lambda: self._set_power_high())

            elif detected == "creative":
                # Creative: render priority + audio
                step("Creative I/O elevation",
                     lambda: self.executor.io_priority_boost(fg_pid))
                step("Creative audio scheduling",
                     lambda: self.executor.mmcss_register(fg_pid, "creative"))
                # ★신규★ 렌더/프리뷰도 GPU 큐 우선순위 이득이 있다
                step("GPU queue priority",
                     lambda: self.modern.gpu_priority_boost(fg_pid))
                if cyc % 4 == 0:
                    step("Creative: trim disk cache",
                         lambda: self._trim_system_cache())

            elif detected == "dev":
                # Dev: build performance + IO
                step("Dev I/O priority boost",
                     lambda: self.executor.io_priority_boost(fg_pid))

            elif detected == "browser":
                # Browser: balance, lighter touch
                step("Browser balance tuning",
                     lambda: self.executor.io_priority_boost(fg_pid))

            else:
                # General/office: baseline IO
                step("Foreground I/O priority",
                     lambda: self.executor.io_priority_boost(fg_pid))

            if cyc % 8 == 0:
                step("Pause Windows background services (5min)",
                     lambda: f"Paused: {', '.join(self._pause_bg_services()) or 'none'}")

            if cyc == 1:  # First cycle only
                step("Disable GameDVR background recording",
                     lambda: "Disabled" if self._disable_gamedvr() else "Failed")

        # ★PATCH26★ 이번 사이클 요약 — 한 줄로 "무엇을 했고 무엇을 미뤘나"
        try:
            ACTLOG.cycle_summary(cyc, self._cycle_ran, self._cycle_skips)
        except Exception as _dx:
            DIAG.q("CoreMode._run_cycle#3", _dx)

        # Measure after — full AI vector
        # ★수정★ 사이클당 블로킹 대기 총합이 0.85s 를 넘었다(여기 0.3 +
        # _measure_full 0.25 + _trim 0.3). 4초 사이클의 20% 이상을 sleep 으로
        # 쓰면서 그 사이 스레드는 GIL 을 잡았다 놨다 반복한다. 절반으로 줄임.
        time.sleep(0.15)
        current_full = self._measure_full()
        after_used_mb = current_full["ram_used_mb"]
        after_cpu = current_full["cpu_pct"]

        # Compute AI Performance Improvement Score
        # ★수정★ 기준값은 '세션 시작 시점'이 아니라 '가장 최근에 측정한
        # 최적화 OFF 상태(홀드아웃)'다. 홀드아웃 표본이 아직 없으면
        # 시작 시점 baseline 으로 폴백한다.
        ref = self._pis_reference()
        pis = self._compute_pis(ref, current_full)
        self._last_pis_dominant = pis["dominant"]
        self._last_pis_measured = pis.get("measured", 0)
        # ★수정★ _compute_pis 는 등급 문구 키(tier_key)를 이미 계산해 돌려준다.
        # GUI 가 점수만 받아 자기 임계값으로 등급을 다시 매기고 있었던 탓에
        # '측정 데이터 부족(pis_tier_nodata)' 상태가 화면에 절대 나오지 않고
        # 대신 '악화'로 표시됐다. 여기서 키를 그대로 보관해 GUI 가 쓰게 한다.
        self._last_pis_tier = pis.get("tier_key", "pis_tier_nodata")

        cycle_freed_mb = max(0, before_used_mb - after_used_mb)
        with self._cont_lock:
            self._cont_ram_freed_mb += cycle_freed_mb
            self._cont_cycles += 1
            self._cont_pis_history.append(pis["score"])
            # Keep only last 50 for memory
            if len(self._cont_pis_history) > 50:
                self._cont_pis_history.pop(0)

            # ─── ★전면 재작성★ 성능 % 계산 ────────────────────
            #
            # 기존 계산식이 무엇이었는지 남겨둔다:
            #   freed_pct    = 누적 회수 RAM / baseline * 100   (단조 증가)
            #   mem_quality  = PIS 메모리 컴포넌트 * 0.5 ...
            #   recent_pct   = 이번 사이클 회수량 ...
            #   ram_inst     = freed_pct*1.4 + mem_quality*0.6 + recent_pct*0.8
            #   action_bonus = min(6.0, 액션개수 * 0.8)
            #   cpu_inst     = cpu_quality*0.6 + action_bonus*1.0
            #
            # 문제가 셋이었다.
            #  (1) freed_pct 는 '누적' 회수량이라 시간이 갈수록 무조건
            #      올라간다. 시스템이 나빠져도 숫자는 계속 오른다.
            #  (2) cpu_inst 에 action_bonus, 즉 '액션을 몇 개 실행했나'가
            #      직접 들어간다. 아무 효과가 없어도 실행만 하면 오른다.
            #  (3) 원본 주석에 "튜닝 목표: 일반 사용 12~18%" 라고 적혀
            #      있다. 보여줄 숫자를 먼저 정하고 식을 역산한 것이다.
            #  결과적으로 화면 숫자는 항상 좋아 보이는데 체감은 나빠지는,
            #  문제를 숨기는 계기판이 됐다.
            #
            # 이제 실제로 잰 값만 쓴다. 나빠졌으면 음수가 나온다.
            #  RAM  : 시작 시점 사용량 대비 현재 사용량의 실제 변화율
            #  CPU  : 시작 시점 백그라운드 CPU 대비 현재의 실제 변화율
            #         (포그라운드 CPU 는 사용자가 무엇을 하느냐에 따라
            #          달라지므로 우리 성과가 아니다 — 백그라운드만 본다)
            # 단일 사이클 값은 노이즈가 크므로 세션 히스토리의 '중앙값'
            # 으로 대표값을 낸다(평균은 스파이크 한 번에 끌려간다).
            ram_now = after_used_mb

            # ★수정★ 여기도 기준을 홀드아웃(최적화 OFF 실측)으로 바꾼다.
            # 시작 시점 고정 baseline 은 사용자가 앱을 하나 더 켜는 순간
            # 무의미해진다.
            base_ram = max(1, int(ref.get("ram_used_mb",
                                          self._baseline_ram_mb) or 1))
            ram_inst = (base_ram - ram_now) / base_ram * 100.0

            base_bg = ref.get("bg_cpu_pct", ref.get("bg_cpu_norm", 0.0)) or 0.0
            cur_bg  = current_full.get("bg_cpu_pct", 0.0)
            # ★수정★ 작은 분모 증폭 + 자기 자신 포함으로 -50% 가 고정
            # 표시되던 계산. bg_rel_change 가 코어 단위 하한과 데드밴드를
            # 적용하고, 잴 부하가 없었으면 None → 0 으로 정직하게 둔다.
            # 동시 대조군 관측 갱신(처리군·비교군 모두)
            try:
                self._observe_effect()
            except Exception as _dx:
                DIAG.q("CoreMode._run_cycle#4", _dx)
            # 이번 사이클의 결과를 학습기에 넘긴다(백그라운드 부하, 낮을수록 좋음)
            try:
                LEARN.commit(getattr(self, "_last_bg_cores", None))
            except Exception as _dx:
                DIAG.q("CoreMode._run_cycle#5", _dx)
            _r = self.bg_rel_change(base_bg, cur_bg, self._cores,
                                    self.bg_noise_cores())
            cpu_inst = 0.0 if _r is None else _r
            # 잴 부하가 있었던 사이클이 하나도 없으면 화면에 0.0% 대신
            # "—" 를 띄운다. '효과 0' 과 '잴 게 없었다' 는 다른 말이다.
            if _r is not None:
                self._cpu_meas_n = getattr(self, "_cpu_meas_n", 0) + 1

            # 물리적으로 말이 되는 범위로만 자른다(부호는 보존).
            ram_inst = max(-50.0, min(50.0, ram_inst))
            cpu_inst = max(-100.0, min(100.0, cpu_inst))

            if not hasattr(self, "_cont_ram_history"):
                self._cont_ram_history = []
                self._cont_cpu_history = []
            self._cont_ram_history.append(ram_inst)
            self._cont_cpu_history.append(cpu_inst)
            if len(self._cont_ram_history) > 100:
                self._cont_ram_history.pop(0)
                self._cont_cpu_history.pop(0)

            ram_improve_pct = _median(self._cont_ram_history)
            cpu_improve_pct = _median(self._cont_cpu_history)

            # Average PIS over session
            avg_pis = int(sum(self._cont_pis_history) /
                         max(1, len(self._cont_pis_history)))

            # Cache for _refresh_improve_card_from_state
            # ★수정★ 번역된 문자열을 캐시하면 언어를 바꿔도 옛 언어가 남는다.
            #        키를 저장하고 표시 직전에 t() 로 번역한다.
            self._last_profile_key = profile_key
            # 사용 패턴 관측 — 앱 이름과 전환 시각만 본다(설정에서 끌 수 있음).
            try:
                if SETTINGS.get("ai_learn_apps", True):
                    PREDICT.observe(self._last_fg_name)
            except Exception as _dx:
                DIAG.q("CoreMode._run_cycle#6", _dx)

            stats = {
                "cycles":              self._cont_cycles,
                "total_ram_freed_mb":  self._cont_ram_freed_mb,
                "this_cycle_freed_mb": cycle_freed_mb,
                "current_ram_mb":      ram_now,
                "current_cpu_pct":     after_cpu,
                "baseline_ram_mb":     self._baseline_ram_mb,
                "baseline_cpu_pct":    self._baseline_cpu_pct,
                "ram_improve_pct":     ram_improve_pct,
                "cpu_improve_pct":     cpu_improve_pct,
                "ram_improve_inst":    ram_inst,
                "cpu_improve_inst":    cpu_inst,
                **self._evidence(current_full),
                # 비율의 근거가 된 실제 부하(코어 단위)와 우리 자신의 비용.
                # 퍼센트만 보면 분모가 얼마였는지 알 수 없다.
                "bg_cores_base":       base_bg * self._cores / 100.0,
                "bg_cores_now":        cur_bg * self._cores / 100.0,
                "self_cpu_pct":        current_full.get("self_cpu_pct", 0.0),
                "cpu_measurable":      getattr(self, "_cpu_meas_n", 0) > 0,
                "actions_this_cycle":  len(cycle_steps),
                "mode":                mode,
                "detected_profile":    detected,
                "profile_label":       profile_label,
                "pis_score":           pis["score"],
                "pis_avg":             avg_pis,
                "pis_components":      pis["components"],
                "pis_dominant":        pis["dominant"],
                "pis_tier_key":        pis["tier_key"],
                "pis_measured":        pis.get("measured", 0),
                "pis_pdh_ok":          pis.get("pdh_ok", False),
                "holdout_samples":     len(self._holdout_samples),
            }

        if self._cont_status_cb:
            try: self._cont_status_cb(stats)
            except Exception as _dx: DIAG.q("CoreMode._run_cycle#7", _dx)


def subprocess_run(args, timeout=3):
    """Run subprocess silently with timeout."""
    import subprocess
    try:
        return subprocess.run(args, creationflags=CREATE_NO_WINDOW,
                            capture_output=True, timeout=timeout, text=True)
    except Exception:
        return None


# ============================================================================
# CLEANUP / HEALTH / STARTUP / PROCESS managers
# ============================================================================
class CleanupEngine:
    @staticmethod
    def scan_temp_files():
        """Scan temp locations. Optimized: Use scandir for reduced SSD reads."""
        results = {}
        locations = {
            "User Temp":    os.environ.get("TEMP", ""),
            "Recent Files": os.path.join(os.environ.get("APPDATA", ""),
                                        "Microsoft", "Windows", "Recent"),
            "Edge Cache":   os.path.join(os.environ.get("LOCALAPPDATA", ""),
                                        "Microsoft", "Edge", "User Data",
                                        "Default", "Cache"),
            "Chrome Cache": os.path.join(os.environ.get("LOCALAPPDATA", ""),
                                        "Google", "Chrome", "User Data",
                                        "Default", "Cache"),
        }
        
        def recursive_scan(dirpath, limit=10000):
            count, size = 0, 0
            try:
                for entry in os.scandir(dirpath):
                    if count >= limit: break
                    if entry.is_file(follow_symlinks=False):
                        try:
                            size += entry.stat(follow_symlinks=False).st_size
                            count += 1
                        except (OSError, PermissionError) as _dx: DIAG.q("CleanupEngine.recursive_scan#0", _dx)
                    elif entry.is_dir(follow_symlinks=False):
                        sub_count, sub_size = recursive_scan(entry.path, limit - count)
                        count += sub_count; size += sub_size
                        if count >= limit: break
            except Exception as _dx: DIAG.q("CleanupEngine.recursive_scan#1", _dx)
            return count, size
        
        for label, path in locations.items():
            if not path:
                results[label] = {"path": path, "count": 0, "size": 0}
                continue
            try:
                if os.path.exists(path):
                    count, size = recursive_scan(path)
                    results[label] = {"path": path, "count": count, "size": size}
                else:
                    results[label] = {"path": path, "count": 0, "size": 0}
            except Exception:
                results[label] = {"path": path, "count": 0, "size": 0}
        return results

    @staticmethod
    def clean_temp():
        """Clean temp files. Optimized: Use scandir to reduce SSD access."""
        results = {"cleaned": 0, "freed": 0, "errors": 0}
        cutoff = time.time() - 86400
        
        def recursive_clean(dirpath):
            try:
                for entry in os.scandir(dirpath):
                    if entry.is_file(follow_symlinks=False):
                        try:
                            st = entry.stat(follow_symlinks=False)
                            if st.st_mtime > cutoff: continue
                            os.remove(entry.path)
                            results["cleaned"] += 1
                            results["freed"] += st.st_size
                        except (OSError, PermissionError):
                            results["errors"] += 1
                        except Exception:
                            results["errors"] += 1
                    elif entry.is_dir(follow_symlinks=False):
                        recursive_clean(entry.path)
            except Exception as _dx: DIAG.q("CleanupEngine.recursive_clean#0", _dx)
        
        # ★대상 축소★ 예전에는 C:\Windows\Temp 와 C:\Windows\Prefetch 도
        #   지웠다. 프리페치 삭제는 다음 앱 실행을 느리게 만드는 역효과이고,
        #   Windows\Temp 는 시스템 서비스가 쓰는 영역이라 업데이트·드라이버
        #   설치 중간 상태가 깨질 수 있다. 사용자 %TEMP% 하나만 남긴다.
        for path in [os.environ.get("TEMP", "")]:
            if not path or not os.path.exists(path): continue
            recursive_clean(path)
        return results

    @staticmethod
    def empty_recycle_bin():
        try:
            shell32 = ctypes.windll.shell32
            r = shell32.SHEmptyRecycleBinW(None, None, 0x0001 | 0x0002 | 0x0004)
            return "Recycle Bin emptied" if r == 0 else f"Failed ({r})"
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def get_recycle_bin_info():
        """(바이트, 항목수). 못 읽으면 (0, 0).

        PATCH25_RELEASE_GATE: 확인 창에 '무엇이 얼마나' 지워지는지 적기 위해
        항목 수까지 읽는다. SHQUERYRBINFO 는 원래 둘 다 준다.
        """
        try:
            shell32 = ctypes.windll.shell32

            class SHQUERYRBINFO(ctypes.Structure):
                _fields_ = [("cbSize", ctypes.c_ulong),
                            ("i64Size", ctypes.c_int64),
                            ("i64NumItems", ctypes.c_int64)]
            info = SHQUERYRBINFO()
            info.cbSize = ctypes.sizeof(info)
            r = shell32.SHQueryRecycleBinW(None, ctypes.byref(info))
            if r == 0:
                return int(info.i64Size), int(info.i64NumItems)
        except Exception as _dx:
            DIAG.q("CleanupEngine.get_recycle_bin_info#0", _dx)
        return 0, 0

    @staticmethod
    def get_recycle_bin_size():
        try:
            shell32 = ctypes.windll.shell32
            class SHQUERYRBINFO(ctypes.Structure):
                _fields_ = [("cbSize", ctypes.c_ulong),
                           ("i64Size", ctypes.c_int64),
                           ("i64NumItems", ctypes.c_int64)]
            info = SHQUERYRBINFO()
            info.cbSize = ctypes.sizeof(info)
            r = shell32.SHQueryRecycleBinW(None, ctypes.byref(info))
            if r == 0: return info.i64Size
        except Exception as _dx: DIAG.q("CleanupEngine.get_recycle_bin_size#0", _dx)
        return 0


class HealthAnalyzer:
    @staticmethod
    def analyze(snap, history):
        cpu_avg = sum(h.get("cpu", 0) for h in history) / max(1, len(history))
        ram_avg = sum(h.get("ram", 0) for h in history) / max(1, len(history))
        cpu_score = max(0, 100 - cpu_avg)
        ram_score = max(0, 100 - ram_avg)
        disk_score = max(0, 100 - snap.get("disk_pct", 0))
        uptime_h = snap.get("uptime_hours", 0)
        uptime_score = 100 if uptime_h < 72 else max(0, 100 - (uptime_h - 72) / 2)
        overall = int(cpu_score * 0.30 + ram_score * 0.30 +
                     disk_score * 0.25 + uptime_score * 0.15)
        status = ("Excellent" if overall >= 85 else
                 "Good" if overall >= 70 else
                 "Fair" if overall >= 50 else "Poor")
        issues = []
        if cpu_avg > 60: issues.append(("warning", f"High avg CPU ({cpu_avg:.0f}%)"))
        if ram_avg > 75: issues.append(("warning", f"High avg RAM ({ram_avg:.0f}%)"))
        if snap.get("disk_pct", 0) > 85:
            issues.append(("critical", f"Disk almost full ({snap['disk_pct']:.0f}%)"))
        if uptime_h > 168: issues.append(("info", f"Uptime > 1 week ({uptime_h:.0f}h)"))
        if snap.get("page_faults", 0) > 1500:
            issues.append(("warning", "High page fault rate"))
        recs = []
        if snap.get("disk_pct", 0) > 80: recs.append("Run Storage cleanup")
        if ram_avg > 70: recs.append("Run Hard Core to free memory")
        if uptime_h > 72: recs.append("Restart Windows to refresh state")
        if cpu_avg > 50: recs.append("Review high-CPU processes in Apps tab")
        return {
            "overall_score": overall, "status": status,
            "cpu_score": int(cpu_score), "ram_score": int(ram_score),
            "disk_score": int(disk_score), "uptime_score": int(uptime_score),
            "cpu_avg": cpu_avg, "ram_avg": ram_avg,
            "disk_pct": snap.get("disk_pct", 0),
            "uptime_hours": uptime_h, "issues": issues,
            "recommendations": recs,
        }


class StartupManager:
    REGISTRY_KEYS = None  # populated lazily

    @classmethod
    def _keys(cls):
        if cls.REGISTRY_KEYS is None:
            import winreg
            cls.REGISTRY_KEYS = [
                (winreg.HKEY_CURRENT_USER,
                 r"Software\Microsoft\Windows\CurrentVersion\Run", "User"),
                (winreg.HKEY_LOCAL_MACHINE,
                 r"Software\Microsoft\Windows\CurrentVersion\Run", "All Users"),
                (winreg.HKEY_LOCAL_MACHINE,
                 r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run",
                 "All Users (WOW64)"),
            ]
        return cls.REGISTRY_KEYS

    @staticmethod
    def list_startup_apps():
        import winreg
        apps = []
        for hive, path, scope in StartupManager._keys():
            try:
                key = winreg.OpenKey(hive, path, 0, winreg.KEY_READ)
                i = 0
                while True:
                    try:
                        name, value, _ = winreg.EnumValue(key, i)
                        apps.append({
                            "name": name, "cmd": value, "scope": scope,
                            "hive": hive, "path": path,
                            "safe_to_disable": StartupManager._safe(name, value),
                        })
                        i += 1
                    except OSError: break
                winreg.CloseKey(key)
            except Exception as _dx: DIAG.q("StartupManager.list_startup_apps#0", _dx)
        return apps

    # ★수정★ 예전 _safe 는 이름·명령줄에 대해 단순 부분문자열 검사였다.
    #   'intel' 이 'IntelliJ' 에, 'amd' 가 'AMDeploy' 같은 이름에 걸려
    #   멀쩡한 항목이 '중요'로 잠기고, 반대로 목록에 없는 진짜 중요한
    #   항목은 전부 삭제 가능으로 표시됐다.
    #   길고 모호하지 않은 토큰은 부분문자열로, 짧고 흔한 토큰은
    #   단어 경계로 나눠 검사한다.
    _CRITICAL_SUBSTR = (
        "nvidia", "realtek", "antivirus", "defender", "windows security",
        "onedrive", "synaptics", "bitdefender", "avast", "kaspersky",
        "eset", "malwarebytes", "securityhealth", "audiodg", "rtkaud",
    )
    _CRITICAL_TOKEN = ("intel", "amd", "audio", "hp", "dell", "lenovo")

    @staticmethod
    def _safe(name, cmd):
        import re
        text = f"{name or ''} {cmd or ''}".lower()
        for k in StartupManager._CRITICAL_SUBSTR:
            if k in text:
                return False
        toks = set(re.findall(r"[a-z0-9]+", text))
        for k in StartupManager._CRITICAL_TOKEN:
            if k in toks:
                return False
        return True

    # ─── 백업/복원 ─────────────────────────────────────────────
    # ★가장 중요한 수정★ 예전 disable() 은 winreg.DeleteValue 로
    #   레지스트리 값을 그냥 지웠다. 백업도 복원 함수도 없어서
    #   '비활성화'가 아니라 영구 삭제였고, 설정 탭의 '전체 되돌리기'
    #   (guard.rollback_all) 대상도 아니었다. 사용자가 되돌리려면
    #   그 프로그램을 재설치하는 수밖에 없었다.
    #   이제 지우기 전에 값·타입·위치를 startup_backup.json 에 적고,
    #   restore() 로 원래 자리에 그대로 복원한다.
    _HIVE_MAP = None

    @classmethod
    def _hives(cls):
        if cls._HIVE_MAP is None:
            import winreg
            cls._HIVE_MAP = {"HKCU": winreg.HKEY_CURRENT_USER,
                             "HKLM": winreg.HKEY_LOCAL_MACHINE}
        return cls._HIVE_MAP

    @staticmethod
    def _hive_name(hive):
        for k, v in StartupManager._hives().items():
            if v == hive:
                return k
        return None

    @staticmethod
    def _backup_path():
        d = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        try:
            d.mkdir(parents=True, exist_ok=True)
        except Exception as _dx:
            DIAG.q("StartupManager._backup_path#0", _dx)
        return d / "startup_backup.json"

    @staticmethod
    def _load_backup():
        try:
            p = StartupManager._backup_path()
            if p.exists():
                with open(p, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    return [e for e in data if isinstance(e, dict)]
        except Exception as _dx:
            DIAG.q("StartupManager._load_backup#0", _dx)
        return []

    @staticmethod
    def _save_backup(entries):
        p = StartupManager._backup_path()
        tmp = p.with_suffix(".tmp")
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(entries, f, ensure_ascii=False, indent=1)
            os.replace(str(tmp), str(p))
            return True
        except Exception:
            try:
                os.remove(str(tmp))
            except Exception as _dx:
                DIAG.q("StartupManager._save_backup#0", _dx)
            return False

    @staticmethod
    def list_disabled():
        """이 앱이 지워둔 시작프로그램 목록(복원 대상)."""
        return StartupManager._load_backup()

    @staticmethod
    def _same(e, hive_name, path, name):
        return (e.get("name") == name and e.get("path") == path
                and e.get("hive") == hive_name)

    @staticmethod
    def disable(hive, path, name):
        """값을 백업한 뒤 삭제한다. 백업에 실패하면 삭제하지 않는다."""
        import winreg
        hname = StartupManager._hive_name(hive)
        try:
            key = winreg.OpenKey(hive, path, 0,
                                 winreg.KEY_READ | winreg.KEY_SET_VALUE)
        except Exception:
            return False
        try:
            try:
                value, vtype = winreg.QueryValueEx(key, name)
            except Exception:
                value, vtype = None, winreg.REG_SZ
            if value is not None and hname:
                entries = [e for e in StartupManager._load_backup()
                           if not StartupManager._same(e, hname, path, name)]
                entries.append({"name": name, "cmd": value,
                                "type": int(vtype), "hive": hname,
                                "path": path,
                                "ts": time.strftime("%Y-%m-%d %H:%M:%S")})
                if not StartupManager._save_backup(entries):
                    return False
            winreg.DeleteValue(key, name)
            return True
        except Exception:
            return False
        finally:
            try:
                winreg.CloseKey(key)
            except Exception as _dx:
                DIAG.q("StartupManager.disable#0", _dx)

    @staticmethod
    def restore(entry):
        """백업해둔 항목을 원래 레지스트리 위치에 되돌린다."""
        import winreg
        hive = StartupManager._hives().get(entry.get("hive"))
        path = entry.get("path")
        name = entry.get("name")
        if hive is None or not path or not name:
            return False
        try:
            try:
                key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
            except FileNotFoundError:
                key = winreg.CreateKey(hive, path)
            try:
                winreg.SetValueEx(
                    key, name, 0,
                    int(entry.get("type") or winreg.REG_SZ),
                    entry.get("cmd", ""))
            finally:
                try:
                    winreg.CloseKey(key)
                except Exception as _dx:
                    DIAG.q("StartupManager.restore#0", _dx)
        except Exception:
            return False
        remain = [e for e in StartupManager._load_backup()
                  if not StartupManager._same(e, entry.get("hive"),
                                              path, name)]
        StartupManager._save_backup(remain)
        return True


class ProcessManager:
    @staticmethod
    def kill(pid):
        try:
            p = psutil.Process(pid)
            name = p.name().lower()
            if name in SYSTEM_WHITELIST:
                return False, "System process — cannot kill"
            if any(k in name for k in SAFE_KEYWORDS):
                return False, f"Protected: {name}"
            p.terminate()
            try: p.wait(timeout=2)
            except psutil.TimeoutExpired: p.kill()
            return True, f"Terminated: {name}"
        except psutil.NoSuchProcess: return False, "Not found"
        except psutil.AccessDenied: return False, "Access denied"
        except Exception as e: return False, str(e)

    @staticmethod
    def boost(pid):
        try:
            p = psutil.Process(pid)
            name = p.name().lower()
            if not is_safe_to_modify(name):
                return False, f"Cannot modify: {name}"
            orig = p.nice()
            p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
            def restore():
                try: psutil.Process(pid).nice(orig)
                except Exception as _dx: DIAG.q("ProcessManager.restore#0", _dx)
            # ★수정★ threading.Timer 는 기본이 비데몬이다. 사용자가
            # 부스트를 누른 직후 앱을 닫으면 종료가 최대 5초 지연됐다.
            SCHED.call_later(5.0, restore)
            return True, f"Boosted {name}"
        except Exception as e: return False, str(e)

    @staticmethod
    def throttle(pid):
        try:
            p = psutil.Process(pid)
            name = p.name().lower()
            if not is_safe_to_modify(name):
                return False, f"Cannot modify: {name}"
            orig = p.nice()
            p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
            def restore():
                try: psutil.Process(pid).nice(orig)
                except Exception as _dx: DIAG.q("ProcessManager.restore#1", _dx)
            # ★수정★ 위와 동일 — 종료가 최대 10초 지연됐다.
            SCHED.call_later(10.0, restore)
            return True, f"Throttled {name}"
        except Exception as e: return False, str(e)


# ============================================================================
# AUTO OPTIMIZER LOOP
# ============================================================================
class AutoOptimizer:
    def __init__(self, observer, ai, policy, guard, executor, log_fn, cb):
        self.observer = observer
        self.ai = ai; self.policy = policy
        self.guard = guard; self.executor = executor
        self.log = log_fn; self.cb = cb
        self._run = False; self._busy = False
        self._lk = threading.Lock()
        self.cycle = 0; self.last_state = "IDLE"
        self.last_actions = []; self.last_lpi = 0
        self.last_anomaly = False

    def start(self):
        if self._run: return
        self._run = True
        threading.Thread(target=self._loop, daemon=True).start()

    def stop(self):
        self._run = False
        # ★추가★ Auto 루프가 걸어둔 EcoQoS 를 해제한다.
        try: self.executor.revert_ecoqos_all()
        except Exception as _dx: DIAG.q("AutoOptimizer.stop#0", _dx)
        try: self.executor._release_fg_boost()
        except Exception as _dx: DIAG.q("AutoOptimizer.stop#1", _dx)

    def _loop(self):
        psutil.cpu_percent(interval=None)
        # Longer initial delay (was 3s) so GUI fully renders and the first
        # process_iter walk happens in the cache-warm thread, NOT here.
        time.sleep(8.0)
        while self._run:
            t0 = time.time()
            try: self._tick()
            except Exception as e: self.log(f"err: {e}")
            elapsed = time.time() - t0
            time.sleep(max(1.0, AUTO_INTERVAL - elapsed))

    # ★신규★ CoreMode 연속 모드가 도는 동안 Auto 루프의 '실행'을 멈춘다.
    # 기존엔 두 시스템이 완전히 독립적으로 같은 프로세스의 nice / IO /
    # EcoQoS 를 건드렸다. AutoOptimizer(6초)가 어떤 프로세스를
    # BELOW_NORMAL 로 내린 직후 CoreMode(3~4초)가 그 값을 '원래값'으로
    # 기록해버리면, 복구를 해도 BELOW_NORMAL 로 되돌아간다. 서로의 복구
    # 기록을 오염시키는 구조였다.
    # 관측·상태 분류·LPI 갱신(UI 표시용)은 그대로 두고 액션만 멈춘다.
    core_mode = None

    def _core_busy(self):
        try:
            return bool(self.core_mode and self.core_mode.is_running())
        except Exception:
            return False

    def _tick(self):
        self.cycle += 1
        snap = self.observer.snapshot()
        try: FG.refresh(snap.get("fg_pid"), snap.get("fg_name"))
        except Exception as _dx: DIAG.q("AutoOptimizer._tick#0", _dx)
        state, conf, _ = self.ai.classify(snap)
        self.last_state = state
        lpi = compute_lpi(snap)
        self.last_lpi = lpi
        self.last_anomaly = self.ai.detect_anomaly(lpi)
        record_perf(snap["cpu_pct"], snap["ram_pct"], lpi)
        actions = [] if self._core_busy() else self.policy.decide(state, snap)
        self.last_actions = actions
        if not actions:
            self.cb({"status": "Idle", "state": state, "lpi": lpi,
                    "snap": snap, "actions": []})
            return
        with self._lk:
            if self._busy: return
            self._busy = True
        threading.Thread(target=self._execute,
                        args=(actions, snap, state, lpi), daemon=True).start()

    def _execute(self, actions, snap, state, lpi):
        try:
            results = []
            for a in actions:
                results.append((a, self.executor.execute(
                    a, snap["fg_pid"], snap["fg_type"])))
            self.cb({"status": "Active", "state": state, "lpi": lpi,
                    "snap": snap, "actions": [a for a, _ in results],
                    "results": results})
        finally:
            with self._lk: self._busy = False


# ============================================================================
# GAME AUTO-DETECT — Auto-start Hard Core when game launches
# ============================================================================
class GameAutoDetect:
    """Background watcher that auto-starts Hard Core when a game is detected.

    Runs every 4s, checks foreground app. If it's a game and Core is not
    running, auto-starts Hard Core. When user exits game, optionally stops.
    """

    def __init__(self, observer, core_mode):
        self.observer = observer
        self.core_mode = core_mode
        self.enabled = False
        self.auto_stop_on_exit = True
        self._thread = None
        self._stop = threading.Event()
        self._was_game = False
        self._auto_started = False  # only auto-stop what we auto-started

    def start(self):
        if self.enabled: return
        self.enabled = True
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.enabled = False
        self._stop.set()

    def _loop(self):
        # Initial delay so we don't collide with other background threads
        # firing process walks at startup
        self._stop.wait(6.0)
        while not self._stop.is_set():
            try:
                snap = self.observer.snapshot()
                is_game = (snap.get("fg_type") == "game")

                if is_game and not self._was_game:
                    # Game just launched
                    if not self.core_mode.is_running():
                        self.core_mode.start_continuous("hard")
                        self._auto_started = True
                elif not is_game and self._was_game:
                    # Game just closed
                    if (self.auto_stop_on_exit and self._auto_started
                        and self.core_mode.is_running()
                        and self.core_mode.get_continuous_mode() == "hard"):
                        self.core_mode.stop_continuous()
                        self._auto_started = False

                self._was_game = is_game
            except Exception as _dx: DIAG.q("GameAutoDetect._loop#0", _dx)
            self._stop.wait(4.0)


# ============================================================================
# SCHEDULER — Run optimizations at scheduled times (e.g. 3 AM cleanup)
# ============================================================================
class Scheduler:
    """Time-based scheduled optimization runner.

    Supports daily schedules (e.g., daily at 03:00) for:
      - Temp file cleanup
      - Memory trim
      - Health report
    """

    def __init__(self, core_mode, cleanup_cls, observer):
        self.core_mode = core_mode
        self.cleanup_cls = cleanup_cls
        self.observer = observer
        self.enabled = False
        # Schedule: list of dicts {"hour": int, "minute": int,
        #                          "task": "cleanup"|"trim"|"hard_5min"}
        self.schedule = []
        self._last_run = {}  # task → date string (avoid double-run)
        self._thread = None
        self._stop = threading.Event()
        self.last_action = None  # for status display

    def add_schedule(self, hour, minute, task):
        self.schedule.append({"hour": hour, "minute": minute, "task": task})

    def remove_schedule(self, idx):
        if 0 <= idx < len(self.schedule):
            self.schedule.pop(idx)

    def start(self):
        if self.enabled: return
        self.enabled = True
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.enabled = False
        self._stop.set()

    def _loop(self):
        while not self._stop.is_set():
            try:
                now = datetime.now()
                date_key = now.strftime("%Y-%m-%d")
                for entry in self.schedule:
                    h, m, task = entry["hour"], entry["minute"], entry["task"]
                    # Within 1-min window of scheduled time
                    if now.hour == h and now.minute == m:
                        last_key = f"{task}_{date_key}_{h:02d}{m:02d}"
                        if self._last_run.get(task) != last_key:
                            self._run_task(task)
                            self._last_run[task] = last_key
            except Exception as _dx: DIAG.q("Scheduler._loop#0", _dx)
            self._stop.wait(30.0)  # check every 30s

    def _run_task(self, task):
        try:
            # ★삭제됨★ "cleanup"(자동 임시파일 정리) 작업.
            #   사용자가 자리에 없는 새벽 3시에 확인 없이 파일을 영구
            #   삭제하는 동작이었다. 디스크 정리는 저장소 탭에서 사용자가
            #   직접 눌러 실행한다. 기존에 등록된 "cleanup" 일정이 있으면
            #   아무 것도 하지 않고 무시한다(예약 목록에서 지우면 사라짐).
            if task == "cleanup":
                self.last_action = (datetime.now(),
                    "Skipped: automatic temp cleanup was removed")
            elif task == "trim":
                # Trim background working sets via CoreMode helper
                c, m = self.core_mode._trim_bg_processes(aggressive=True)
                self.last_action = (datetime.now(),
                    f"Memory trim: {c} processes, {m}MB freed")
            elif task == "hard_5min":
                # 5분 Hard 버스트 실행 후 자동 정지
                if not self.core_mode.is_running():
                    self.core_mode.start_continuous("hard")
                    SCHED.call_later(300.0, self.core_mode.stop_continuous)
                    self.last_action = (datetime.now(),
                        "5-min Hard Core burst started")
        except Exception as e:
            self.last_action = (datetime.now(), f"Failed: {e}")


# ============================================================================
# BATTERY SAVER — Auto-EcoQoS when on battery
# ============================================================================
class BatterySaver:
    """Watches power state. When laptop on battery (not plugged in),
    automatically applies EcoQoS to background apps every 30s.

    When plugged back in, releases EcoQoS (lets system go full power)."""

    def __init__(self, observer, executor):
        self.observer = observer
        self.executor = executor
        self.enabled = False
        self._thread = None
        self._stop = threading.Event()
        self._was_on_battery = False
        self.last_action = None

    def start(self):
        if self.enabled: return
        self.enabled = True
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self):
        self.enabled = False
        self._stop.set()

    def _loop(self):
        # Initial delay so we don't collide with other background threads
        self._stop.wait(10.0)
        while not self._stop.is_set():
            try:
                snap = self.observer.snapshot()
                # ★패치23★ 배터리든 아니든, 매 tick 포그라운드 트리는
                # 먼저 풀어준다. 이 루프가 30초마다 최대 10개씩 EcoQoS 를
                # 쌓는데 해제는 충전기를 꽂을 때뿐이었다.
                try:
                    FG.refresh(snap.get("fg_pid"), snap.get("fg_name"))
                except Exception as _dx: DIAG.q("BatterySaver._loop#0", _dx)
                release_fg_ecoqos()
                on_battery = snap.get("on_battery", False)
                bat_pct = snap.get("battery_pct", 100)

                if on_battery:
                    # Apply EcoQoS to background (every cycle to keep them suppressed)
                    if IS_WIN11_22H2:
                        result = self.executor.apply_ecoqos(snap.get("fg_pid"))
                        self.last_action = (datetime.now(),
                            f"On battery ({bat_pct:.0f}%) — {result}")
                    self._was_on_battery = True
                else:
                    if self._was_on_battery:
                        # ★수정(절전 고착 버그)★
                        # 기존 코드는 전원을 다시 꽂으면 로그 문자열만
                        # "power saving released" 로 바꾸고, 정작 걸어둔
                        # EcoQoS 는 하나도 해제하지 않았다. 배터리로 쓰는
                        # 동안 30초마다 최대 10개씩 쌓인 저클럭 지정이
                        # 충전기를 꽂은 뒤에도 그대로 남아, 콘센트에
                        # 연결했는데 노트북이 계속 느린 상태가 됐다.
                        n = 0
                        try: n = self.executor.revert_ecoqos_all() or 0
                        except Exception as _dx: DIAG.q("BatterySaver._loop#1", _dx)
                        self.last_action = (datetime.now(),
                            f"Plugged in — released {n} processes")
                        self._was_on_battery = False
            except Exception as _dx: DIAG.q("BatterySaver._loop#2", _dx)
            self._stop.wait(30.0)


# ============================================================================
# RAM LEAK DETECTOR — Detects monotonically growing memory usage per process
# ============================================================================
class RamLeakDetector:
    """Tracks per-process memory over time. Flags processes whose memory
    grows monotonically over a window (likely memory leak).

    Sampling: every 60s, reuses Observer's process cache (no extra iter).
    Window: last 30 samples (= 30 minutes).
    Memory cost: ~2MB max (50 procs × 30 samples).
    """

    SAMPLE_INTERVAL_S = 60.0
    WINDOW_SAMPLES    = 30          # 30 minutes
    MIN_RSS_MB        = 100         # ignore small processes
    GROWTH_WARN_MB    = 200         # 30min growth → warn
    GROWTH_DANGER_MB  = 500         # 30min growth → danger
    GROWTH_CRITICAL_MB = 1024       # 30min growth → critical
    MAX_HISTORY_PROCS = 50          # cap memory footprint

    def __init__(self, observer):
        self.observer = observer
        # pid → deque of (timestamp, rss_mb)
        self._history = {}
        # pid → name (cache)
        self._names = {}
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self.enabled = False
        self.alerts = []                # current active alerts
        self._auto_handler = None       # callback for auto-action

    def set_auto_handler(self, fn):
        """Register callback fn(pid, name) to auto-trim."""
        self._auto_handler = fn

    def start(self):
        if self.enabled: return
        self.enabled = True
        self._stop.clear()
        threading.Thread(target=self._loop, daemon=True).start()

    def stop(self):
        self.enabled = False
        self._stop.set()

    def _loop(self):
        # initial delay so observer has data AND startup is past
        self._stop.wait(15.0)
        while not self._stop.is_set():
            try:
                self._sample()
                self._detect()
            except Exception as _dx: DIAG.q("RamLeakDetector._loop#0", _dx)
            self._stop.wait(self.SAMPLE_INTERVAL_S)

    def _sample(self):
        """Take memory snapshot of all running processes (reuse cache)."""
        procs = self.observer.get_processes()
        now = time.time()
        with self._lock:
            seen_pids = set()
            for p in procs:
                pid = p.get("pid")
                name = (p.get("name") or "").lower()
                if not pid or not name: continue
                if name in SYSTEM_WHITELIST: continue
                if pid == SELF_PID: continue      # ★추가★ 자기 자신 제외
                mem_info = p.get("memory_info")
                if not mem_info: continue
                rss_mb = mem_info.rss / (1024 * 1024)
                if rss_mb < self.MIN_RSS_MB: continue

                seen_pids.add(pid)
                self._names[pid] = name
                if pid not in self._history:
                    self._history[pid] = deque(maxlen=self.WINDOW_SAMPLES)
                self._history[pid].append((now, rss_mb))

            # Cleanup: remove dead pids
            dead = [pid for pid in self._history if pid not in seen_pids]
            for pid in dead:
                self._history.pop(pid, None)
                self._names.pop(pid, None)

            # Cap total tracked procs (keep the largest ones)
            if len(self._history) > self.MAX_HISTORY_PROCS:
                sorted_pids = sorted(
                    self._history.items(),
                    key=lambda x: -x[1][-1][1] if x[1] else 0
                )
                keep = dict(sorted_pids[:self.MAX_HISTORY_PROCS])
                self._history = keep

    def _detect(self):
        """Analyze history for monotonic growth patterns."""
        new_alerts = []
        with self._lock:
            for pid, samples in self._history.items():
                if len(samples) < 5: continue  # need at least 5 min of data

                rss_values = [s[1] for s in samples]
                first_mb = rss_values[0]
                last_mb = rss_values[-1]
                duration_min = (samples[-1][0] - samples[0][0]) / 60.0
                growth_mb = last_mb - first_mb

                # Must have grown noticeably
                if growth_mb < self.GROWTH_WARN_MB: continue

                # ★수정(오탐 억제)★
                # 기존 조건은 "30분 안에 200MB 이상 늘었고 하락 구간이
                # 30% 미만" 이 전부였다. 그런데 게임이 레벨을 로딩하거나,
                # 브라우저가 탭을 열거나, IDE 가 인덱싱을 시작하면 몇 분
                # 만에 수 GB 가 정상적으로 늘어난다. 전부 'critical 누수'로
                # 표시됐고, 자동 정리가 켜져 있으면 정상 동작 중인 앱의
                # 워킹셋을 강제로 비워 오히려 버벅이게 만들었다.
                #
                # 누수의 특징은 '한 번 치솟는 것'이 아니라 '계속 오르는 것'
                # 이다. 그래서 창을 반으로 갈라 두 구간 모두에서 올랐는지
                # 본다. 로딩 스파이크는 앞 구간만 오르고 뒤는 평평하므로
                # 여기서 걸러진다.
                if duration_min < 10.0: continue      # 최소 10분 관측
                mid = len(rss_values) // 2
                first_half_growth = rss_values[mid] - rss_values[0]
                second_half_growth = rss_values[-1] - rss_values[mid]
                # 뒤 구간이 사실상 멈췄으면 로딩 스파이크 → 누수 아님
                if second_half_growth < self.GROWTH_WARN_MB * 0.25:
                    continue
                # 앞 구간만 폭증하고 뒤는 미미한 형태도 제외
                if first_half_growth > 0 and \
                        second_half_growth < first_half_growth * 0.20:
                    continue

                # Must be roughly monotonic (allow small dips)
                decreases = sum(1 for i in range(1, len(rss_values))
                              if rss_values[i] < rss_values[i-1] - 50)
                # Reject if too many dips (= not a leak)
                if decreases > len(rss_values) * 0.3: continue

                # Determine severity
                if growth_mb >= self.GROWTH_CRITICAL_MB:
                    severity = "critical"
                elif growth_mb >= self.GROWTH_DANGER_MB:
                    severity = "danger"
                else:
                    severity = "warn"

                new_alerts.append({
                    "pid":          pid,
                    "name":         self._names.get(pid, "?"),
                    "growth_mb":    int(growth_mb),
                    "current_mb":   int(last_mb),
                    "duration_min": int(duration_min),
                    "severity":     severity,
                })

        # Sort by growth desc
        new_alerts.sort(key=lambda x: -x["growth_mb"])
        self.alerts = new_alerts[:10]

        # auto-trim handler
        if self._auto_handler:
            for alert in self.alerts:
                if alert["severity"] in ("danger", "critical"):
                    try: self._auto_handler(alert["pid"], alert["name"])
                    except Exception as _dx: DIAG.q("RamLeakDetector._detect#0", _dx)

    def get_alerts(self):
        return list(self.alerts)

    def get_tracked_count(self):
        with self._lock:
            return len(self._history)


# ============================================================================
# SESSION HISTORY — Persistent session records (Reports tab)
# ============================================================================
class SessionHistory:
    """Stores Hard/Lite Core sessions to JSON, supports summary aggregation.

    Storage: %APPDATA%/OMEGA_X/sessions.json
    Retention: 90 days (auto-pruned)
    Size: ~200 bytes per session → 90 days ≈ 18KB
    """

    MAX_DAYS = 90

    def __init__(self):
        self._dir = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        try: self._dir.mkdir(parents=True, exist_ok=True)
        except Exception as _dx: DIAG.q("SessionHistory.__init__#0", _dx)
        self._path = self._dir / "sessions.json"
        self._lock = threading.Lock()
        self._cache = self._load()
        self._current = None  # session in progress
        self._prune()

    def _load(self):
        try:
            if self._path.exists():
                with open(self._path, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception as _dx: DIAG.q("SessionHistory._load#0", _dx)
        return []

    def _save(self):
        """Atomic write — write to temp, then rename."""
        tmp = self._path.with_suffix(".json.tmp")
        try:
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self._cache, f, ensure_ascii=False)
            tmp.replace(self._path)
        except Exception as _dx: DIAG.q("SessionHistory._save#0", _dx)

    def _prune(self):
        """Drop sessions older than MAX_DAYS."""
        cutoff = (datetime.now() - timedelta(days=self.MAX_DAYS)).strftime("%Y-%m-%d")
        with self._lock:
            self._cache = [s for s in self._cache if s.get("date", "") >= cutoff]
            self._save()

    def start_session(self, mode):
        """Mark session start. Stats added at end_session."""
        self._current = {
            "mode":         mode,
            "start_ts":     time.time(),
            "start_time":   datetime.now().strftime("%H:%M"),
            "date":         datetime.now().strftime("%Y-%m-%d"),
        }

    def end_session(self, stats):
        """Persist session with final stats from CoreMode."""
        if not self._current: return
        end_ts = time.time()
        record = {
            "date":          self._current["date"],
            "start_time":    self._current["start_time"],
            "end_time":      datetime.now().strftime("%H:%M"),
            "duration_min":  int((end_ts - self._current["start_ts"]) / 60),
            "mode":          self._current["mode"],
            "cycles":        stats.get("cycles", 0),
            "ram_freed_mb":  stats.get("total_ram_freed_mb", 0),
            "pis_avg":       stats.get("pis_avg", 0),
            "pis_peak":      stats.get("pis_peak", 0),
            "top_profile":   stats.get("top_profile", "Auto"),
            "leaks_found":   stats.get("leaks_found", 0),
        }
        with self._lock:
            self._cache.append(record)
            self._save()
        self._current = None

    def load(self, days=30):
        """Return sessions from last N days (newest first)."""
        cutoff = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        with self._lock:
            return [s for s in reversed(self._cache)
                   if s.get("date", "") >= cutoff]

    def summary(self, days=30):
        """Aggregate stats for last N days."""
        sessions = self.load(days)
        if not sessions:
            return {"total_ram_gb": 0.0, "total_files": 0,
                   "avg_pis": 0, "session_count": 0}
        total_ram_mb = sum(s.get("ram_freed_mb", 0) for s in sessions)
        avg_pis_sum = sum(s.get("pis_avg", 0) for s in sessions
                         if s.get("pis_avg"))
        avg_pis_n = sum(1 for s in sessions if s.get("pis_avg"))
        return {
            "total_ram_gb":  round(total_ram_mb / 1024, 1),
            "total_cycles":  sum(s.get("cycles", 0) for s in sessions),
            "avg_pis":       int(avg_pis_sum / max(1, avg_pis_n)),
            "session_count": len(sessions),
        }

    def export_csv(self, days=90):
        """Generate CSV string for export."""
        sessions = self.load(days)
        csv = "Date,Start,End,Duration(min),Mode,Cycles,RAM Freed(MB),Avg PIS,Top Profile\n"
        for s in sessions:
            csv += f"{s.get('date','')},{s.get('start_time','')},"
            csv += f"{s.get('end_time','')},{s.get('duration_min',0)},"
            csv += f"{s.get('mode','')},{s.get('cycles',0)},"
            csv += f"{s.get('ram_freed_mb',0)},{s.get('pis_avg',0)},"
            csv += f"{s.get('top_profile','')}\n"
        return csv


# ============================================================================
# REPORT GENERATOR
# ============================================================================
class ReportGenerator:
    @staticmethod
    def health_report(observer, history, ai_summary):
        snap = observer.last_snap or observer.snapshot()
        health = HealthAnalyzer.analyze(snap, history)
        try:
            procs = observer.get_processes(force=True)
            top_cpu = sorted(procs, key=lambda x: x.get("cpu_percent", 0), reverse=True)[:8]
            top_ram = sorted(procs, key=lambda x: x.get("memory_percent", 0), reverse=True)[:8]
        except Exception: top_cpu = top_ram = []
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>OMEGA X — Health Report</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
     background:#FFF;color:#1A1A1A;padding:40px 20px;line-height:1.6}}
.container{{max-width:960px;margin:0 auto}}
.header{{border-bottom:2px solid #0066FF;padding-bottom:20px;margin-bottom:32px}}
h1{{font-size:32px;color:#0066FF}}
.subtitle{{color:#6B7280;margin-top:6px;font-size:14px}}
.score-card{{background:#FFF;border:1px solid #E5E7EB;border-radius:12px;
            padding:32px;margin-bottom:24px;text-align:center}}
.score-num{{font-size:72px;font-weight:700;color:#0066FF;line-height:1}}
.score-label{{font-size:18px;color:#4B5563;margin-top:8px}}
.status-badge{{display:inline-block;padding:6px 16px;border-radius:20px;
              background:#E6F0FF;color:#0066FF;font-weight:600;margin-top:12px}}
.metrics-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px}}
.metric-card{{background:#F8F9FA;border:1px solid #E5E7EB;border-radius:8px;padding:16px}}
.metric-label{{font-size:11px;color:#9CA3AF;text-transform:uppercase}}
.metric-value{{font-size:24px;font-weight:700;color:#1A1A1A;margin-top:4px}}
.metric-bar{{height:4px;background:#E5E7EB;border-radius:2px;margin-top:10px;overflow:hidden}}
.metric-fill{{height:100%;background:#0066FF}}
.section{{background:#FFF;border:1px solid #E5E7EB;border-radius:12px;padding:24px;margin-bottom:20px}}
.section h2{{font-size:18px;font-weight:600;margin-bottom:16px}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th{{text-align:left;padding:10px;color:#6B7280;font-weight:600;border-bottom:1px solid #E5E7EB;
   font-size:11px;text-transform:uppercase}}
td{{padding:10px;border-bottom:1px solid #F0F1F3}}
.issue{{padding:12px;border-radius:6px;margin-bottom:8px;background:#F0F7FF;
       border-left:3px solid #0066FF}}
.issue.critical{{background:#FFF5F5;border-left-color:#DC2626}}
.issue.warning{{background:#FFFBEB;border-left-color:#F59E0B}}
ul{{list-style:none}}
ul li{{padding:10px 0 10px 28px;border-bottom:1px solid #F0F1F3;position:relative}}
ul li:before{{content:"→";position:absolute;left:8px;color:#0066FF;font-weight:bold}}
footer{{text-align:center;margin-top:40px;color:#9CA3AF;font-size:12px}}
</style></head><body><div class="container">
<div class="header"><h1>OMEGA X — Health Report</h1>
<p class="subtitle">{ts} · Windows {WIN_MAJOR}.{WIN_MINOR} (Build {WIN_BUILD})</p></div>
<div class="score-card"><div class="score-num">{health['overall_score']}</div>
<div class="score-label">Overall / 100</div>
<div class="status-badge">{health['status']}</div></div>
<div class="metrics-grid">
<div class="metric-card"><div class="metric-label">CPU</div>
<div class="metric-value">{health['cpu_score']}</div>
<div class="metric-bar"><div class="metric-fill" style="width:{health['cpu_score']}%"></div></div></div>
<div class="metric-card"><div class="metric-label">RAM</div>
<div class="metric-value">{health['ram_score']}</div>
<div class="metric-bar"><div class="metric-fill" style="width:{health['ram_score']}%"></div></div></div>
<div class="metric-card"><div class="metric-label">Disk</div>
<div class="metric-value">{health['disk_score']}</div>
<div class="metric-bar"><div class="metric-fill" style="width:{health['disk_score']}%"></div></div></div>
<div class="metric-card"><div class="metric-label">Uptime</div>
<div class="metric-value">{health['uptime_score']}</div>
<div class="metric-bar"><div class="metric-fill" style="width:{health['uptime_score']}%"></div></div></div>
</div>
<div class="section"><h2>Snapshot</h2><table>
<tr><td><strong>CPU avg</strong></td><td>{health['cpu_avg']:.1f}%</td></tr>
<tr><td><strong>RAM avg</strong></td><td>{health['ram_avg']:.1f}%</td></tr>
<tr><td><strong>Disk used</strong></td><td>{health['disk_pct']:.0f}% ({snap.get('disk_free_gb',0):.1f} GB free)</td></tr>
<tr><td><strong>Uptime</strong></td><td>{health['uptime_hours']:.1f} h</td></tr>
<tr><td><strong>Cores</strong></td><td>{snap.get('logical_cores',0)} logical</td></tr>
<tr><td><strong>Threads running</strong></td><td>{snap.get('threads_running',0)}</td></tr>
</table></div>"""

        if health['issues']:
            html += '<div class="section"><h2>Issues</h2>'
            for sev, msg in health['issues']:
                html += f'<div class="issue {sev}">{msg}</div>'
            html += '</div>'

        if health['recommendations']:
            html += '<div class="section"><h2>Recommendations</h2><ul>'
            for r in health['recommendations']: html += f'<li>{r}</li>'
            html += '</ul></div>'

        html += '<div class="section"><h2>Top by CPU</h2><table>'
        html += '<tr><th>Process</th><th>CPU</th><th>RAM</th><th>Threads</th></tr>'
        for p in top_cpu:
            html += f"""<tr><td><strong>{p.get('name','?')}</strong></td>
<td>{p.get('cpu_percent',0):.1f}%</td><td>{p.get('memory_percent',0):.1f}%</td>
<td>{p.get('num_threads','-')}</td></tr>"""
        html += '</table></div>'

        html += '<div class="section"><h2>Top by RAM</h2><table>'
        html += '<tr><th>Process</th><th>RAM</th><th>CPU</th></tr>'
        for p in top_ram:
            html += f"""<tr><td><strong>{p.get('name','?')}</strong></td>
<td>{p.get('memory_percent',0):.1f}%</td><td>{p.get('cpu_percent',0):.1f}%</td></tr>"""
        html += '</table></div>'

        if ai_summary and ai_summary.get('cycles', 0) > 0:
            html += f'<div class="section"><h2>AI Session</h2>'
            html += f'<p style="color:#4B5563;margin-bottom:12px">'
            html += f'Cycles: {ai_summary["cycles"]} · Anomalies: {ai_summary["anomalies"]}</p>'
            html += '<table><tr><th>State</th><th>Time</th></tr>'
            for st, pct in sorted(ai_summary.get('distribution', {}).items(),
                                  key=lambda x: -x[1]):
                html += f'<tr><td><strong>{st}</strong></td><td>{pct}%</td></tr>'
            html += '</table></div>'

        html += f'<footer>OMEGA X v{APP_VERSION}</footer></div></body></html>'
        return html

    @staticmethod
    def perf_csv(history):
        csv = "Time,CPU%,RAM%,LPI\n"
        for h in history:
            csv += f"{h['time']},{h['cpu']},{h['ram']},{h['score']}\n"
        return csv

    @staticmethod
    def startup_report(apps):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>OMEGA X — Startup Apps</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
     background:#FFF;color:#1A1A1A;padding:40px 20px}}
.container{{max-width:960px;margin:0 auto}}
h1{{color:#0066FF;border-bottom:2px solid #0066FF;padding-bottom:12px;margin-bottom:24px}}
table{{width:100%;border-collapse:collapse}}
th{{text-align:left;padding:12px;background:#F8F9FA;color:#6B7280;border-bottom:2px solid #E5E7EB}}
td{{padding:12px;border-bottom:1px solid #F0F1F3}}
.badge{{padding:3px 8px;border-radius:4px;font-size:11px;font-weight:600}}
.safe{{background:#E6F0FF;color:#0066FF}}
.danger{{background:#FEF2F2;color:#991B1B}}
</style></head><body><div class="container">
<h1>Startup Apps</h1>
<p style="color:#6B7280;margin-bottom:24px">{ts} · {len(apps)} apps</p>
<table><tr><th>Name</th><th>Scope</th><th>Status</th><th>Path</th></tr>"""
        for a in apps:
            badge = '<span class="badge safe">Safe</span>' if a['safe_to_disable'] \
                   else '<span class="badge danger">Keep</span>'
            cmd_short = a['cmd'][:80] + ('...' if len(a['cmd']) > 80 else '')
            html += f"""<tr><td><strong>{a['name']}</strong></td><td>{a['scope']}</td>
<td>{badge}</td><td style="font-family:monospace;font-size:11px;color:#6B7280">{cmd_short}</td></tr>"""
        html += "</table></div></body></html>"
        return html


# ============================================================================
# GUI — Lazy-loaded sidebar layout (Microsoft PC Manager style)
# ============================================================================
class OmegaGUI:
    SIDEBAR_W = 200
    # (section_id, translation_key, icon)
    SECTIONS = [
        ("home",     "nav_home",      "🏠"),
        ("ai_core",  "nav_ai_core",   "⚡"),
        ("storage",  "nav_storage",   "💾"),
        ("apps",     "nav_apps",      "📦"),
        ("health",   "nav_health",    "🩺"),
        ("reports",  "nav_reports",   "📊"),
        ("settings", "nav_settings",  "⚙"),
    ]

    def __init__(self, root, perf, observer, ai, policy, guard, executor,
                 optimizer, core_mode,
                 game_detect=None, scheduler=None, battery_saver=None,
                 leak_detector=None, session_history=None):
        self.root = root
        self.perf = perf
        self.observer = observer
        self.ai = ai; self.policy = policy
        self.guard = guard; self.executor = executor
        self.optimizer = optimizer
        self.core_mode = core_mode
        # Smart automation managers
        self.game_detect = game_detect
        self.scheduler = scheduler
        self.battery_saver = battery_saver
        # Phase 2-3: leak detector + session history
        self.leak_detector = leak_detector
        self.session_history = session_history
        # 온도 자동 완화(설정에서 켬). main() 이 생성 직후 주입한다.
        self.governor = None
        # Performance tracking for session-end save
        self._last_pis_peak = 0
        self._last_top_profile = "Auto"

        self.active_section = None
        self.dynamic = {}        # widget references
        self._sections_built = set()  # lazy-build cache
        self._refresh_timer_id = None
        self._toast_widget = None
        # ── ★GUI 최적화 상태★ ───────────────────────────────────
        # 백그라운드 스레드 → 메인 스레드 UI 전달용 큐.
        # Tk 는 스레드 안전하지 않다. 기존 코드는 워커 스레드에서
        # root.after() 를 직접 불러 간헐적 멈춤/크래시 위험이 있었다.
        # deque 의 append/popleft 는 GIL 하에서 원자적이므로 안전하다.
        self._ui_queue = deque(maxlen=300)
        self._ui_pump_id = None
        # 백그라운드 샘플러가 채우고, Tk 스레드는 읽기만 하는 값들.
        # (dict 의 단일 키 읽기/쓰기는 GIL 하에서 원자적이라 락이 필요 없다)
        self._ui_data = {}
        self._ui_frame_ms = 0.0
        self._ui_frame_ms_max = 0.0
        # 섹션 위젯 캐시(LRU 3) — 탭 전환마다 수백 개 위젯을
        # destroy/재생성하던 비용 제거
        self._section_frames = {}
        self._section_dyn = {}
        self._section_lru = []
        # 프로세스 목록 행 풀 (30행 재사용)
        self._proc_row_pool = []
        # 진행 로그 행 풀 (8행 재사용)
        self._prog_row_pool = []
        self._prog_lines = deque(maxlen=8)
        self._toast_after_id = None
        self._win_visible = True

        self.root.title(f"{APP_NAME} v{APP_VERSION}")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 700)
        # ★위젯 색은 생성 시점에 굳는다★ — 스켈레톤을 만들기 전에
        # 저장된 테마를 팔레트에 반영해야 한다.
        self.theme = SETTINGS.get("theme", "light")
        apply_theme(self.theme)
        apply_window_icon(self.root)
        # 프로세스 표 상태(검색어 / 정렬 열 / 내림차순)
        self._proc_query = ""
        self._proc_sort = "cpu"
        self._proc_desc = True
        self._proc_hdr = {}

        # Listen for language changes to rebuild UI
        I18N.on_change(self._on_lang_change)

        # Setup keyboard shortcuts
        self._setup_shortcuts()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

        self._build_skeleton()
        self._show_section("home")
        # Defer auto-loop start AND first refresh until UI is fully on screen.
        # Was 800ms — extended to 2000ms so the first paint completes before
        # any background work fires.
        self.root.after(2000, self._start_background)

        # Auto-update check (2 seconds after startup)
        self._update_dialog_open = False
        if UPDATE_ENABLED:
            self.root.after(2500, self._show_post_update_toast)
            self.root.after(3000, self._check_update_background)

    def _show_post_update_toast(self):
        if not UPDATE_ENABLED:
            return
        result = UpdateChecker.check_startup_update_message()
        if result == "success":
            # 방금 업데이트가 성공했다 -> 이번 실행에서는 백그라운드
            # 업데이트 재확인을 건너뛴다. 혹시 버전 비교가 꼬여 있어도
            # 설치 직후 또 업데이트 창이 뜨는 무한 반복을 막는 안전장치.
            self._just_updated = True
            self._toast(t("update_success_toast"))
        elif result == "failed":
            self._toast(t("update_failed") + " " + t("update_log_hint"))

    def _check_update_background(self):
        thread = threading.Thread(target=self._update_check_thread, daemon=True)
        thread.start()

    def _update_check_thread(self):
        if getattr(self, "_just_updated", False):
            UpdateChecker._log(
                "방금 업데이트 성공 -> 이번 실행의 백그라운드 체크 생략")
            return
        UpdateChecker._log(
            f"백그라운드 업데이트 체크 시작 (APP_VERSION={APP_VERSION}, "
            f"UPDATE_ENABLED={UPDATE_ENABLED})"
        )
        try:
            has_update, latest = UpdateChecker.has_update()
            if has_update and latest:
                if self._is_reboot_pending_for(latest):
                    UpdateChecker._log(
                        "재부팅 대기 상태 -> 자동 업데이트 재시도 생략, 재부팅 안내")
                    self.root.after(0, lambda: self._toast(t("update_reboot_pending")))
                    return
                self.root.after(0, lambda l=latest: self._show_update_dialog(l))
            else:
                UpdateChecker._log("백그라운드 체크 완료 - 업데이트 없음 또는 확인 실패")
        except Exception as e:
            UpdateChecker._log(f"백그라운드 체크 예외: {e}")
            self.root.after(0, lambda: self._toast(t("update_check_failed")))

    def _is_reboot_pending_for(self, latest):
        """직전에 이 버전으로 업데이트했는데 EXE 가 안 바뀐(재부팅 대기) 상태인지.
        맞으면 재부팅 전까지 자동 재설치를 막아 무한 반복을 끊는다.
        현재 버전이 이미 목표(또는 그 이상)면 표식을 지우고 정상 진행한다."""
        try:
            pend = UpdateChecker._get_reboot_pending()
            if not pend:
                return False
            tgt = str((latest or {}).get("version", "")).strip()
            npend = UpdateChecker._normalize_version(pend)
            ncur = UpdateChecker._normalize_version(str(APP_VERSION).strip())
            # 이미 적용됨(재부팅 후 등) -> 표식 해제하고 정상 진행.
            if UpdateChecker._version_key(ncur) >= UpdateChecker._version_key(npend):
                UpdateChecker._clear_reboot_pending()
                return False
            # 같은 목표 버전을 또 시도하려는 상황이면 막는다.
            return bool(tgt) and UpdateChecker._normalize_version(tgt) == npend
        except Exception:
            return False

    def _manual_check_update(self):
        if not UPDATE_ENABLED:
            self._toast(t("update_check_failed"))
            return
        self._toast(t("update_checking"))
        threading.Thread(target=self._manual_update_check_thread, daemon=True).start()

    def _manual_update_check_thread(self):
        try:
            has_update, latest = UpdateChecker.has_update()
            if has_update and latest:
                if self._is_reboot_pending_for(latest):
                    self.root.after(0, lambda: self._toast(t("update_reboot_pending")))
                    return
                self.root.after(0, lambda l=latest: self._show_update_dialog(l))
            else:
                self.root.after(0, lambda: self._toast(t("update_none")))
        except Exception as e:
            print(f"[Update] 수동 확인 실패: {e}")
            self.root.after(0, lambda: self._toast(t("update_check_failed")))

    def _close_update_dialog(self, dialog):
        self._update_dialog_open = False
        try:
            dialog.grab_release()
        except Exception as _dx:
            DIAG.q("OmegaGUI._close_update_dialog#0", _dx)
        try:
            dialog.destroy()
        except Exception as _dx:
            DIAG.q("OmegaGUI._close_update_dialog#1", _dx)

    def _show_update_dialog(self, latest):
        if getattr(self, "_update_dialog_open", False):
            return
        # root 유효성 확인
        try:
            if not self.root or not self.root.winfo_exists():
                return
        except Exception:
            return
        # _default_root 재확인 (이중 CTk 방어)
        try:
            import tkinter as _tk
            if _tk._default_root is None:
                _tk._default_root = self.root
        except Exception as _dx:
            DIAG.q("OmegaGUI._show_update_dialog#0", _dx)
        self._update_dialog_open = True
        try:
            dialog = ctk.CTkToplevel(self.root)
            dialog.title(t("update_title"))
            dialog.geometry("500x500")
            dialog.resizable(False, False)
            dialog.transient(self.root)
            dialog.grab_set()
            dialog.protocol("WM_DELETE_WINDOW", lambda: self._close_update_dialog(dialog))

            dialog.update_idletasks()
            x = (dialog.winfo_screenwidth() // 2) - 250
            y = (dialog.winfo_screenheight() // 2) - 250
            dialog.geometry(f"500x500+{x}+{y}")

            btn_frame = ctk.CTkFrame(dialog, fg_color="transparent", height=60)
            btn_frame.pack(side="bottom", fill="x", pady=15, padx=20)
            btn_frame.pack_propagate(False)

            status_lbl = ctk.CTkLabel(
                dialog, text="", font=("", 12), text_color=C["text_2"],
                wraplength=440, justify="center")
            status_lbl.pack(side="bottom", fill="x", padx=20, pady=(0, 8))

            progress = ctk.CTkProgressBar(dialog, width=420, height=14)
            progress.pack(side="bottom", padx=20, pady=(0, 8))
            progress.set(0)

            progress_lbl = ctk.CTkLabel(
                dialog, text="", font=("", 11), text_color=C["text_3"])
            progress_lbl.pack(side="bottom", fill="x", padx=20, pady=(0, 4))

            def set_ui_status(msg, color=None, prog=None, prog_text=""):
                status_lbl.configure(text=msg, text_color=color or C["text_2"])
                progress_lbl.configure(text=prog_text)
                if prog is not None:
                    progress.set(max(0.0, min(1.0, prog)))

            def on_fail():
                set_ui_status(
                    t("update_failed") + "\n" + t("update_log_hint"),
                    C["danger_text"], 0, "")
                btn_update.configure(state="normal", text=t("update_retry"))
                btn_later.configure(state="normal")

            def on_restart():
                set_ui_status(t("update_restarting"), C["blue"], 1.0, "")
                btn_update.configure(state="disabled")
                dialog.update()
                time.sleep(2.0)
                self._close_update_dialog(dialog)
                try:
                    self.root.withdraw()
                except Exception as _dx:
                    DIAG.q("OmegaGUI.on_restart#0", _dx)
                try:
                    self.root.quit()
                    self.root.destroy()
                except Exception as _dx:
                    DIAG.q("OmegaGUI.on_restart#1", _dx)
                os._exit(0)

            def progress_cb(done, total):
                pct = (done / total) if total else 0
                pt = int(pct * 100)
                self.root.after(
                    0,
                    lambda p=pct, n=pt: set_ui_status(
                        t("update_downloading"), C["text_2"], p * 0.85,
                        f"{t('update_downloading')} {n}%"),
                )

            def do_update():
                btn_update.configure(state="disabled", text=t("update_downloading"))
                btn_later.configure(state="disabled")
                set_ui_status(t("update_downloading"), C["text_2"], 0.05, "")

                def worker():
                    new_path = UpdateChecker.download_update(
                        latest["url"],
                        filename=latest.get("filename"),
                        progress_cb=progress_cb,
                        expected_digest=latest.get("digest"),
                    )
                    if not new_path:
                        self.root.after(0, on_fail)
                        return
                    self.root.after(
                        0,
                        lambda: set_ui_status(
                            t("update_applying"), C["text_2"], 0.9, ""),
                    )
                    ok = UpdateChecker.apply_downloaded_update(
                        new_path,
                        target_version=latest.get("version"),
                        expected_digest=latest.get("digest"),
                    )
                    if ok:
                        self.root.after(0, on_restart)
                    else:
                        self.root.after(0, on_fail)

                threading.Thread(target=worker, daemon=True).start()

            btn_update = ctk.CTkButton(
                btn_frame, text=t("update_now"), command=do_update,
                fg_color=C["btn_primary"], hover_color=C["btn_primary_h"],
                width=180, height=42, font=("", 14, "bold"),
            )
            btn_update.pack(side="left", expand=True, padx=5)

            btn_later = ctk.CTkButton(
                btn_frame, text=t("update_later"),
                command=lambda: self._close_update_dialog(dialog),
                fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                text_color=C["text"], width=120, height=42, font=("", 13),
            )
            btn_later.pack(side="left", expand=True, padx=5)

            content_frame = ctk.CTkFrame(dialog, fg_color="transparent")
            content_frame.pack(side="top", fill="both", expand=True, padx=20, pady=(20, 0))

            ctk.CTkLabel(
                content_frame, text=t("update_new_version"),
                font=("", 18, "bold"), text_color=C["text"],
            ).pack(pady=(0, 10))

            current_v = str(APP_VERSION).lstrip("vV")
            latest_v = str(latest.get("version", "?")).lstrip("vV")
            ctk.CTkLabel(
                content_frame,
                text=t("update_version_line").format(current=current_v, latest=latest_v),
                font=("", 13), text_color=C["text_2"],
            ).pack(pady=(0, 8))

            if latest.get("is_setup"):
                ctk.CTkLabel(
                    content_frame, text=t("update_setup_hint"),
                    font=("", 11), text_color=C["warn_text"], wraplength=440,
                ).pack(pady=(0, 10))

            ctk.CTkLabel(
                content_frame, text=t("update_notes_label"),
                font=("", 11, "bold"), text_color=C["text"], anchor="w",
            ).pack(fill="x", pady=(0, 5))

            notes_text = ctk.CTkTextbox(
                content_frame, height=140, fg_color=C["card"],
                text_color=C["text_2"], wrap="word",
            )
            notes_text.pack(fill="x", pady=(0, 10))
            notes_content = (latest.get("notes") or "").strip() or t("update_notes_empty")
            notes_text.insert("0.0", notes_content[:800])
            notes_text.configure(state="disabled")

        except Exception as e:
            self._update_dialog_open = False
            print(f"[Update] 다이얼로그 표시 실패: {e}")
    

    def _invalidate_section_cache(self):
        """★신규★ 캐시된 섹션 프레임을 전부 파기한다.

        _show_section 은 만들어둔 프레임을 destroy 하지 않고 pack_forget 으로
        숨겼다가 다시 pack 한다(LRU 3개). 성능에는 좋지만, 언어를 바꿨을 때
        '다시 그린다'는 요청이 캐시 적중으로 흡수돼 옛 언어 화면이 그대로
        다시 붙는다. 언어 전환 시에는 캐시를 통째로 버려야 한다.
        """
        for sid, f in list(getattr(self, "_section_frames", {}).items()):
            if self._widget_alive(f):
                try: f.destroy()
                except Exception as _dx: DIAG.q("OmegaGUI._invalidate_section_cache#0", _dx)
        self._section_frames = {}
        self._section_dyn = {}
        self._section_lru = []
        self._sections_built = set()
        # 섹션에 속한 위젯 참조도 함께 버린다(파기된 위젯을 가리키고 있다).
        for k in list(self.dynamic.keys()):
            if k not in self._PERSISTENT_DYN_KEYS:
                self.dynamic.pop(k, None)

    def _on_lang_change(self):
        """Rebuild entire UI when language changes."""
        # Clear diff cache so all widgets re-render with new language
        if hasattr(self, "_lv"): self._lv = {}
        # ★수정(언어가 안 바뀌던 직접 원인)★
        # 아래 _show_section 호출이 '강제 재렌더'를 의도했지만, 섹션 캐시가
        # 적중해서 옛 언어로 만들어둔 프레임을 그대로 다시 pack 했다.
        # 캐시에 없던(=LRU 3개에서 밀려난) 섹션만 새 언어로 다시 만들어져서
        # '일부만 바뀐다'는 증상이 나왔다.
        self._invalidate_section_cache()
        # ★수정★ 아래 캐시들은 '번역이 끝난 문자열'을 담고 있다. 안 비우면
        # 진행 로그 라벨과 합계 표시가 세션 내내 옛 언어로 남는다.
        self._friendly_label_cache = {}
        self._running_totals_cache = {}
        self._last_profile_seen = None
        # ★추가★ 진행 로그는 이제 원본 라벨만 들고 있다. 다시 그리라고
        #   표시해야 새 언어로 렌더된다(표시 안 하면 펌프가 건너뛴다).
        self._prog_dirty = True
        # 행 풀의 텍스트 비교 캐시도 비운다 — 안 비우면 "값이 같다"고 보고
        #   configure 를 생략해 옛 언어가 그대로 남는다.
        for r in getattr(self, "_prog_row_pool", []) or []:
            try: r["cache"] = {}
            except Exception as _dx: DIAG.q("OmegaGUI._on_lang_change#0", _dx)
        # Update window title (no change but harmless)
        self.root.title(f"{APP_NAME} v{APP_VERSION}")
        # Update nav button labels
        for sid, btn in self.nav_buttons.items():
            label_key = next(K for SID, K, _ in self.SECTIONS if SID == sid)
            icon = next(I for SID, _, I in self.SECTIONS if SID == sid)
            is_active = (sid == self.active_section)
            btn.configure(
                text=f"  {icon}   {t(label_key)}",
                font=("Segoe UI", 12, "bold" if is_active else "normal"),
            )
        # Update header title
        if self.active_section:
            cur_key = next(K for SID, K, _ in self.SECTIONS
                          if SID == self.active_section)
            self.header_title.configure(text=t(cur_key))
        # Force re-render of current section
        cur = self.active_section
        self.active_section = None
        self._show_section(cur or "home")

    def _setup_shortcuts(self):
        """Setup keyboard shortcuts for common actions."""
        # Ctrl+Home → Home
        self.root.bind("<Control-Home>", lambda e: self._show_section("home"))
        # Ctrl+1 → AI Core
        self.root.bind("<Control-1>", lambda e: self._show_section("ai_core"))
        # Ctrl+2 → Storage
        self.root.bind("<Control-2>", lambda e: self._show_section("storage"))
        # Ctrl+3 → Apps
        self.root.bind("<Control-3>", lambda e: self._show_section("apps"))
        # Ctrl+4 → Health
        self.root.bind("<Control-4>", lambda e: self._show_section("health"))
        # Ctrl+5 → Reports
        self.root.bind("<Control-5>", lambda e: self._show_section("reports"))
        # Ctrl+, → Settings
        self.root.bind("<Control-comma>", lambda e: self._show_section("settings"))
        # F1 → Help
        self.root.bind("<F1>", lambda e: self._toast(f"{APP_NAME} v{APP_VERSION}"))

    def _on_closing(self):
        """Handle window close — force quit immediately, no confirmation."""
        # 0) 온도 관련 정리 — ★CPU 속도 제한을 반드시 먼저 되돌린다★
        #    (여기서 안 풀면 앱을 꺼도 PC 가 70% 로 묶인 채 남는다)
        try:
            gov = getattr(self, "governor", None)
            if gov is not None: gov.stop(restore=True)
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#0", _dx)
        try:
            th = getattr(self.observer, "thermal", None)
            if th is not None: th.stop()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#1", _dx)
        # 0-b) EcoQoS 전량 해제 — 장부가 하나로 합쳐졌으므로 이 한 줄이
        #      Auto 루프와 코어 모드가 건 것을 모두 덮는다.
        try:
            ECO.release_all()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#2", _dx)
        # 1) 백그라운드 스레드 정리 시도 (실패해도 무시)
        try:
            if self.core_mode and self.core_mode.is_running():
                self.core_mode.stop_continuous()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#3", _dx)
        # 1-b) 전원 계획을 원래대로 — stop_continuous 가 안 탔을 경우(원샷
        #      Hard 실행 등)에도 반드시 원복되도록 명시적으로 한 번 더 호출.
        try:
            if self.core_mode:
                self.core_mode._restore_power_scheme()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#4", _dx)
        # 1-c) ★추가★ 신형 최적화(CPU Sets·메모리 우선순위·타이머 차단·
        #      GPU 우선순위)와 EcoQoS 원복. os._exit 로 끝나므로 main 의
        #      finally 정리가 실행되지 않는다 — 여기서 직접 해야 한다.
        try:
            if self.core_mode: self.core_mode.modern.revert_all()
        except Exception as _dx: DIAG.q("OmegaGUI._on_closing#5", _dx)
        try:
            if self.executor: self.executor.revert_ecoqos_all()
        except Exception as _dx: DIAG.q("OmegaGUI._on_closing#6", _dx)
        try:
            if self.guard: self.guard.rollback_all()
        except Exception as _dx: DIAG.q("OmegaGUI._on_closing#7", _dx)
        # 2) 모든 after 큐에 쌓인 콜백이 죽은 위젯 만지지 않게 게이트
        self._shutting_down = True
        # 2-b) 주기 타이머 정지 (죽은 위젯 접근 방지)
        for attr in ("_ui_pump_id", "_refresh_timer_id", "_toast_after_id"):
            job = getattr(self, attr, None)
            if job:
                try: self.root.after_cancel(job)
                except Exception as _dx: DIAG.q("OmegaGUI._on_closing#8", _dx)
                setattr(self, attr, None)
        # 3) 토스트 같은 자투리 위젯 정리
        try:
            if getattr(self, "_toast_widget", None):
                self._toast_widget.destroy()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#9", _dx)
        # 4) 메인 윈도우 파괴
        try:
            self.root.destroy()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_closing#10", _dx)
        # 5) 남은 데몬 스레드까지 확실히 종료 — os._exit 사용 (atexit 건너뜀)
        try:
            os._exit(0)
        except Exception:
            sys.exit(0)

    # ────────────────────────────────────────────────────────────
    #  SKELETON
    # ────────────────────────────────────────────────────────────
    def _build_skeleton(self):
        self.root.configure(fg_color=C["bg"])

        # Sidebar
        self.sidebar = ctk.CTkFrame(self.root, width=self.SIDEBAR_W,
                                    fg_color=C["sidebar"], corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        logo = ctk.CTkFrame(self.sidebar, fg_color="transparent", height=72)
        logo.pack(fill="x", padx=20, pady=(20, 8))
        logo.pack_propagate(False)
        ctk.CTkLabel(logo, text="◆ OMEGA X",
                     font=("Segoe UI", 18, "bold"),
                     text_color=C["blue"], anchor="w").pack(side="left", fill="y")

        ctk.CTkFrame(self.sidebar, height=1, fg_color=C["border"]).pack(
            fill="x", padx=12, pady=(8, 12))

        self.nav_buttons = {}
        for sid, label_key, icon in self.SECTIONS:
            btn = ctk.CTkButton(
                self.sidebar, text=f"  {icon}   {t(label_key)}",
                anchor="w", font=("Segoe UI", 12),
                fg_color="transparent", text_color=C["text_2"],
                hover_color=C["sidebar_hov"],
                corner_radius=8, height=40,
                command=lambda s=sid: self._show_section(s),
            )
            btn.pack(fill="x", padx=8, pady=2)
            self.nav_buttons[sid] = btn

        # Bottom info
        bottom = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        bottom.pack(side="bottom", fill="x", padx=12, pady=12)
        ctk.CTkFrame(bottom, height=1, fg_color=C["border"]).pack(
            fill="x", pady=(0, 8))
        self.dynamic["sidebar_status"] = ctk.CTkLabel(
            bottom, text=t("sidebar_active"), font=("Segoe UI", 10),
            text_color=C["blue"], anchor="w")
        self.dynamic["sidebar_status"].pack(fill="x", padx=4, pady=(0, 2))
        os_label = "Win11" if IS_WIN11 else "Win10"
        ctk.CTkLabel(bottom, text=f"{os_label} · {WIN_BUILD}",
                    font=("Segoe UI", 9), text_color=C["text_3"],
                    anchor="w").pack(fill="x", padx=4)

        # Main
        self.main = ctk.CTkFrame(self.root, fg_color=C["bg"], corner_radius=0)
        self.main.pack(side="left", fill="both", expand=True)

        self.header = ctk.CTkFrame(self.main, fg_color=C["bg"], height=60)
        self.header.pack(fill="x", padx=24, pady=(20, 0))
        self.header.pack_propagate(False)

        self.header_title = ctk.CTkLabel(
            self.header, text=t("nav_home"), font=("Segoe UI", 26, "bold"),
            text_color=C["text"], anchor="w")
        self.header_title.pack(side="left", fill="y")

        self.dynamic["header_status"] = ctk.CTkLabel(
            self.header, text=t("sidebar_loading"), font=("Segoe UI", 12),
            text_color=C["blue"], anchor="e")
        self.dynamic["header_status"].pack(side="right", fill="y", padx=8)

        # One scrollable container for all sections
        self.content = ctk.CTkScrollableFrame(
            self.main, fg_color=C["bg"], corner_radius=0)
        self.content.pack(fill="both", expand=True, padx=24, pady=(8, 16))

    # 섹션 전환 시에도 보존해야 하는 영구 위젯 키 (스켈레톤 위젯)
    _PERSISTENT_DYN_KEYS = frozenset({"header_status"})

    def _show_section(self, sid):
        if sid == self.active_section: return

        # 섹션 전환 중에는 백그라운드 콜백이 죽은 위젯에 접근하지 못하게 게이트
        self._switching = True

        for s, btn in self.nav_buttons.items():
            is_active = (s == sid)
            label_key = next(K for SID, K, _ in self.SECTIONS if SID == s)
            icon = next(I for SID, _, I in self.SECTIONS if SID == s)
            btn.configure(
                text=f"  {icon}   {t(label_key)}",
                fg_color=C["sidebar_act"] if is_active else "transparent",
                text_color=C["blue"] if is_active else C["text_2"],
                font=("Segoe UI", 12, "bold" if is_active else "normal"),
            )
        cur_key = next(K for SID, K, _ in self.SECTIONS if SID == sid)
        self.header_title.configure(text=t(cur_key))

        # ── ★GUI 최적화★ 섹션 캐시 ─────────────────────────────
        # 기존: 탭을 누를 때마다 content 의 자식 위젯을 전부 destroy 하고
        # 빌더를 다시 돌렸다. 홈/설정 같은 화면은 위젯이 200~400개라
        # 전환마다 눈에 띄는 멈칫이 생긴다. 이제 만들어둔 프레임을
        # pack_forget 으로 숨겼다가 다시 pack 한다(최근 3개 유지).
        prev_sid = self.active_section
        if prev_sid:
            prev_frame = self._section_frames.get(prev_sid)
            if self._widget_alive(prev_frame):
                try: prev_frame.pack_forget()
                except Exception as _dx: DIAG.q("OmegaGUI._show_section#0", _dx)
            # 이전 섹션의 위젯 참조를 따로 보관
            self._section_dyn[prev_sid] = {
                k: v for k, v in self.dynamic.items()
                if k not in self._PERSISTENT_DYN_KEYS}

        for k in list(self.dynamic.keys()):
            if k not in self._PERSISTENT_DYN_KEYS:
                self.dynamic.pop(k, None)

        self.active_section = sid

        frame = self._section_frames.get(sid)
        if self._widget_alive(frame):
            # 캐시 적중 — 위젯 참조 복원 후 다시 표시
            self.dynamic.update(self._section_dyn.get(sid, {}))
            try:
                frame.pack(fill="both", expand=True)
            except Exception:
                frame = None
        else:
            frame = None

        if frame is None:
            builder = {
                "home":      self._build_home,
                "ai_core":   self._build_ai_core,
                "storage":   self._build_storage,
                "apps":      self._build_apps,
                "health":    self._build_health,
                "reports":   self._build_reports,
                "settings":  self._build_settings,
            }.get(sid, self._build_home)
            try:
                frame = ctk.CTkFrame(self.content, fg_color="transparent")
                frame.pack(fill="both", expand=True)
                outer = self.content
                self.content = frame       # 빌더가 frame 을 부모로 쓰게 함
                try:
                    builder()
                finally:
                    self.content = outer
                self._section_frames[sid] = frame
            except Exception as _dx:
                # 빌더 실패해도 게이트는 풀어야 다음 전환이 가능하다
                DIAG.q("OmegaGUI._show_section#1", _dx)

        # LRU 3개만 유지 — 나머지는 파기해 메모리 상한을 둔다
        if sid in self._section_lru:
            self._section_lru.remove(sid)
        self._section_lru.append(sid)
        while len(self._section_lru) > 3:
            drop = self._section_lru.pop(0)
            f = self._section_frames.pop(drop, None)
            self._section_dyn.pop(drop, None)
            self._sections_built.discard(drop)
            if self._widget_alive(f):
                try: f.destroy()
                except Exception as _dx: DIAG.q("OmegaGUI._show_section#2", _dx)

        self._sections_built.add(sid)
        self._switching = False

    # ────────────────────────────────────────────────────────────
    #  HELPERS
    # ────────────────────────────────────────────────────────────
    def _card(self, parent, title=None, padding=20):
        card = ctk.CTkFrame(parent, fg_color=C["card"],
                           border_color=C["border"], border_width=1,
                           corner_radius=12)
        if title:
            ctk.CTkLabel(card, text=title, font=("Segoe UI", 14, "bold"),
                        text_color=C["text"], anchor="w").pack(
                            fill="x", padx=padding, pady=(padding, 8))
        return card

    def _primary_btn(self, parent, text, command, height=44):
        return ctk.CTkButton(parent, text=text, command=command,
                            fg_color=C["btn_primary"],
                            hover_color=C["btn_primary_h"],
                            text_color="#FFFFFF",
                            font=("Segoe UI", 13, "bold"),
                            height=height, corner_radius=8)

    def _secondary_btn(self, parent, text, command, height=36):
        return ctk.CTkButton(parent, text=text, command=command,
                            fg_color=C["btn_sec"],
                            hover_color=C["btn_sec_h"],
                            text_color=C["blue"],
                            font=("Segoe UI", 12),
                            height=height, corner_radius=8,
                            border_width=1, border_color=C["border"])

    def _toast(self, msg, duration=2500):
        # ★수정★ 이전 토스트의 삭제 타이머를 취소하지 않아, 토스트가
        # 연달아 뜨면 앞 타이머가 '새' 토스트를 조기에 지워버렸다.
        if self._toast_after_id is not None:
            try: self.root.after_cancel(self._toast_after_id)
            except Exception as _dx: DIAG.q("OmegaGUI._toast#0", _dx)
            self._toast_after_id = None
        if self._toast_widget:
            try: self._toast_widget.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI._toast#1", _dx)
        self._toast_widget = ctk.CTkFrame(self.root, fg_color=C["blue"],
                                         corner_radius=8)
        self._toast_widget.place(relx=0.5, rely=0.93, anchor="s")
        ctk.CTkLabel(self._toast_widget, text=msg,
                    font=("Segoe UI", 12, "bold"),
                    text_color="#FFFFFF").pack(padx=24, pady=10)
        def kill():
            self._toast_after_id = None
            if self._toast_widget:
                try: self._toast_widget.destroy()
                except Exception as _dx: DIAG.q("OmegaGUI.kill#0", _dx)
                self._toast_widget = None
        self._toast_after_id = self.root.after(duration, kill)

    # ────────────────────────────────────────────────────────────
    #  HOME
    # ────────────────────────────────────────────────────────────
    def _build_home(self):
        # Hero AI Core CTA
        hero = ctk.CTkFrame(self.content, fg_color=C["blue_subtle"],
                           border_color=C["border"], border_width=1,
                           corner_radius=12)
        hero.pack(fill="x", pady=(0, 16))

        hero_inner = ctk.CTkFrame(hero, fg_color="transparent")
        hero_inner.pack(fill="x", padx=24, pady=24)

        ctk.CTkLabel(hero_inner, text=f"⚡  {t('home_hero_title')}",
                    font=("Segoe UI", 18, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")
        ctk.CTkLabel(hero_inner,
                    text=t("home_hero_subtitle"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(2, 16))

        stats_row = ctk.CTkFrame(hero_inner, fg_color="transparent")
        stats_row.pack(fill="x", pady=(0, 16))
        # 온도는 '읽히는 PC 에서만' 한 칸 더 붙인다. 못 읽는 PC 에
        # "알 수 없음" 타일을 세워두지 않는다.
        _stats = [("ram", t("home_ram_label")), ("cpu", t("home_cpu_label"))]
        try:
            _th = getattr(self.observer, "thermal", None)
            if _th is not None and _th.ok:
                _stats.append(("temp", t("thermal_label")))
        except Exception as _dx:
            DIAG.q("OmegaGUI._build_home#0", _dx)
        # 색 상태 캐시는 위젯과 수명을 같이 해야 한다(테마/언어 재빌드 시
        # 위젯이 새로 만들어지므로 여기서 초기화).
        self._temp_band = None
        for i, (key, label) in enumerate(_stats):
            sf = ctk.CTkFrame(stats_row, fg_color="transparent")
            sf.pack(side="left", padx=(0 if i == 0 else 32))
            num_row = ctk.CTkFrame(sf, fg_color="transparent")
            num_row.pack(anchor="w")
            self.dynamic[f"sec_hero_{key}"] = ctk.CTkLabel(
                num_row, text="...", font=("Segoe UI", 22, "bold"),
                text_color=C["blue"], anchor="w")
            self.dynamic[f"sec_hero_{key}"].pack(side="left")
            # Mini progress bar
            bar_bg = ctk.CTkFrame(num_row, fg_color=C["border"],
                                  width=56, height=6, corner_radius=3)
            bar_bg.pack(side="left", padx=(8, 0), pady=(6, 0))
            bar_bg.pack_propagate(False)
            bar_fill = ctk.CTkFrame(bar_bg, fg_color=C["blue"],
                                    width=4, height=6, corner_radius=3)
            bar_fill.place(x=0, y=0, relheight=1)
            self.dynamic[f"sec_hero_{key}_bar"] = bar_fill
            _cap = ctk.CTkLabel(sf, text=label, font=("Segoe UI", 10),
                        text_color=C["text_3"], anchor="w")
            _cap.pack(anchor="w")
            if key == "temp":
                # 온도 캡션은 상태에 따라 문구가 바뀐다(자극적 표현은 쓰지
                # 않는다 — "위험!" 같은 건 가짜 최적화 도구의 수법이다).
                self.dynamic["sec_hero_temp_note"] = _cap

        btn_frame = ctk.CTkFrame(hero_inner, fg_color="transparent")
        btn_frame.pack(fill="x")
        self._primary_btn(btn_frame, t("home_hero_open"),
                         lambda: self._show_section("ai_core"),
                         height=40).pack(fill="x", pady=(0, 0))

        # Quick cards 2x2
        grid = ctk.CTkFrame(self.content, fg_color="transparent")
        grid.pack(fill="x", pady=(0, 16))
        grid.grid_columnconfigure((0, 1), weight=1, uniform="col")

        c1 = self._card(grid)
        c1.grid(row=0, column=0, padx=(0, 8), pady=(0, 8), sticky="nsew")
        self._home_quick(c1, t("home_health_check"), "sec_health_score",
                        t("home_health_desc"),
                        lambda: self._show_section("health"), t("view"))

        c2 = self._card(grid)
        c2.grid(row=0, column=1, padx=(8, 0), pady=(0, 8), sticky="nsew")
        self._home_quick(c2, t("home_active_apps"), "sec_proc_count",
                        t("home_apps_desc"),
                        lambda: self._show_section("apps"), t("open"))

        c3 = self._card(grid)
        c3.grid(row=1, column=0, padx=(0, 8), pady=(8, 0), sticky="nsew")
        self._home_quick(c3, t("home_storage"), "sec_disk_free",
                        t("home_storage_desc"),
                        lambda: self._show_section("storage"), t("manage"))

        c4 = self._card(grid)
        c4.grid(row=1, column=1, padx=(8, 0), pady=(8, 0), sticky="nsew")
        self._home_quick(c4, t("home_ai_core_card"), "sec_ai_state_quick",
                        t("home_ai_core_desc"),
                        lambda: self._show_section("ai_core"), t("open"))

        # AI status
        ai_card = self._card(self.content, t("home_ai_status"))
        ai_card.pack(fill="x", pady=(0, 16))

        ai_inner = ctk.CTkFrame(ai_card, fg_color="transparent")
        ai_inner.pack(fill="x", padx=20, pady=(0, 20))

        m_row = ctk.CTkFrame(ai_inner, fg_color="transparent")
        m_row.pack(fill="x", pady=(0, 12))
        m_row.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="m")

        for i, (k, label) in enumerate([
            ("sec_ai_state", t("home_state")),
            ("sec_ai_lpi", t("home_lpi")),
            ("sec_ai_cycles", t("home_cycles")),
            ("sec_ai_actions", t("home_actions")),
        ]):
            mf = ctk.CTkFrame(m_row, fg_color=C["panel"], corner_radius=8)
            mf.grid(row=0, column=i, padx=2, sticky="ew")
            ctk.CTkLabel(mf, text=label, font=("Segoe UI", 10),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=12, pady=(10, 0))
            v = ctk.CTkLabel(mf, text="--", font=("Segoe UI", 16, "bold"),
                            text_color=C["blue"], anchor="w")
            v.pack(anchor="w", padx=12, pady=(2, 10))
            self.dynamic[k] = v

        self.dynamic["sec_ai_summary"] = ctk.CTkLabel(
            ai_inner, text=t("home_ai_monitoring"), font=("Segoe UI", 11),
            text_color=C["text_2"], anchor="w")
        self.dynamic["sec_ai_summary"].pack(fill="x")

        # Recommendations
        rec_card = self._card(self.content, t("home_recs"))
        rec_card.pack(fill="x", pady=(0, 16))
        self.dynamic["sec_recs"] = ctk.CTkFrame(rec_card, fg_color="transparent")
        self.dynamic["sec_recs"].pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(self.dynamic["sec_recs"], text=t("loading"),
                    font=("Segoe UI", 11), text_color=C["text_3"],
                    anchor="w").pack(fill="x")

    def _home_quick(self, parent, title, key, desc, command, btn_text):
        ctk.CTkLabel(parent, text=title, font=("Segoe UI", 13, "bold"),
                    text_color=C["text"], anchor="w").pack(
                        fill="x", padx=20, pady=(20, 4))
        v = ctk.CTkLabel(parent, text="...", font=("Segoe UI", 20, "bold"),
                        text_color=C["blue"], anchor="w")
        v.pack(fill="x", padx=20)
        self.dynamic[key] = v
        ctk.CTkLabel(parent, text=desc, font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w").pack(
                        fill="x", padx=20, pady=(4, 12))
        self._secondary_btn(parent, btn_text, command).pack(
            fill="x", padx=20, pady=(0, 20))

    # ────────────────────────────────────────────────────────────
    #  AI CORE MODE — the headline feature
    # ────────────────────────────────────────────────────────────
    def _build_ai_core(self):
        ctk.CTkLabel(self.content,
                    text=t("ai_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        # Two big buttons side by side
        btns_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        btns_frame.pack(fill="x", pady=(0, 24))
        btns_frame.grid_columnconfigure((0, 1), weight=1, uniform="b")

        # LITE CORE
        lite_card = ctk.CTkFrame(btns_frame, fg_color=C["card"],
                                border_color=C["border"], border_width=2,
                                corner_radius=16)
        lite_card.grid(row=0, column=0, padx=(0, 8), sticky="nsew", ipady=4)

        lite_inner = ctk.CTkFrame(lite_card, fg_color="transparent")
        lite_inner.pack(fill="both", expand=True, padx=24, pady=24)

        # Title row with FREE badge
        lite_title_row = ctk.CTkFrame(lite_inner, fg_color="transparent")
        lite_title_row.pack(fill="x")
        ctk.CTkLabel(lite_title_row, text=t("ai_lite_title"),
                    font=("Segoe UI", 22, "bold"),
                    text_color=C["text"], anchor="w").pack(side="left", fill="y")
        # FREE badge
        free_badge = ctk.CTkFrame(lite_title_row, fg_color=C["panel"],
                                 corner_radius=6)
        free_badge.pack(side="right", padx=(0, 4))
        ctk.CTkLabel(free_badge, text=t("ai_lite_badge"),
                    font=("Segoe UI", 10, "bold"),
                    text_color=C["text_2"]).pack(padx=10, pady=4)

        ctk.CTkLabel(lite_inner, text=t("ai_lite_desc"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(4, 16))

        for key in ["lite_a1", "lite_a2", "lite_a3", "lite_a4", "lite_a5"]:
            ctk.CTkLabel(lite_inner, text=f"·  {t(key)}",
                        font=("Segoe UI", 11), text_color=C["text_2"],
                        anchor="w").pack(fill="x", pady=2)

        ctk.CTkFrame(lite_inner, height=12, fg_color="transparent").pack()

        self.dynamic["sec_lite_btn"] = self._primary_btn(
            lite_inner,
            t("ai_lite_run_stop") if (self.core_mode.is_running() and
                                      self.core_mode.get_continuous_mode() == "lite")
                                    else t("ai_lite_run_start"),
            self._on_lite_core, height=52)
        self.dynamic["sec_lite_btn"].pack(fill="x")

        # HARD CORE
        hard_card = ctk.CTkFrame(btns_frame, fg_color=C["blue_pale"],
                                border_color=C["blue"], border_width=2,
                                corner_radius=16)
        hard_card.grid(row=0, column=1, padx=(8, 0), sticky="nsew", ipady=4)

        hard_inner = ctk.CTkFrame(hard_card, fg_color="transparent")
        hard_inner.pack(fill="both", expand=True, padx=24, pady=24)

        title_row = ctk.CTkFrame(hard_inner, fg_color="transparent")
        title_row.pack(fill="x")
        ctk.CTkLabel(title_row, text=t("ai_hard_title"),
                    font=("Segoe UI", 22, "bold"),
                    text_color=C["blue"], anchor="w").pack(side="left", fill="y")
        # 모드 배지
        pro_badge = ctk.CTkFrame(title_row, fg_color=C["blue"],
                                corner_radius=6)
        pro_badge.pack(side="right", padx=(0, 4))
        ctk.CTkLabel(pro_badge, text=t("ai_hard_badge"),
                    font=("Segoe UI", 10, "bold"),
                    text_color="#FFFFFF").pack(padx=10, pady=4)

        ctk.CTkLabel(hard_inner, text=t("ai_hard_desc"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(4, 16))

        for key in ["hard_a1", "hard_a2", "hard_a3", "hard_a4", "hard_a5",
                    "hard_a6", "hard_a8", "hard_a9"]:
            ctk.CTkLabel(hard_inner, text=f"·  {t(key)}",
                        font=("Segoe UI", 11), text_color=C["text_2"],
                        anchor="w").pack(fill="x", pady=2)

        ctk.CTkFrame(hard_inner, height=12, fg_color="transparent").pack()

        self.dynamic["sec_hard_btn"] = self._primary_btn(
            hard_inner,
            t("ai_hard_run_stop") if (self.core_mode.is_running() and
                                      self.core_mode.get_continuous_mode() == "hard")
                                    else t("ai_hard_run_start"),
            self._on_hard_core, height=52)
        self.dynamic["sec_hard_btn"].pack(fill="x")

        # ─── LIVE AI SCORE CARD ──────────────────────────────────
        improve_card = ctk.CTkFrame(
            self.content, fg_color=C["blue_subtle"],
            border_color=C["blue"], border_width=2, corner_radius=12)
        improve_card.pack(fill="x", pady=(0, 16))
        self.dynamic["sec_improve_card"] = improve_card

        ic_inner = ctk.CTkFrame(improve_card, fg_color="transparent")
        ic_inner.pack(fill="x", padx=20, pady=20)

        # Title
        ctk.CTkLabel(ic_inner, text=t("ai_improve_title"),
                    font=("Segoe UI", 14, "bold"),
                    text_color=C["blue"], anchor="w").pack(fill="x", pady=(0, 12))

        # ─── BIG AI SCORE (the headline number) ──────────────────
        score_row = ctk.CTkFrame(ic_inner, fg_color="transparent")
        score_row.pack(fill="x", pady=(0, 12))

        # Left: huge score number
        score_left = ctk.CTkFrame(score_row, fg_color=C["card"],
                                 border_color=C["border"], border_width=1,
                                 corner_radius=12)
        score_left.pack(side="left", padx=(0, 8), fill="both", expand=True)
        sl_inner = ctk.CTkFrame(score_left, fg_color="transparent")
        sl_inner.pack(padx=20, pady=16)
        ctk.CTkLabel(sl_inner, text=t("pis_score_label"),
                    font=("Segoe UI", 11), text_color=C["text_3"],
                    anchor="w").pack(anchor="w")
        self.dynamic["sec_pis_score"] = ctk.CTkLabel(
            sl_inner, text="--", font=("Segoe UI", 48, "bold"),
            text_color=C["blue"], anchor="w")
        self.dynamic["sec_pis_score"].pack(anchor="w")
        self.dynamic["sec_pis_tier"] = ctk.CTkLabel(
            sl_inner, text=t("pis_tier_idle"),
            font=("Segoe UI", 11), text_color=C["text_2"],
            anchor="w")
        self.dynamic["sec_pis_tier"].pack(anchor="w", pady=(2, 0))

        # Right: secondary metrics stacked
        score_right = ctk.CTkFrame(score_row, fg_color="transparent")
        score_right.pack(side="left", padx=(8, 0), fill="both", expand=True)

        # Top row (2 metrics): Session Avg, Top Factor
        sr_top = ctk.CTkFrame(score_right, fg_color="transparent")
        sr_top.pack(fill="x", pady=(0, 4))
        sr_top.grid_columnconfigure((0, 1), weight=1, uniform="srt")

        for i, (key, label) in enumerate([
            ("sec_pis_avg",      t("pis_score_avg")),
            ("sec_pis_dominant", t("pis_factor_dominant")),
        ]):
            mf = ctk.CTkFrame(sr_top, fg_color=C["card"],
                            border_color=C["border"], border_width=1,
                            corner_radius=8)
            mf.grid(row=0, column=i, padx=2, sticky="ew")
            ctk.CTkLabel(mf, text=label, font=("Segoe UI", 9),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=10, pady=(8, 0))
            v = ctk.CTkLabel(mf, text="--", font=("Segoe UI", 14, "bold"),
                            text_color=C["blue"], anchor="w")
            v.pack(anchor="w", padx=10, pady=(0, 8))
            self.dynamic[key] = v

        # Bottom row (4 small metrics): RAM%, CPU%, Total Freed, Cycles
        sr_bot = ctk.CTkFrame(score_right, fg_color="transparent")
        sr_bot.pack(fill="x")
        sr_bot.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="srb")

        for i, (key, label) in enumerate([
            ("improve_ram_pct",   t("ai_improve_ram")),
            ("improve_cpu_pct",   t("ai_improve_cpu")),
            ("improve_freed_mb",  t("ai_improve_freed")),
            ("improve_cycles",    t("ai_improve_cycles")),
        ]):
            mf = ctk.CTkFrame(sr_bot, fg_color=C["card"],
                            border_color=C["border"], border_width=1,
                            corner_radius=6)
            mf.grid(row=0, column=i, padx=2, sticky="ew")
            ctk.CTkLabel(mf, text=label, font=("Segoe UI", 8),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=8, pady=(6, 0))
            v = ctk.CTkLabel(mf, text="0", font=("Segoe UI", 12, "bold"),
                            text_color=C["text"], anchor="w")
            v.pack(anchor="w", padx=8, pady=(0, 6))
            self.dynamic[key] = v

        # Status line
        self.dynamic["sec_improve_status"] = ctk.CTkLabel(
            ic_inner, text=t("ai_status_idle"),
            font=("Segoe UI", 11),
            text_color=C["text_2"], anchor="w")
        self.dynamic["sec_improve_status"].pack(fill="x", pady=(8, 4))

        # Detected app + active profile row
        det_row = ctk.CTkFrame(ic_inner, fg_color=C["card"],
                              border_color=C["border"], border_width=1,
                              corner_radius=8)
        det_row.pack(fill="x", pady=(8, 4))
        det_inner = ctk.CTkFrame(det_row, fg_color="transparent")
        det_inner.pack(fill="x", padx=12, pady=10)

        col1 = ctk.CTkFrame(det_inner, fg_color="transparent")
        col1.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(col1, text=t("ai_detected"), font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w").pack(anchor="w")
        self.dynamic["sec_detected_app"] = ctk.CTkLabel(
            col1, text="—", font=("Segoe UI", 13, "bold"),
            text_color=C["text"], anchor="w")
        self.dynamic["sec_detected_app"].pack(anchor="w")

        ctk.CTkLabel(det_inner, text="→", font=("Segoe UI", 16, "bold"),
                    text_color=C["blue"], width=24).pack(side="left", padx=8)

        col2 = ctk.CTkFrame(det_inner, fg_color="transparent")
        col2.pack(side="left", fill="x", expand=True)
        ctk.CTkLabel(col2, text=t("ai_active_profile"), font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w").pack(anchor="w")
        self.dynamic["sec_active_profile"] = ctk.CTkLabel(
            col2, text="—", font=("Segoe UI", 13, "bold"),
            text_color=C["blue"], anchor="w")
        self.dynamic["sec_active_profile"].pack(anchor="w")

        # ★PATCH28★ 이 판정이 무엇을 재고 무엇을 안 재는지 명시한다.
        # 좁은 측정 하나를 프로그램 전체에 대한 평결처럼 보여주면
        # 사용자는 "효과가 확실한데 0 이 뜬다" 고 느낄 수밖에 없다.
        ctk.CTkLabel(ic_inner, text=t("effect_scope_note"),
                    font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w",
                    justify="left", wraplength=820).pack(
                        fill="x", pady=(6, 0))

        ctk.CTkLabel(ic_inner, text=t("ai_baseline_note"),
                    font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w",
                    justify="left", wraplength=820).pack(
                        fill="x", pady=(8, 0))

        # Initial state: pre-fill with current improvement if running
        if self.core_mode.is_running():
            self._refresh_improve_card_from_state()

        # ─── 학습 결과 카드 ──────────────────────────────────────
        # 화면에 '무엇을 배웠는지' 를 그대로 적는다. 학습했다고 말만 하고
        # 근거를 안 보여주면 그건 그냥 마케팅 문구다.
        lc = self._card(self.content, t("learn_title"))
        lc.pack(fill="x", pady=(0, 16))
        li = ctk.CTkFrame(lc, fg_color="transparent")
        li.pack(fill="x", padx=20, pady=(0, 16))
        ctk.CTkLabel(li, text=t("learn_desc"), font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w", justify="left",
                    wraplength=800).pack(fill="x", pady=(0, 10))
        rows_box = ctk.CTkFrame(li, fg_color="transparent")
        rows_box.pack(fill="x")
        # ★PATCH26★ 학습이 무엇을 바꾸고 무엇은 안 바꾸는지 명시.
        ctk.CTkLabel(li, text=t("learn_policy_note"), font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w", justify="left",
                    wraplength=800).pack(fill="x", pady=(10, 0))
        self.dynamic["sec_learn_rows"] = rows_box
        self._render_learn_rows()

        # ─── 사용 패턴 예측 ───────────────────────────────────
        pbox = ctk.CTkFrame(li, fg_color=C["panel"], corner_radius=8)
        pbox.pack(fill="x", pady=(12, 0))
        pin = ctk.CTkFrame(pbox, fg_color="transparent")
        pin.pack(fill="x", padx=16, pady=12)
        phead = ctk.CTkFrame(pin, fg_color="transparent")
        phead.pack(fill="x")
        ctk.CTkLabel(phead, text=t("predict_title"),
                    font=("Segoe UI", 12, "bold"), text_color=C["text"],
                    anchor="w").pack(side="left")
        psw = ctk.CTkSwitch(phead, text="", command=self._on_predict_toggle,
                           progress_color=C["blue"], button_color=C["blue"],
                           button_hover_color=C["blue_dark"])
        if SETTINGS.get("ai_learn_apps", True): psw.select()
        psw.pack(side="right")
        self.dynamic["sec_predict_sw"] = psw
        self.dynamic["sec_predict_line"] = ctk.CTkLabel(
            pin, text="—", font=("Segoe UI", 12), text_color=C["blue"],
            anchor="w")
        self.dynamic["sec_predict_line"].pack(fill="x", pady=(4, 0))
        ctk.CTkLabel(pin, text=t("predict_privacy"), font=("Segoe UI", 9),
                    text_color=C["text_3"], anchor="w", justify="left",
                    wraplength=760).pack(fill="x", pady=(6, 0))
        self._render_predict_line()

        btn = ctk.CTkButton(li, text=t("learn_reset"), height=30,
                           font=("Segoe UI", 11), fg_color=C["panel"],
                           hover_color=C["border"], text_color=C["text_2"],
                           command=self._on_learn_reset)
        btn.pack(anchor="w", pady=(10, 0))

        # ─── ★PATCH26★ 실행 기록 카드 ────────────────────────────
        # 진행 카드는 '돌고 있는 동안'만 보인다. 멈춘 뒤에 무엇을 했는지
        # 확인할 방법이 없으면 테스트 결과를 되짚을 수가 없다.
        self._build_activity_card()

        # Live progress card (initially empty)
        self.dynamic["sec_progress_card"] = ctk.CTkFrame(
            self.content, fg_color=C["card"],
            border_color=C["border"], border_width=1, corner_radius=12)
        # Don't pack yet — packed only when running

        # Last result card
        self.dynamic["sec_result_card"] = ctk.CTkFrame(
            self.content, fg_color="transparent")
        self.dynamic["sec_result_card"].pack(fill="x")
        ctk.CTkLabel(self.dynamic["sec_result_card"],
                    text=t("ai_status_idle"),
                    font=("Segoe UI", 11), text_color=C["text_3"],
                    anchor="w").pack(fill="x")

    _LEARN_LABELS = {
        "ecoqos":       "EcoQoS (백그라운드 절전)",
        "bg_throttle":  "백그라운드 CPU 억제",
        "mem_priority": "백그라운드 메모리 우선순위",
        "trim":         "메모리 정리",
        "standby":      "대기 메모리 회수",
        "io_priority":  "I/O 우선순위",
        "mmcss":        "MMCSS 스케줄러 힌트",
        "affinity":     "P/E 코어 힌트",
    }

    def _render_learn_rows(self):
        """학습 결과를 표로 그린다. 판정과 표본 수를 같이 보여준다."""
        box = self.dynamic.get("sec_learn_rows")
        if not self._widget_alive(box):
            return
        for w in box.winfo_children():
            try: w.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI._render_learn_rows#0", _dx)
        try:
            rows = LEARN.summary()
        except Exception:
            rows = []
        if not rows:
            ctk.CTkLabel(box, text=t("learn_none"), font=("Segoe UI", 11),
                        text_color=C["text_3"], anchor="w").pack(fill="x")
            return
        seen = set()
        for r in rows[:8]:
            act = r["action"]
            key = (r.get("state_key"), act)
            if act in seen and not str(r.get("state_key", "")).startswith("app:"):
                continue         # 같은 액션은 대표 한 줄, 앱별 결과는 따로
            if key in seen:
                continue
            seen.add(act); seen.add(key)
            line = ctk.CTkFrame(box, fg_color="transparent")
            line.pack(fill="x", pady=3)
            _k = str(r.get("state_key", ""))
            _lab = self._LEARN_LABELS.get(act, act)
            if _k.startswith("app:"):
                _lab = "%s · %s" % (_k[4:][:14], _lab)
            ctk.CTkLabel(line, text=_lab,
                        font=("Segoe UI", 11), text_color=C["text"],
                        anchor="w", width=230).pack(side="left")
            st = r["state"]
            col = (C["blue"] if st == "helps" else
                   C["warn_text"] if st == "hurts" else C["text_3"])
            txt = t("learn_" + st)
            if st in ("helps", "hurts"):
                txt += "  (%.2f %s)" % (abs(r["delta"]), t("unit_cores"))
            ctk.CTkLabel(line, text=txt, font=("Segoe UI", 11, "bold"),
                        text_color=col, anchor="w",
                        width=200).pack(side="left")
            ctk.CTkLabel(line,
                        text=t("learn_samples", on=r["n_on"], off=r["n_off"]),
                        font=("Segoe UI", 10), text_color=C["text_3"],
                        anchor="w", width=150).pack(side="left")
            # ★PATCH26★ 판정만 보여주면 "그래서 뭘 하는데?"에 답이 없다.
            # 판정이 실제로 바꾸는 것(실행 여부)과 지금 이 순간의 상태를
            # 같이 적는다.
            ctk.CTkLabel(line, text=self._learn_policy_text(act, st),
                        font=("Segoe UI", 10), text_color=C["text_2"],
                        anchor="w").pack(side="left")

    def _render_predict_line(self):
        """예측 한 줄. 근거가 부족하면 숫자를 만들지 않고 그렇다고 말한다."""
        lbl = self.dynamic.get("sec_predict_line")
        if not self._widget_alive(lbl):
            return
        try:
            if not SETTINGS.get("ai_learn_apps", True):
                lbl.configure(text="—", text_color=C["text_3"])
                return
            top = PREDICT.predict(top=1)
            st = PREDICT.stats()
            if not top:
                lbl.configure(text=t("predict_none"), text_color=C["text_3"])
                return
            lbl.configure(text=t("predict_line", app=top[0][0][:24],
                                 pct=int(top[0][1] * 100),
                                 n=st.get("switches", 0)),
                         text_color=C["blue"])
        except Exception as _dx:
            DIAG.q("OmegaGUI._render_predict_line#0", _dx)

    def _on_predict_toggle(self):
        sw = self.dynamic.get("sec_predict_sw")
        if not sw: return
        on = bool(sw.get())
        SETTINGS.set("ai_learn_apps", on)
        if not on:
            # 끄면 수집만 멈추는 게 아니라 모아둔 것도 지운다.
            try: PREDICT.reset()
            except Exception as _dx: DIAG.q("OmegaGUI._on_predict_toggle#0", _dx)
        self._render_predict_line()
        self._toast(t("predict_toggle"))

    # ══════════════════════════════════════════════════════════════
    # ★PATCH26★ 실행 기록
    # ══════════════════════════════════════════════════════════════
    _LEARN_POLICY_KEYS = {
        "helps":    "learn_pol_keep",
        "neutral":  "learn_pol_stop",
        "hurts":    "learn_pol_stop",
        "learning": "learn_pol_test",
    }

    def _learn_policy_text(self, action, state):
        """판정 -> 실제 동작. 지금 이 순간의 블록 상태도 붙인다."""
        txt = t(self._LEARN_POLICY_KEYS.get(state, "learn_pol_test"))
        try:
            b = LEARN.block_state(action)
        except Exception:
            b = None
        if b:
            txt += " · " + t("learn_now_on" if b.get("on") else "learn_now_off")
        return txt

    def _build_activity_card(self):
        card = self._card(self.content, t("act_title"))
        card.pack(fill="x", pady=(0, 16))
        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=(0, 16))
        ctk.CTkLabel(inner, text=t("act_desc"), font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w", justify="left",
                    wraplength=800).pack(fill="x", pady=(0, 8))
        box = ctk.CTkTextbox(inner, height=220, wrap="none",
                            font=("Consolas", 11),
                            fg_color=C["panel"], text_color=C["text_2"],
                            border_width=0)
        box.pack(fill="x")
        box.configure(state="disabled")
        self.dynamic["sec_act_box"] = box
        cnt = ctk.CTkLabel(inner, text="", font=("Segoe UI", 9),
                          text_color=C["text_3"], anchor="w")
        cnt.pack(fill="x", pady=(4, 0))
        self.dynamic["sec_act_count"] = cnt

        row = ctk.CTkFrame(inner, fg_color="transparent")
        row.pack(fill="x", pady=(8, 0))
        self._secondary_btn(row, t("act_copy"),
                           self._on_activity_copy).pack(side="left")
        self._secondary_btn(row, t("act_open"),
                           self._on_activity_open).pack(side="left", padx=(8, 0))
        self._secondary_btn(row, t("act_clear"),
                           self._on_activity_clear).pack(side="left", padx=(8, 0))
        self._act_log_ver = -1
        self._act_log_t = 0.0
        self._refresh_activity_log(force=True)

    def _activity_line(self, r):
        """화면용 한 줄 — 라벨은 사용자 말로, 사유는 번역해서."""
        try:
            ts = datetime.fromtimestamp(r["ts"]).strftime("%H:%M:%S")
        except Exception:
            ts = "--:--:--"
        kind = r.get("kind")
        if kind == "cycle":
            return "%s  ---- %s %s" % (ts, r.get("label", ""), r.get("result", ""))
        mark = "OK" if r.get("ok") else "!!"
        if kind == "skip":
            mark = "--"
        lab = self._friendly_action_label(r.get("label", ""))
        line = "%s  [%s] #%d  %s" % (ts, mark, r.get("cycle", 0), lab)
        rsn = r.get("reason") or ""
        if rsn:
            line += "  (%s)" % t("act_r_" + rsn)
        res = r.get("result") or ""
        if res:
            line += "  -> %s" % res
        return line

    def _refresh_activity_log(self, force=False):
        box = self.dynamic.get("sec_act_box")
        if not self._widget_alive(box):
            return
        if self.active_section != "ai_core":
            return
        try:
            ver = ACTLOG.version()
        except Exception:
            return
        now = time.time()
        if not force:
            # 내용이 그대로면 다시 그리지 않는다. 초당 200줄을 통째로
            # 갈아끼우면 그것만으로 Tk 가 눈에 띄게 느려진다.
            if ver == getattr(self, "_act_log_ver", -1):
                return
            if now - getattr(self, "_act_log_t", 0.0) < 1.5:
                return
        self._act_log_ver = ver
        self._act_log_t = now
        try:
            rows = ACTLOG.rows(200)
            txt = ("\n".join(self._activity_line(r) for r in rows)
                   if rows else t("act_none"))
            at_end = True
            try:
                at_end = box.yview()[1] >= 0.999
            except Exception as _dx:
                DIAG.q("OmegaGUI._refresh_activity_log#0", _dx)
            box.configure(state="normal")
            box.delete("1.0", "end")
            box.insert("1.0", txt)
            box.configure(state="disabled")
            if at_end:
                try: box.see("end")
                except Exception as _dx: DIAG.q("OmegaGUI._refresh_activity_log#1", _dx)
            lbl = self.dynamic.get("sec_act_count")
            if self._widget_alive(lbl):
                lbl.configure(text=t("act_lines", n=len(rows)))
        except Exception as _dx:
            DIAG.q("OmegaGUI._refresh_activity_log#2", _dx)

    def _on_activity_copy(self):
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(ACTLOG.text(400) or "-")
            self._toast(t("act_copied"))
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_activity_copy#0", _dx)

    def _on_activity_open(self):
        try:
            p = ACTLOG.path()
            if p.exists():
                os.startfile(str(p.parent))
            else:
                os.startfile(str(p.parent) if p.parent.exists()
                             else os.environ.get("APPDATA", "."))
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_activity_open#0", _dx)

    def _on_activity_clear(self):
        try:
            ACTLOG.clear()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_activity_clear#0", _dx)
        self._refresh_activity_log(force=True)
        self._toast(t("act_cleared"))

    def _on_learn_reset(self):
        try:
            LEARN.reset()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_learn_reset#0", _dx)
        try:
            PREDICT.reset()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_learn_reset#1", _dx)
        self._render_learn_rows()
        self._render_predict_line()
        self._toast(t("learn_reset"))

    def _refresh_improve_card_from_state(self):
        """Pull latest stats from CoreMode and update the improvement card."""
        cm = self.core_mode
        if not cm.is_running(): return
        with cm._cont_lock:
            cycles      = cm._cont_cycles
            freed       = cm._cont_ram_freed_mb
            baseline_ram = cm._baseline_ram_mb
            baseline_cpu = cm._baseline_cpu_pct
            pis_history  = list(cm._cont_pis_history)
            # ★수정 2★ 첫 사이클이 끝나기 전 기본값이 0 이었다. 이 척도는
            #   50 = 변화 없음이므로 0 은 '최악의 악화'를 뜻한다. 모드를 켜자마자
            #   1~2초 동안 화면에 0점 + '악화' 등급이 떴다가 정상값으로 튀었다.
            #   (_build_stats_snapshot 은 이미 50 을 쓰고 있어 두 경로가 서로
            #   다른 값을 보내고 있었다.) 중립값 50 으로 통일한다.
            pis_score    = pis_history[-1] if pis_history else 50
            avg_pis      = (int(sum(pis_history) / len(pis_history))
                            if pis_history else 50)
            ram_hist     = list(getattr(cm, "_cont_ram_history", []))
            cpu_hist     = list(getattr(cm, "_cont_cpu_history", []))
        try:
            # ★수정 1★ 여기서 계산하던 ram_now / cpu_now 는 어디에도 쓰이지
            #   않는 죽은 코드였다. 게다가 psutil.cpu_percent(interval=None)
            #   은 psutil 내부의 전역 직전-스냅샷을 갱신한다 — UI 새로고침이
            #   0.2초마다 이걸 호출하면서 CoreMode 의 CPU 측정 구간을 잘라
            #   먹어, 점수 재료인 bg_cpu/sys_cpu 값이 실제보다 작게 나왔다.
            #   (측정용 샘플러는 이미 cpu_times 전용 스냅샷을 따로 쓴다.)
            #   호출 자체를 삭제한다.
            # 자체 메트릭 우선 — CoreMode가 계산한 ram_hist/cpu_hist 사용.
            # 히스토리가 아직 없으면 0%로 시작 (첫 사이클 직후 즉시 채워짐).
            # 음수(=악화)도 부호를 보존하고 중앙값을 쓴다.
            ram_pct = _median(ram_hist) if ram_hist else 0.0
            cpu_pct = _median(cpu_hist) if cpu_hist else 0.0
            self._apply_improve_stats({
                "ram_improve_pct":    ram_pct,
                "cpu_improve_pct":    cpu_pct,
                "total_ram_freed_mb": freed,
                "cycles":             cycles,
                "mode":               cm.get_continuous_mode(),
                "pis_score":          pis_score,
                "pis_avg":            avg_pis,
                # ★수정★ 기존엔 여기서 RAM% 와 CPU% 라는 서로 무관한 두 수를
                # 비교해 "주요 기여 요인"을 지어냈다. PIS 가 실제로 계산한
                # 지배 컴포넌트를 그대로 쓴다.
                "pis_dominant":       getattr(cm, "_last_pis_dominant", "none"),
                "pis_tier":           getattr(cm, "_last_pis_tier",
                                              "pis_tier_nodata"),
                "profile_label":      t(getattr(cm, "_last_profile_key",
                                                "profile_general")),
            })
        except Exception as _dx:
            DIAG.q("OmegaGUI._refresh_improve_card_from_state#0", _dx)

    def _widget_alive(self, w):
        """위젯이 destroy되지 않았는지 안전 체크."""
        try:
            return bool(w and w.winfo_exists())
        except Exception:
            return False

    def _apply_improve_stats(self, stats):
        """Update improvement card widgets from stats dict — 극도로 최적화됨."""
        if getattr(self, "_shutting_down", False): return

        # ★수정 3★ 아래 통계 누적(최고 점수·주 프로필)은 화면과 무관한
        #   세션 기록이다. 예전에는 active_section 검사 뒤에 있어서, 다른 탭을
        #   보고 있는 동안의 사이클이 전부 누락됐다. 보고서의 '최고 점수'가
        #   AI Core 탭을 켜 둔 시간에만 갱신되던 원인. 게이트 앞으로 옮긴다.
        pis = stats.get("pis_score", 50)
        if pis > self._last_pis_peak:
            self._last_pis_peak = pis
        pl = stats.get("profile_label", "")
        if pl and pl != t("profile_general"):
            self._last_top_profile = pl

        if getattr(self, "_switching", False): return
        if self.active_section != "ai_core": return

        try:
            # ★수정 4★ DISPLAY_MULT 는 화면에 보여줄 숫자를 부풀리던 배율의
            #   잔재다(지금은 1.0). 곱셈을 남겨두면 언젠가 다시 1.0 이 아닌
            #   값이 들어간다 — 완전히 제거한다.
            # ★개선율 % 를 걷어낸 자리★ 여기 들어가는 값은 전부
            # '우리가 한 일' 이거나 '지금 잰 절대량' 이다. 비율이 아니다.
            # (비율은 분모가 작아 잡음이면 폭주하고, 잡음을 누르면 늘 0%
            #  가 된다 — 어느 쪽도 사용자에게 정보를 주지 못했다)
            evd_eco = int(stats.get("eco_count", 0) or 0)
            evd_bg = float(stats.get("bg_cores_now", 0.0) or 0.0)
            evd_self = float(stats.get("self_cores",
                             (stats.get("self_cpu_pct", 0.0) or 0.0)) or 0.0)
            evd_avail = float(stats.get("avail_gb", 0.0) or 0.0)
            eff = stats.get("effect") or {}

            # ─── 최적화: 텍스트가 실제로 변했을 때만 configure() 호출
            if "sec_pis_score" in self.dynamic:
                new_text = str(evd_eco)
                try:
                    if self.dynamic["sec_pis_score"].cget("text") != new_text:
                        self.dynamic["sec_pis_score"].configure(text=new_text)
                except Exception: self.dynamic["sec_pis_score"].configure(text=new_text)

            if "sec_pis_tier" in self.dynamic:
                # ★수정 5★ 여기서 점수만 보고 등급을 다시 매기고 있었다.
                #   _compute_pis 는 '측정 가능한 신호가 하나도 없음'을
                #   pis_tier_nodata 로 따로 알려주는데, GUI 가 그 정보를 버리고
                #   점수 50 을 그냥 'pis_tier_stable' 로 표시했다. 결과적으로
                #   PDH 카운터가 죽어 아무것도 못 재는 상황과 정말로 변화가
                #   없는 상황이 화면에서 구분되지 않았다.
                #   CoreMode 가 준 tier_key 를 그대로 쓰고, 없을 때만 폴백한다.
                # ★점수 등급 대신 실측 판정 문장★
                # "0% / 중간" 은 고장처럼 읽힌다. 표본이 부족하면 부족하다고,
                # 차이가 흔들림보다 작으면 "차이 없음" 이라고 말한다.
                _st = eff.get("state", "idle")
                if _st == "collecting":
                    new_text = t("effect_collecting",
                                 n=eff.get("n_t", 0),
                                 need=eff.get("need_t", 6),
                                 c=eff.get("n_c", 0))
                elif _st == "none":
                    new_text = t("effect_none")
                elif _st == "control_blocked":
                    # ★패치30★ '측정 중' 으로 덮으면 끝나지 않는다.
                    new_text = t("effect_control_blocked",
                                 u=eff.get("unreleased", 0))
                elif _st == "unmeasurable":
                    # ★PATCH28★ '효과 없음' 이 아니라 '잴 수 없음' 이다.
                    # 왜 못 재는지 숫자로 같이 보여준다.
                    new_text = t("effect_unmeasurable",
                                 h="%.4f" % (eff.get("headroom") or 0.0),
                                 f="%.4f" % (eff.get("floor") or 0.0))
                elif _st in ("better", "worse"):
                    new_text = t("effect_" + _st,
                                 d="%.2f" % abs(eff.get("delta_cores") or 0.0),
                                 nt=eff.get("n_t", 0), nc=eff.get("n_c", 0))
                else:
                    new_text = t("effect_idle")
                try:
                    if self.dynamic["sec_pis_tier"].cget("text") != new_text:
                        self.dynamic["sec_pis_tier"].configure(text=new_text)
                except Exception: self.dynamic["sec_pis_tier"].configure(text=new_text)

            if "sec_pis_avg" in self.dynamic:
                new_text = "%.2f %s" % (evd_bg, t("unit_cores"))
                try:
                    if self.dynamic["sec_pis_avg"].cget("text") != new_text:
                        self.dynamic["sec_pis_avg"].configure(text=new_text)
                except Exception: self.dynamic["sec_pis_avg"].configure(text=new_text)

            # 학습 표는 자주 바뀌지 않는다 — 20회에 한 번만 다시 그린다.
            self._learn_redraw = getattr(self, "_learn_redraw", 0) + 1
            if self._learn_redraw % 20 == 0:
                try:
                    self._render_learn_rows()
                    self._render_predict_line()
                except Exception as _dx: DIAG.q("OmegaGUI._apply_improve_stats#0", _dx)

            if "sec_pis_dominant" in self.dynamic:
                # 우리가 줄인 부하 — 판정이 서기 전에는 숫자를 만들지 않는다
                dom_text = ("—" if eff.get("state") not in ("better", "worse")
                            else "%.2f %s" % (eff.get("delta_cores") or 0.0,
                                              t("unit_cores")))
                try:
                    if self.dynamic["sec_pis_dominant"].cget("text") != dom_text:
                        self.dynamic["sec_pis_dominant"].configure(text=dom_text)
                except Exception: self.dynamic["sec_pis_dominant"].configure(text=dom_text)

            # ─── 프로필 변경 토스트 (캐시로 중복 방지)
            new_profile = stats.get("profile_label")
            last_profile = getattr(self, "_last_profile_seen", None)
            # ★수정★ "Auto" 라는 영문 문자열과 직접 비교하고 있었다.
            #   프로필 라벨이 번역되면서 한국어 모드에서는 "자동" 이 되므로
            #   비교가 항상 실패해 '자동' 프로필로 돌아올 때도 토스트가 떴다.
            if (new_profile and new_profile != last_profile
                and last_profile is not None
                and new_profile not in (t("profile_general"), "")):
                fg_name, _ = get_foreground_info()
                short = (fg_name or "?").replace(".exe", "")[:20]
                self._toast(t("toast_profile_switched",
                            app=short, profile=new_profile), duration=3500)
            self._last_profile_seen = new_profile

            # ─── 작은 타일 4개 — 전부 센 값 또는 잰 절대량
            ram_freed_mb = int(stats.get('total_ram_freed_mb', 0))
            cycles = stats.get('cycles', 0)

            # ★여기 있던 개선율 % 두 칸을 절대량으로 바꿨다★
            #   예전: "평균 RAM 감소 ▼0.0% / 평균 CPU 감소 ▼0.0%"
            #   비율은 분모(백그라운드 부하)가 작아 잡음이면 폭주하고,
            #   잡음을 누르면 항상 0% 가 됐다. 둘 다 사용자에게 아무
            #   정보가 아니다. 이제 그 자리에는 지금 실제로 잰 값이 온다.
            #     · 가용 메모리(GB)      — 남은 메모리는 그 자체로 유용하다
            #     · OMEGA X 자신(코어)   — 우리 비용을 숨기지 않는다
            if "improve_ram_pct" in self.dynamic:
                new_text = "%.1f GB" % evd_avail
                try:
                    if self.dynamic["improve_ram_pct"].cget("text") != new_text:
                        self.dynamic["improve_ram_pct"].configure(text=new_text)
                except Exception: self.dynamic["improve_ram_pct"].configure(text=new_text)

            if "improve_cpu_pct" in self.dynamic:
                new_text = "%.2f %s" % (evd_self, t("unit_cores"))
                try:
                    if self.dynamic["improve_cpu_pct"].cget("text") != new_text:
                        self.dynamic["improve_cpu_pct"].configure(text=new_text)
                except Exception: self.dynamic["improve_cpu_pct"].configure(text=new_text)

            if "improve_freed_mb" in self.dynamic:
                new_text = f"{ram_freed_mb} MB"
                try:
                    if self.dynamic["improve_freed_mb"].cget("text") != new_text:
                        self.dynamic["improve_freed_mb"].configure(text=new_text)
                except Exception: self.dynamic["improve_freed_mb"].configure(text=new_text)

            if "improve_cycles" in self.dynamic:
                new_text = str(cycles)
                try:
                    if self.dynamic["improve_cycles"].cget("text") != new_text:
                        self.dynamic["improve_cycles"].configure(text=new_text)
                except Exception: self.dynamic["improve_cycles"].configure(text=new_text)

            if "sec_improve_status" in self.dynamic:
                mode = stats.get("mode", "")
                mode_label = t("ai_lite_title") if mode == "lite" else t("ai_hard_title")
                new_text = t("ai_status_running", mode=mode_label, n=cycles)
                try:
                    if self.dynamic["sec_improve_status"].cget("text") != new_text:
                        self.dynamic["sec_improve_status"].configure(text=new_text)
                except Exception: self.dynamic["sec_improve_status"].configure(text=new_text)

            if "sec_detected_app" in self.dynamic:
                fg_name, _ = get_foreground_info()
                new_text = (fg_name or "?").replace(".exe", "")[:24]
                try:
                    if self.dynamic["sec_detected_app"].cget("text") != new_text:
                        self.dynamic["sec_detected_app"].configure(text=new_text)
                except Exception: self.dynamic["sec_detected_app"].configure(text=new_text)

            if "sec_active_profile" in self.dynamic:
                new_text = new_profile or t("profile_general")
                try:
                    if self.dynamic["sec_active_profile"].cget("text") != new_text:
                        self.dynamic["sec_active_profile"].configure(text=new_text)
                except Exception: self.dynamic["sec_active_profile"].configure(text=new_text)
        except Exception as _dx: DIAG.q("OmegaGUI._apply_improve_stats#1", _dx)

    def _on_lite_core(self):
        self._toggle_continuous("lite")

    def _on_hard_core(self):
        self._toggle_continuous("hard")

    def _prompt_admin_for_mode(self, mode: str) -> bool:
        """admin 권한이 필요한 모드 시작 시 호출.
        사용자에게 UAC 재시작 동의 받고 → 동의하면 elevation + 현재 프로세스 종료.
        취소하면 False 반환 (호출자가 일반 권한으로 진행할지 결정)."""
        # CTk 다이얼로그 — 기존 UI와 일관된 모양
        dlg = ctk.CTkToplevel(self.root)
        dlg.title(f"{APP_NAME} — {t('admin_dlg_title')}")
        dlg.geometry("460x210")
        dlg.resizable(False, False)
        dlg.configure(fg_color=C["bg"])
        dlg.grab_set()
        dlg.transient(self.root)

        mode_label = t("mode_name_hard") if mode == "hard" else t("mode_name_lite")
        # ★수정★ 여기 전체가 한국어 하드코딩이라 영어로 바꿔도 안 바뀌었다.
        msg = t("admin_dlg_msg", mode=mode_label)
        ctk.CTkLabel(dlg, text=msg, font=("Segoe UI", 12),
                    text_color=C["text"], wraplength=400, justify="left",
                    anchor="w").pack(fill="x", padx=20, pady=(20, 16))

        btn_row = ctk.CTkFrame(dlg, fg_color="transparent")
        btn_row.pack(fill="x", padx=20, pady=(0, 16))

        result = {"elevated": False}

        def on_cancel():
            try: dlg.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI.on_cancel#0", _dx)

        def on_yes():
            try: dlg.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI.on_yes#0", _dx)
            if request_admin_with_action(mode):
                result["elevated"] = True
                # 새 프로세스가 admin으로 시작됨 → 현재 프로세스 즉시 종료
                try:
                    if self.core_mode and self.core_mode.is_running():
                        self.core_mode.stop_continuous()
                except Exception as _dx: DIAG.q("OmegaGUI.on_yes#1", _dx)
                try: self.root.destroy()
                except Exception as _dx: DIAG.q("OmegaGUI.on_yes#2", _dx)
                os._exit(0)

        ctk.CTkButton(btn_row, text=t("cancel"),
                     fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                     text_color=C["blue"], font=("Segoe UI", 12),
                     corner_radius=8, height=36, width=110,
                     border_width=1, border_color=C["border"],
                     command=on_cancel).pack(side="left")
        ctk.CTkButton(btn_row, text=t("admin_dlg_restart"),
                     fg_color=C["btn_primary"], hover_color=C["btn_primary_h"],
                     text_color="#FFFFFF", font=("Segoe UI", 12, "bold"),
                     corner_radius=8, height=36, width=220,
                     command=on_yes).pack(side="right")

        self.root.wait_window(dlg)
        return result["elevated"]

    def _toggle_continuous(self, mode):
        cm = self.core_mode
        # If already running this mode → stop
        if cm.is_running() and cm.get_continuous_mode() == mode:
            cm.stop_continuous()
            # Save session record
            if self.session_history:
                with cm._cont_lock:
                    final_stats = {
                        "cycles":             cm._cont_cycles,
                        "total_ram_freed_mb": cm._cont_ram_freed_mb,
                        "pis_avg":            int(sum(cm._cont_pis_history) /
                                              max(1, len(cm._cont_pis_history))),
                        "pis_peak":           max(cm._cont_pis_history) if cm._cont_pis_history else 0,
                        "top_profile":        self._last_top_profile,
                        "leaks_found":        len(self.leak_detector.get_alerts())
                                              if self.leak_detector else 0,
                    }
                self.session_history.end_session(final_stats)
            self._update_core_buttons()
            self._toast(t("complete"))
            try:
                self.dynamic["sec_improve_status"].configure(
                    text=t("ai_status_idle"))
            except Exception as _dx: DIAG.q("OmegaGUI._toggle_continuous#0", _dx)
            return
        # If running OTHER mode → stop+save first
        if cm.is_running():
            if self.session_history:
                with cm._cont_lock:
                    final_stats = {
                        "cycles":             cm._cont_cycles,
                        "total_ram_freed_mb": cm._cont_ram_freed_mb,
                        "pis_avg":            int(sum(cm._cont_pis_history) /
                                              max(1, len(cm._cont_pis_history))),
                        "pis_peak":           max(cm._cont_pis_history) if cm._cont_pis_history else 0,
                        "top_profile":        self._last_top_profile,
                    }
                self.session_history.end_session(final_stats)
            cm.stop_continuous()
            time.sleep(0.2)

        # ─── Admin 권한 체크 (START 직전) ─────────────────────────
        # Hard 모드: admin 강력 필요 → 다이얼로그 → 거부 시 시작 중단
        # Lite 모드: admin 권장이지만 없어도 일부 동작 → 그냥 진행
        if mode == "hard" and not is_admin():
            elevated = self._prompt_admin_for_mode("hard")
            # elevated=True 면 _prompt_admin_for_mode가 이미 os._exit(0) 호출함 → 도달 불가
            # 여기 오면 사용자가 취소한 것
            if not elevated:
                self._toast(t("admin_toast_skip"), duration=3500)
                # 그래도 사용자가 명시적으로 눌렀으므로 일반 권한으로라도 시작
                # (Standby purge·system cache trim 등은 silent fallback)

        # Start new session record
        if self.session_history:
            self.session_history.start_session(mode)
        self._last_pis_peak = 0
        self._last_top_profile = "Auto"

        # Reset progress display
        self._init_progress_card(mode)

        # ★수정(스레드 안전성 + GUI 부하)★
        # 기존 콜백은 CoreMode 의 워커 스레드에서 곧바로 root.after() 를
        # 호출했다. Tk 는 스레드 안전하지 않아 간헐적 프리즈/크래시의
        # 원인이 된다. 이제 워커는 deque 에 넣기만 하고(원자적 연산),
        # 메인 스레드의 펌프가 200ms 마다 꺼내 처리한다.
        def progress_cb(step):
            try: self._ui_queue.append(("step", step))
            except Exception as _dx: DIAG.q("OmegaGUI.progress_cb#0", _dx)

        def status_cb(stats):
            try: self._ui_queue.append(("stats", stats))
            except Exception as _dx: DIAG.q("OmegaGUI.status_cb#0", _dx)

        cm.start_continuous(mode, progress_cb=progress_cb,
                           status_cb=status_cb)
        self._update_core_buttons()
        self._toast(t("ai_status_running",
                     mode=t("ai_lite_title") if mode == "lite"
                          else t("ai_hard_title"),
                     n=0))

    def _update_core_buttons(self):
        """Sync button labels with current continuous mode state."""
        cm = self.core_mode
        running = cm.is_running()
        cur = cm.get_continuous_mode() if running else None
        try:
            if "sec_lite_btn" in self.dynamic:
                self.dynamic["sec_lite_btn"].configure(
                    text=t("ai_lite_run_stop") if cur == "lite"
                         else t("ai_lite_run_start"))
            if "sec_hard_btn" in self.dynamic:
                self.dynamic["sec_hard_btn"].configure(
                    text=t("ai_hard_run_stop") if cur == "hard"
                         else t("ai_hard_run_start"))
        except Exception as _dx: DIAG.q("OmegaGUI._update_core_buttons#0", _dx)

    def _init_progress_card(self, mode):
        """Initialize/reset the progress card for a new continuous run."""
        # Reset running totals
        self._running_totals = {
            "ram_freed_mb":  0,
            "procs_trimmed": 0,
            "procs_throttled": 0,
            "files_cleaned": 0,
            "bytes_freed":   0,
            "step_count":    0,
        }

        prog = self.dynamic.get("sec_progress_card")
        if not prog: return
        prog.pack(fill="x", pady=(0, 16))
        for w in prog.winfo_children(): w.destroy()

        mode_label = t("ai_lite_title") if mode == "lite" else t("ai_hard_title")
        ctk.CTkLabel(prog, text=f"  {mode_label} — {t('running')}",
                    font=("Segoe UI", 14, "bold"),
                    text_color=C["blue"],
                    anchor="w").pack(fill="x", padx=20, pady=(16, 8))

        # Live cumulative stats row (4 metrics)
        stats_row = ctk.CTkFrame(prog, fg_color=C["panel"], corner_radius=8)
        stats_row.pack(fill="x", padx=20, pady=(0, 12))
        stats_row.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="ps")

        stat_keys = [
            ("running_ram",   t("running_ram_freed")),
            ("running_procs", t("running_procs_handled")),
            ("running_files", t("running_files_cleaned")),
            ("running_steps", t("running_steps_done")),
        ]
        for i, (key, label) in enumerate(stat_keys):
            sf = ctk.CTkFrame(stats_row, fg_color="transparent")
            sf.grid(row=0, column=i, padx=4, pady=8, sticky="ew")
            ctk.CTkLabel(sf, text=label, font=("Segoe UI", 9),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=8)
            v = ctk.CTkLabel(sf, text="0", font=("Segoe UI", 14, "bold"),
                            text_color=C["blue"], anchor="w")
            v.pack(anchor="w", padx=8)
            self.dynamic[key] = v

        # Step list (capped at last 10 visible to avoid memory growth)
        ctk.CTkLabel(prog, text=t("running_action_log"),
                    font=("Segoe UI", 11), text_color=C["text_3"],
                    anchor="w").pack(fill="x", padx=20, pady=(8, 4))
        plist = ctk.CTkFrame(prog, fg_color="transparent")
        plist.pack(fill="x", padx=20, pady=(0, 16))
        self.dynamic["sec_progress_list"] = plist

        # ★GUI 최적화★ 8행을 미리 만들어두고 텍스트만 갈아끼운다.
        # 기존엔 스텝 1개마다 CTkFrame+CTkLabel 3개를 만들고 오래된 행을
        # destroy 했다. Hard Core 는 사이클당 최대 9스텝 × 4초 간격이라
        # 분당 500개 넘는 위젯이 생성/파괴되고 있었다.
        self._prog_lines.clear()
        self._prog_row_pool = []
        for _ in range(8):
            row = ctk.CTkFrame(plist, fg_color=C["panel"], corner_radius=6)
            icon = ctk.CTkLabel(row, text="", font=("Segoe UI", 14, "bold"),
                               text_color=C["blue"], width=28)
            icon.pack(side="left", padx=(8, 4), pady=8)
            lab = ctk.CTkLabel(row, text="", font=("Segoe UI", 11, "bold"),
                              text_color=C["text"], anchor="w", width=240)
            lab.pack(side="left", padx=(4, 8), pady=8)
            imp = ctk.CTkLabel(row, text="", font=("Segoe UI", 11, "bold"),
                              text_color=C["blue"], anchor="e")
            imp.pack(side="right", padx=12, pady=8)
            self._prog_row_pool.append(
                {"frame": row, "icon": icon, "lab": lab, "imp": imp,
                 "mapped": False, "cache": {}})

    def _add_progress_row(self, step):
        """Add a progress row — 극도로 최적화됨."""
        if getattr(self, "_shutting_down", False): return
        if getattr(self, "_switching", False): return
        if self.active_section != "ai_core": return
        if not self._win_visible: return   # ★GUI 최적화★ 안 보이면 그리지 않음

        cont = self.dynamic.get("sec_progress_list")
        if not self._widget_alive(cont): return

        raw_label = step.get("label", "?")
        raw_result = str(step.get("result", ""))
        ok = step.get("ok", True)

        if not hasattr(self, "_running_totals"):
            self._running_totals = {"ram_freed_mb": 0, "procs_trimmed": 0,
                                    "procs_throttled": 0, "files_cleaned": 0,
                                    "bytes_freed": 0, "step_count": 0}
        self._running_totals["step_count"] += 1
        self._update_running_totals_from_text(raw_label, raw_result)

        # ★GUI 최적화★ 위젯 생성 없이 풀의 라벨만 갱신.
        # 여기서는 줄만 쌓아두고, 실제 그리기는 펌프가 한 번만 호출한다
        # (한 사이클에 스텝이 9개 와도 다시 그리는 건 1번).
        # ★언어 전환 수정★ 예전에는 여기서 번역까지 끝낸 문자열을 큐에
        # 넣었다. 그래서 언어를 바꾸면 이미 쌓인 진행 로그 8줄이 옛 언어로
        # 그대로 남았다(섹션을 다시 그려도 큐 내용이 옛 언어라 소용없음).
        # 원본 라벨·결과만 저장하고 번역은 _render_progress_rows 에서 한다.
        self._prog_lines.append((ok, raw_label, raw_result))
        self._prog_dirty = True

    def _render_progress_rows(self):
        if not getattr(self, "_prog_dirty", False): return
        self._prog_dirty = False
        if not self._win_visible: return
        if self.active_section != "ai_core": return
        pool = self._prog_row_pool
        if not pool:
            return
        lines = list(self._prog_lines)
        for i, r in enumerate(pool):
            if i >= len(lines):
                if r["mapped"]:
                    try: r["frame"].pack_forget()
                    except Exception as _dx: DIAG.q("OmegaGUI._render_progress_rows#0", _dx)
                    r["mapped"] = False
                continue
            l_ok, l_raw_label, l_raw_result = lines[i]
            # 번역은 렌더 시점에 — 언어를 바꾸면 같은 큐가 새 언어로 다시 그려진다.
            l_lab = self._friendly_action_label(l_raw_label)
            l_imp = self._extract_impact(l_raw_label, l_raw_result)
            cache = r["cache"]
            try:
                icon_txt = "✓" if l_ok else "×"
                icon_col = C["blue"] if l_ok else C["danger_text"]
                if cache.get("icon") != icon_txt:
                    r["icon"].configure(text=icon_txt, text_color=icon_col)
                    cache["icon"] = icon_txt
                if cache.get("lab") != l_lab:
                    r["lab"].configure(text=l_lab); cache["lab"] = l_lab
                if cache.get("imp") != l_imp:
                    r["imp"].configure(text=l_imp); cache["imp"] = l_imp
                if not r["mapped"]:
                    r["frame"].pack(fill="x", pady=2)
                    r["mapped"] = True
            except Exception as _dx:
                DIAG.q("OmegaGUI._render_progress_rows#1", _dx)

        self._refresh_running_totals()

    # ★신규★ step() 에 넘기는 영문 라벨 → i18n 키 정확 매칭표.
    # 기존에는 아래 mapping 의 부분문자열 매칭만 있었는데, 47개 라벨 중
    # 12개가 어떤 키워드에도 걸리지 않아 한국어 모드에서 영어로 남았다
    # ("Light memory trim", "P/E core scheduling hint", "GPU queue priority" 등).
    # 정확 매칭을 먼저 보고, 못 찾으면 기존 부분문자열 매칭으로 폴백한다.
    STEP_LABEL_KEYS = {
        "trim idle background processes":        "friendly_memory_cleanup",
        "deep memory trim (aggressive)":         "friendly_memory_cleanup",
        "light memory trim":                     "friendly_light_memory",
        "apply ecoqos to background apps":       "friendly_energy_saving",
        "ecoqos for all background apps":        "friendly_energy_saving",
        "light energy-save (background)":        "friendly_energy_saving",
        "energy-save mode for background apps":  "friendly_energy_saving",
        "throttle background cpu usage":         "friendly_cpu_balance",
        "throttle high-cpu background tasks":    "friendly_cpu_balance",
        "lower background cpu usage (8s)":       "friendly_cpu_balance",
        "lower background cpu usage (12s)":      "friendly_cpu_balance",
        "boost foreground app priority":         "friendly_app_boost",
        "boost foreground threads":              "friendly_app_boost",
        "boost foreground app threads":          "friendly_app_boost",
        "elevate foreground i/o priority":       "friendly_disk_priority",
        "elevate foreground i/o":                "friendly_disk_priority",
        "foreground i/o priority":               "friendly_disk_priority",
        "gaming i/o priority boost":             "friendly_disk_priority",
        "creative i/o elevation":                "friendly_disk_priority",
        "dev i/o priority boost":                "friendly_disk_priority",
        "pause windows background services":     "friendly_pause_services",
        "pause windows background services (5min)": "friendly_pause_services",
        "disable gamedvr background recording":  "friendly_disable_recording",
        "register mmcss scheduler hint":         "friendly_audio_priority",
        "gaming scheduler hint (mmcss)":         "friendly_audio_priority",
        "creative audio scheduling":             "friendly_audio_priority",
        "apply hybrid cpu hint":                 "friendly_cpu_smart",
        "p/e core scheduling hint":              "friendly_pe_core_hint",
        "switch to high performance power":      "friendly_power_mode",
        "gaming: switch to high performance power": "friendly_power_mode",
        "trim system file cache":                "friendly_disk_cache",
        "creative: trim disk cache":             "friendly_disk_cache",
        "flush dns cache":                       "friendly_dns_flush",
        "compact standby memory list":           "friendly_memory_compact",
        "reclaim standby memory":                "friendly_memory_compact",
        "background memory priority":            "friendly_bg_mem_priority",
        "block timer-resolution hijacking":      "friendly_timer_guard",
        "gpu queue priority":                    "friendly_gpu_priority",
        "browser balance tuning":                "friendly_browser_tuning",
    }

    def _friendly_action_label(self, raw_label: str) -> str:
        """Convert technical action label to user-friendly description — 캐시 적용.

        ★언어 전환 주의★ 캐시 키는 원본 영문 라벨이지만 값은 '번역된' 문자열이다.
        따라서 언어를 바꾸면 _on_lang_change 가 이 캐시를 반드시 비워야 한다.
        """
        # 캐시 초기화 (세션당 한 번)
        if not hasattr(self, "_friendly_label_cache"):
            self._friendly_label_cache = {}

        cache_key = raw_label.lower().strip()
        if cache_key in self._friendly_label_cache:
            return self._friendly_label_cache[cache_key]

        # ① 정확 매칭 우선
        exact = self.STEP_LABEL_KEYS.get(cache_key)
        if exact:
            result = t(exact)
            self._friendly_label_cache[cache_key] = result
            return result

        # ② 부분문자열 폴백(사용자 정의/신규 라벨 대비)
        mapping = [
            (("trim idle", "유휴", "공격적 메모리", "deep memory", "aggressive"),
             "friendly_memory_cleanup"),
            (("ecoqos", "에너지", "background app", "백그라운드"),
             "friendly_energy_saving"),
            (("throttle", "억제", "cpu hogs"),
             "friendly_cpu_balance"),
            (("foreground threads", "포그라운드 스레드", "boost foreground"),
             "friendly_app_boost"),
            (("i/o priority", "io priority", "i/o"),
             "friendly_disk_priority"),
            (("pause windows", "백그라운드 서비스", "bg services"),
             "friendly_pause_services"),
            (("gamedvr", "게임dvr", "배경 녹화"),
             "friendly_disable_recording"),
            (("clean temp", "임시 파일"),
             "friendly_clean_temp"),
            (("mmcss", "스케줄러 힌트", "멀티미디어"),
             "friendly_audio_priority"),
            (("hybrid cpu", "하이브리드"),
             "friendly_cpu_smart"),
            (("high performance", "고성능 전원"),
             "friendly_power_mode"),
            (("system file cache", "시스템 파일"),
             "friendly_disk_cache"),
            (("dns", "flush"),
             "friendly_dns_flush"),
            (("standby", "대기 메모리"),
             "friendly_memory_compact"),
        ]

        for keywords, friendly_key in mapping:
            if any(k in cache_key for k in keywords):
                result = t(friendly_key)
                self._friendly_label_cache[cache_key] = result
                return result

        self._friendly_label_cache[cache_key] = raw_label
        return raw_label

    def _extract_impact(self, raw_label: str, raw_result: str) -> str:
        """Extract a short impact summary from the result text — 최적화됨."""
        import re
        rl = raw_label.lower()
        rr = raw_result.lower()

        # 한 번만 검색 실행
        mb_match = re.search(r'(\d+(?:\.\d+)?)\s*mb', rr)
        proc_match = re.search(r'(\d+)\s*(?:processes|process|개)', rr)
        file_match = re.search(r'(\d+(?:,\d+)?)\s*(?:files|file|개 파일)', rr)
        size_match = re.search(r'\(([0-9.]+\s*[kmgt]?b)\)', rr, re.I)

        # Early exit로 불필요한 조건문 제거
        if any(k in rl for k in ("trim", "정리", "memory", "메모리")):
            if mb_match: return t("impact_ram_freed", mb=mb_match.group(1))
            if proc_match: return t("impact_procs_handled", count=proc_match.group(1))

        if any(k in rl for k in ("throttle", "ecoqos", "에너지", "억제", "background")):
            if proc_match: return t("impact_procs_handled", count=proc_match.group(1))

        if any(k in rl for k in ("clean", "temp", "정리", "임시")):
            if file_match and size_match: return f"{file_match.group(1)} · {size_match.group(1)}"
            if file_match: return t("impact_files", count=file_match.group(1))

        if "disable" in rl or "비활성화" in rl:
            if "disabled" in rr or "비활성화됨" in rr: return t("impact_disabled")

        if mb_match: return t("impact_ram_freed", mb=mb_match.group(1))
        if proc_match: return t("impact_procs_handled", count=proc_match.group(1))
        if "ok" in rr or "set" in rr or "설정" in rr or "완료" in rr:
            return t("impact_applied")
        if "skipped" in rr or "skip" in rr or "건너뜀" in rr:
            return t("impact_skipped")
        return (raw_result[:24] + "…") if len(raw_result) > 24 else raw_result

    def _update_running_totals_from_text(self, raw_label: str,
                                         raw_result: str):
        """Parse result text and add to running totals — 최적화됨."""
        import re
        rr = raw_result.lower()
        rl = raw_label.lower()

        # 정규표현식 한 번만 실행
        mb_match = re.search(r'(\d+(?:\.\d+)?)\s*mb\s+(?:freed|회수|회복)?', rr)
        proc_match = re.search(r'(\d+)', rr)
        file_match = re.search(r'(\d+(?:,\d+)?)\s*(?:files|개 파일)', rr)

        # MB freed
        if mb_match and any(k in rl for k in ("trim", "memory", "메모리", "정리")):
            try:
                self._running_totals["ram_freed_mb"] += int(float(mb_match.group(1)))
            except Exception as _dx: DIAG.q("OmegaGUI._update_running_totals_from_text#0", _dx)

        # Process counts
        if proc_match:
            try:
                n = int(proc_match.group(1))
                if any(k in rl for k in ("trim", "정리", "memory", "메모리")):
                    self._running_totals["procs_trimmed"] += n
                elif any(k in rl for k in ("throttle", "억제", "ecoqos", "에너지")):
                    self._running_totals["procs_throttled"] += n
            except Exception as _dx: DIAG.q("OmegaGUI._update_running_totals_from_text#1", _dx)

        # Files
        if file_match:
            try:
                count = int(file_match.group(1).replace(",", ""))
                self._running_totals["files_cleaned"] += count
            except Exception as _dx: DIAG.q("OmegaGUI._update_running_totals_from_text#2", _dx)

    def _refresh_running_totals(self):
        """Update the live totals row at the top of the progress card — 최적화됨."""
        rt = getattr(self, "_running_totals", None)
        if not rt: return

        # 캐시로 중복 업데이트 방지
        if not hasattr(self, "_running_totals_cache"):
            self._running_totals_cache = {}

        try:
            if "running_ram" in self.dynamic:
                new_text = f"{rt['ram_freed_mb']} MB"
                if self._running_totals_cache.get("ram") != new_text:
                    self.dynamic["running_ram"].configure(text=new_text)
                    self._running_totals_cache["ram"] = new_text

            if "running_procs" in self.dynamic:
                total_procs = rt["procs_trimmed"] + rt["procs_throttled"]
                new_text = str(total_procs)
                if self._running_totals_cache.get("procs") != new_text:
                    self.dynamic["running_procs"].configure(text=new_text)
                    self._running_totals_cache["procs"] = new_text

            if "running_files" in self.dynamic:
                new_text = f"{rt['files_cleaned']:,}"
                if self._running_totals_cache.get("files") != new_text:
                    self.dynamic["running_files"].configure(text=new_text)
                    self._running_totals_cache["files"] = new_text

            if "running_steps" in self.dynamic:
                new_text = str(rt["step_count"])
                if self._running_totals_cache.get("steps") != new_text:
                    self.dynamic["running_steps"].configure(text=new_text)
                    self._running_totals_cache["steps"] = new_text
        except Exception as _dx: DIAG.q("OmegaGUI._refresh_running_totals#0", _dx)

    def _show_core_result(self, result):
        cont = self.dynamic.get("sec_result_card")
        if not cont: return
        for w in cont.winfo_children(): w.destroy()

        before = result["before"]; after = result["after"]
        ram_freed = result["ram_freed_mb"]
        cpu_delta = result["cpu_delta"]
        steps = result["step_count"]

        # Result card
        card = ctk.CTkFrame(cont, fg_color=C["blue_subtle"],
                          border_color=C["blue"], border_width=2,
                          corner_radius=12)
        card.pack(fill="x")

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=24, pady=20)

        ctk.CTkLabel(inner,
                    text=t("ai_complete", mode=result['mode']),
                    font=("Segoe UI", 16, "bold"),
                    text_color=C["blue"], anchor="w").pack(fill="x", pady=(0, 12))

        # Metrics row
        m_row = ctk.CTkFrame(inner, fg_color="transparent")
        m_row.pack(fill="x")
        m_row.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="r")

        for i, (label, value) in enumerate([
            (t("ai_ram_freed"),  f"{ram_freed} MB"),
            (t("ai_cpu_lower"),  f"-{cpu_delta:.1f}%"),
            (t("ai_ram_before"), f"{before['ram_used_mb']} MB"),
            (t("ai_ram_after"),  f"{after['ram_used_mb']} MB"),
        ]):
            mf = ctk.CTkFrame(m_row, fg_color=C["card"], corner_radius=8,
                            border_color=C["border"], border_width=1)
            mf.grid(row=0, column=i, padx=4, sticky="ew")
            ctk.CTkLabel(mf, text=label, font=("Segoe UI", 9),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=10, pady=(8, 0))
            ctk.CTkLabel(mf, text=value, font=("Segoe UI", 16, "bold"),
                        text_color=C["blue"],
                        anchor="w").pack(anchor="w", padx=10, pady=(0, 8))

        ctk.CTkLabel(inner,
                    text=t("ai_actions_done", count=steps),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x", pady=(12, 0))

    # ────────────────────────────────────────────────────────────
    #  PC BOOST (Optimizer profiles)
    # ────────────────────────────────────────────────────────────
    def _build_optimizer(self):
        ctk.CTkLabel(self.content, text=t("opt_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        # Profile card
        prof_card = self._card(self.content, t("opt_profile"))
        prof_card.pack(fill="x", pady=(0, 16))

        prof_inner = ctk.CTkFrame(prof_card, fg_color="transparent")
        prof_inner.pack(fill="x", padx=20, pady=(0, 20))
        prof_inner.grid_columnconfigure((0, 1, 2), weight=1, uniform="p")

        self.dynamic["sec_prof_btns"] = {}
        for i, p in enumerate(PolicyEngine.PROFILES):
            r, c = divmod(i, 3)
            is_active = (p == self.policy.profile)
            btn = ctk.CTkButton(
                prof_inner, text=p,
                fg_color=C["blue"] if is_active else C["btn_sec"],
                text_color="#FFFFFF" if is_active else C["blue"],
                hover_color=C["blue_dark"] if is_active else C["btn_sec_h"],
                font=("Segoe UI", 12, "bold" if is_active else "normal"),
                corner_radius=8, height=40,
                border_width=0 if is_active else 1,
                border_color=C["border"],
                command=lambda pr=p: self._set_profile(pr),
            )
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="ew")
            self.dynamic["sec_prof_btns"][p] = btn

        # Action card
        act_card = self._card(self.content, t("opt_active"))
        act_card.pack(fill="x", pady=(0, 16))

        act_inner = ctk.CTkFrame(act_card, fg_color="transparent")
        act_inner.pack(fill="x", padx=20, pady=(0, 20))

        action_descs = [
            (t("opt_thread_title"),
             t("opt_thread_desc"), "always"),
            (t("opt_io_title"),
             t("opt_io_desc"), "always"),
            (t("opt_throttle_title"),
             t("opt_throttle_desc"), "always"),
            (t("opt_mmcss_title"),
             t("opt_mmcss_desc"), "always"),
            (t("opt_eco_title"),
             t("opt_eco_desc"), "win11_22h2"),
            (t("opt_timer_title"),
             t("opt_timer_desc"), "toggle_timer"),
            (t("opt_aff_title"),
             t("opt_aff_desc"), "toggle_affinity"),
        ]
        for title, desc, mode in action_descs:
            self._action_row(act_inner, title, desc, mode)

        # Manual boost
        man_card = self._card(self.content, t("opt_quick"))
        man_card.pack(fill="x", pady=(0, 16))
        man_inner = ctk.CTkFrame(man_card, fg_color="transparent")
        man_inner.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(man_inner,
                    text=t("opt_quick_desc"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 12))
        self._primary_btn(man_inner, t("opt_quick_btn"),
                         self._on_optimize_now).pack(fill="x")

        # Honest note
        note_card = ctk.CTkFrame(self.content, fg_color=C["panel"],
                                corner_radius=8)
        note_card.pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(
            note_card,
            text=t("opt_honest_note"),
            font=("Segoe UI", 10), text_color=C["text_3"],
            anchor="w", justify="left", wraplength=820,
        ).pack(fill="x", padx=16, pady=12)

    def _action_row(self, parent, title, desc, mode):
        row = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=8)
        row.pack(fill="x", pady=4)
        tf = ctk.CTkFrame(row, fg_color="transparent")
        tf.pack(side="left", fill="both", expand=True, padx=16, pady=12)
        ctk.CTkLabel(tf, text=title, font=("Segoe UI", 12, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")
        ctk.CTkLabel(tf, text=desc, font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w").pack(fill="x")
        if mode == "always":
            ctk.CTkLabel(row, text=t("sidebar_active"),
                        font=("Segoe UI", 11, "bold"),
                        text_color=C["blue"]).pack(side="right",
                                                  padx=16, pady=12)
        elif mode == "win11_22h2":
            txt = "● Active" if IS_WIN11_22H2 else "Unavailable"
            color = C["blue"] if IS_WIN11_22H2 else C["text_3"]
            ctk.CTkLabel(row, text=txt, font=("Segoe UI", 11, "bold"),
                        text_color=color).pack(side="right", padx=16, pady=12)
        elif mode == "toggle_timer":
            sw = ctk.CTkSwitch(row, text="", command=self._on_timer_toggle,
                              progress_color=C["blue"], button_color=C["blue"],
                              button_hover_color=C["blue_dark"])
            if self.policy.timer_burst_enabled: sw.select()
            sw.pack(side="right", padx=16, pady=12)
            self.dynamic["sec_timer_sw"] = sw
        elif mode == "toggle_affinity":
            if not IS_HYBRID:
                ctk.CTkLabel(row, text=t("opt_na"),
                            font=("Segoe UI", 10),
                            text_color=C["text_3"]).pack(
                                side="right", padx=16, pady=12)
            else:
                sw = ctk.CTkSwitch(row, text="",
                                  command=self._on_affinity_toggle,
                                  progress_color=C["blue"],
                                  button_color=C["blue"],
                                  button_hover_color=C["blue_dark"])
                if self.policy.affinity_hint_enabled: sw.select()
                sw.pack(side="right", padx=16, pady=12)
                self.dynamic["sec_affinity_sw"] = sw

    # ────────────────────────────────────────────────────────────
    #  STORAGE
    # ────────────────────────────────────────────────────────────
    def _build_storage(self):
        ctk.CTkLabel(self.content, text=t("storage_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        # Disk overview
        disk_card = self._card(self.content, t("storage_drive"))
        disk_card.pack(fill="x", pady=(0, 16))
        disk_inner = ctk.CTkFrame(disk_card, fg_color="transparent")
        disk_inner.pack(fill="x", padx=20, pady=(0, 20))

        snap = self._ui_snap()
        used_gb = snap.get("disk_total_gb", 0) - snap.get("disk_free_gb", 0)
        disk_pct = snap.get("disk_pct", 0)

        info = ctk.CTkFrame(disk_inner, fg_color="transparent")
        info.pack(fill="x", pady=(0, 12))
        ctk.CTkLabel(info,
                    text=f"{used_gb:.1f} GB / {snap.get('disk_total_gb', 0):.1f} GB",
                    font=("Segoe UI", 18, "bold"),
                    text_color=C["text"], anchor="w").pack(side="left")
        ctk.CTkLabel(info, text=t("storage_used", pct=int(disk_pct)),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="e").pack(side="right")

        bar = ctk.CTkProgressBar(disk_inner, progress_color=C["blue"],
                                fg_color=C["border"], height=8)
        bar.set(disk_pct / 100.0 if disk_pct else 0)
        bar.pack(fill="x", pady=(0, 12))

        # Cleanup card
        clean_card = self._card(self.content, t("storage_tools"))
        clean_card.pack(fill="x", pady=(0, 16))
        clean_inner = ctk.CTkFrame(clean_card, fg_color="transparent")
        clean_inner.pack(fill="x", padx=20, pady=(0, 20))

        btn_row = ctk.CTkFrame(clean_inner, fg_color="transparent")
        btn_row.pack(fill="x", pady=(0, 12))
        self._primary_btn(btn_row, t("storage_scan"),
                         self._on_scan_temp, height=40).pack(
            side="left", fill="x", expand=True, padx=(0, 6))
        self._secondary_btn(btn_row, t("storage_recycle"),
                           self._on_empty_recycle, height=40).pack(
            side="left", fill="x", expand=True, padx=(6, 0))

        self.dynamic["sec_scan_results"] = ctk.CTkFrame(
            clean_inner, fg_color="transparent")
        self.dynamic["sec_scan_results"].pack(fill="x", pady=(8, 0))
        ctk.CTkLabel(self.dynamic["sec_scan_results"],
                    text=t("storage_initial"),
                    font=("Segoe UI", 11), text_color=C["text_3"],
                    anchor="w").pack(fill="x")

    # ────────────────────────────────────────────────────────────
    #  APPS & TASKS
    # ────────────────────────────────────────────────────────────
    def _build_apps(self):
        ctk.CTkLabel(self.content,
                    text=t("apps_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        sub_row = ctk.CTkFrame(self.content, fg_color="transparent")
        sub_row.pack(fill="x", pady=(0, 12))

        self.app_subtab = "processes"
        self.dynamic["sec_subtab_btns"] = {}
        for sid, label in [("processes", t("apps_running")),
                          ("startup", t("apps_startup"))]:
            btn = ctk.CTkButton(
                sub_row, text=label,
                fg_color=C["blue"] if sid == self.app_subtab else "transparent",
                text_color="#FFFFFF" if sid == self.app_subtab else C["text_2"],
                hover_color=C["blue_dark"] if sid == self.app_subtab else C["panel"],
                font=("Segoe UI", 12, "bold"),
                corner_radius=8, height=36,
                command=lambda s=sid: self._switch_app_subtab(s),
            )
            btn.pack(side="left", padx=(0, 8))
            self.dynamic["sec_subtab_btns"][sid] = btn

        ctk.CTkButton(sub_row, text=t("ui_refresh"),
                     fg_color="transparent", text_color=C["blue"],
                     hover_color=C["panel"], font=("Segoe UI", 11),
                     corner_radius=8, height=36, width=80,
                     command=self._refresh_app_subtab).pack(side="right")

        self.dynamic["sec_app_content"] = ctk.CTkFrame(
            self.content, fg_color="transparent")
        self.dynamic["sec_app_content"].pack(fill="both", expand=True)
        self._render_app_subtab()

    def _switch_app_subtab(self, sid):
        self.app_subtab = sid
        for s, btn in self.dynamic["sec_subtab_btns"].items():
            is_active = (s == sid)
            btn.configure(
                fg_color=C["blue"] if is_active else "transparent",
                text_color="#FFFFFF" if is_active else C["text_2"],
                hover_color=C["blue_dark"] if is_active else C["panel"],
            )
        self._render_app_subtab()

    def _render_app_subtab(self):
        cont = self.dynamic.get("sec_app_content")
        if not cont: return
        for w in cont.winfo_children(): w.destroy()
        self._proc_row_pool = []          # 풀 무효화 (부모가 사라졌으므로)
        self.dynamic.pop("sec_proc_list", None)
        if self.app_subtab == "processes":
            self._render_processes(cont)
        else:
            self._render_startup(cont)

    PROC_ROW_COUNT = 30

    def _render_processes(self, parent):
        """★GUI 최적화★ 행 풀 재사용 + 이름 검색 + 열 정렬.

        행 풀: 새로고침마다 30행 × 위젯 8개를 destroy/재생성하던 것을
        한 번만 만들고 텍스트만 configure 로 갈아끼운다.

        ★추가★ 예전에는 정렬이 CPU 내림차순 고정이고 검색이 없어서,
        찾는 프로세스가 상위 30위 밖이면 화면에 나올 방법이 없었다.
        또 '상태' 열은 psutil 이 Windows 에서 running/stopped 만
        돌려주므로 사실상 항상 running — 자리만 먹어서 PID 로 바꿨다.
        """
        # ── 검색 줄 ──
        tool = ctk.CTkFrame(parent, fg_color="transparent")
        tool.pack(fill="x", pady=(0, 8))
        ent = ctk.CTkEntry(
            tool, placeholder_text=t("apps_search_ph"),
            width=300, height=34, corner_radius=8,
            fg_color=C["card"], border_color=C["border"],
            text_color=C["text"], font=("Segoe UI", 12))
        ent.pack(side="left")
        if self._proc_query:
            try: ent.insert(0, self._proc_query)
            except Exception as _dx: DIAG.q("OmegaGUI._render_processes#0", _dx)
        ent.bind("<KeyRelease>",
                lambda e, w=ent: self._on_proc_search(w.get()))
        self.dynamic["sec_proc_search"] = ent

        proc_card = self._card(parent, padding=0)
        proc_card.pack(fill="both", expand=True)

        header = ctk.CTkFrame(proc_card, fg_color=C["panel"], height=40)
        header.pack(fill="x", padx=1, pady=(1, 0))
        header.pack_propagate(False)
        self._proc_hdr = {}
        for key, label, w in [
                ("name", t("apps_col_process"), 240),
                ("pid",  t("apps_col_pid"), 64),
                ("cpu",  t("apps_col_cpu"), 70),
                ("ram",  t("apps_col_ram"), 70),
                ("thr",  t("apps_col_threads"), 70),
                (None,   t("apps_col_actions"), 200)]:
            if key is None:
                ctk.CTkLabel(header, text=label,
                            font=("Segoe UI", 10, "bold"),
                            text_color=C["text_2"], anchor="w",
                            width=w).pack(side="left", padx=8, pady=10)
                continue
            btn = ctk.CTkButton(
                header, text=label, width=w, height=26, anchor="w",
                font=("Segoe UI", 10, "bold"),
                fg_color="transparent", hover_color=C["border_soft"],
                text_color=C["text_2"], corner_radius=6,
                command=lambda k=key: self._on_proc_sort(k))
            btn.pack(side="left", padx=8, pady=7)
            self._proc_hdr[key] = (btn, label)
        self._update_sort_headers()

        list_frame = ctk.CTkScrollableFrame(proc_card, fg_color="transparent",
                                           height=420)
        list_frame.pack(fill="both", expand=True)
        self.dynamic["sec_proc_list"] = list_frame
        self._proc_row_pool = []
        # 검색 결과가 없을 때 안내(평소엔 pack 하지 않는다)
        self.dynamic["sec_proc_empty"] = ctk.CTkLabel(
            list_frame, text=t("apps_no_match"),
            font=("Segoe UI", 11), text_color=C["text_3"])
        self._update_process_rows(force=True)

    def _make_proc_row(self, parent):
        """빈 행 위젯 1개 생성 (내용은 나중에 채운다)."""
        row = ctk.CTkFrame(parent, fg_color=C["card"], corner_radius=0,
                          height=44)
        row.pack_propagate(False)
        name = ctk.CTkLabel(row, text="", font=("Segoe UI", 11),
                           text_color=C["text"], anchor="w", width=240)
        name.pack(side="left", padx=8, pady=10)
        pid = ctk.CTkLabel(row, text="", font=("Segoe UI", 10),
                          text_color=C["text_3"], anchor="w", width=64)
        pid.pack(side="left", padx=8, pady=10)
        cpu = ctk.CTkLabel(row, text="", font=("Segoe UI", 11),
                          text_color=C["text"], anchor="w", width=70)
        cpu.pack(side="left", padx=8, pady=10)
        ram = ctk.CTkLabel(row, text="", font=("Segoe UI", 11),
                          text_color=C["text"], anchor="w", width=70)
        ram.pack(side="left", padx=8, pady=10)
        thr = ctk.CTkLabel(row, text="", font=("Segoe UI", 11),
                          text_color=C["text_2"], anchor="w", width=70)
        thr.pack(side="left", padx=8, pady=10)
        af = ctk.CTkFrame(row, fg_color="transparent")
        af.pack(side="left", padx=4, pady=4)
        boost = ctk.CTkButton(af, text=t("apps_btn_boost"), width=56, height=28,
                             fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                             text_color=C["blue"], font=("Segoe UI", 10),
                             corner_radius=6, command=lambda: None)
        thrt = ctk.CTkButton(af, text=t("apps_btn_throttle"), width=64,
                            height=28, fg_color=C["btn_sec"],
                            hover_color=C["btn_sec_h"], text_color=C["blue"],
                            font=("Segoe UI", 10), corner_radius=6,
                            command=lambda: None)
        endb = ctk.CTkButton(af, text=t("apps_btn_end"), width=44, height=28,
                            fg_color=C["btn_danger"],
                            hover_color=C["btn_danger_h"],
                            text_color=C["danger_text"],
                            font=("Segoe UI", 10), corner_radius=6,
                            command=lambda: None)
        return {"frame": row, "name": name, "pid": pid, "cpu": cpu,
                "ram": ram, "thr": thr, "af": af, "boost": boost,
                "thrt": thrt, "end": endb,
                "cache": {}, "btns": False, "mapped": False}

    def _proc_sort_value(self, p):
        key = self._proc_sort
        if key == "name":
            return str(p.get("name", "")).lower()
        if key == "pid":
            try: return int(p.get("pid") or 0)
            except Exception: return 0
        if key == "ram":
            try: return float(p.get("memory_percent") or 0)
            except Exception: return 0.0
        if key == "thr":
            try: return int(p.get("num_threads") or 0)
            except Exception: return 0
        try: return float(p.get("cpu_percent") or 0)
        except Exception: return 0.0

    def _update_process_rows(self, force=False):
        """행 내용만 갱신. 위젯은 재사용한다."""
        list_frame = self.dynamic.get("sec_proc_list")
        if not self._widget_alive(list_frame):
            return
        # ★화면 갱신은 프로세스 워크를 기다리지 않는다★
        procs = self._procs_nowait(force=force)
        q = self._proc_query
        if q:
            procs = [p for p in procs
                     if q in str(p.get("name", "")).lower()]
        try:
            procs.sort(key=self._proc_sort_value, reverse=self._proc_desc)
        except Exception as _dx:
            DIAG.q("OmegaGUI._update_process_rows#0", _dx)
        procs = procs[:self.PROC_ROW_COUNT]

        empty = self.dynamic.get("sec_proc_empty")
        if self._widget_alive(empty):
            try:
                if not procs and q:
                    empty.pack(pady=24)
                else:
                    empty.pack_forget()
            except Exception as _dx:
                DIAG.q("OmegaGUI._update_process_rows#1", _dx)

        pool = self._proc_row_pool
        while len(pool) < len(procs):
            try:
                pool.append(self._make_proc_row(list_frame))
            except Exception:
                break

        for i, r in enumerate(pool):
            if i >= len(procs):
                if r["mapped"]:
                    try: r["frame"].pack_forget()
                    except Exception as _dx: DIAG.q("OmegaGUI._update_process_rows#2", _dx)
                    r["mapped"] = False
                continue
            p = procs[i]
            pid = p.get("pid")
            name = p.get("name", "?")
            is_sys = name.lower() in SYSTEM_WHITELIST
            vals = {
                "name": name,
                "pid":  str(pid),
                "cpu":  f"{p.get('cpu_percent', 0) or 0:.1f}",
                "ram":  f"{p.get('memory_percent', 0) or 0:.1f}",
                "thr":  str(p.get("num_threads", "-")),
            }
            cache = r["cache"]
            try:
                for key, val in vals.items():
                    if cache.get(key) != val:
                        if key == "name":
                            r[key].configure(
                                text=val,
                                text_color=C["text_3"] if is_sys else C["text"])
                        else:
                            r[key].configure(text=val)
                        cache[key] = val
                if cache.get("bind") != pid:
                    r["boost"].configure(
                        command=lambda pid=pid: self._on_proc_boost(pid))
                    r["thrt"].configure(
                        command=lambda pid=pid: self._on_proc_throttle(pid))
                    r["end"].configure(
                        command=lambda pid=pid: self._on_proc_kill(pid))
                    cache["bind"] = pid
                # 시스템 프로세스는 조작 버튼 숨김
                if is_sys and r["btns"]:
                    r["boost"].pack_forget(); r["thrt"].pack_forget()
                    r["end"].pack_forget()
                    r["btns"] = False
                elif not is_sys and not r["btns"]:
                    r["boost"].pack(side="left", padx=2)
                    r["thrt"].pack(side="left", padx=2)
                    r["end"].pack(side="left", padx=2)
                    r["btns"] = True
                if not r["mapped"]:
                    r["frame"].pack(fill="x", pady=1)
                    r["mapped"] = True
            except Exception as _dx:
                DIAG.q("OmegaGUI._update_process_rows#3", _dx)

    def _render_startup(self, parent):
        s_card = self._card(parent, padding=0)
        s_card.pack(fill="both", expand=True)
        list_frame = ctk.CTkScrollableFrame(s_card, fg_color="transparent",
                                           height=480)
        list_frame.pack(fill="both", expand=True, padx=4, pady=4)
        try:
            apps = StartupManager.list_startup_apps()
        except Exception as e:
            ctk.CTkLabel(list_frame, text=t("generic_error", msg=str(e)[:80]),
                        text_color=C["text_3"]).pack(pady=20)
            apps = None
        if apps is not None:
            if apps:
                for a in apps:
                    self._startup_row(list_frame, a)
            else:
                ctk.CTkLabel(list_frame, text=t("startup_none"),
                            font=("Segoe UI", 11),
                            text_color=C["text_3"]).pack(pady=24)

        # ── 이 앱이 제거한 항목 = 되돌릴 수 있는 목록 ──
        # 예전에는 제거하면 끝이었다(레지스트리 값 영구 삭제).
        ctk.CTkLabel(list_frame, text=t("startup_disabled_card"),
                    font=("Segoe UI", 12, "bold"),
                    text_color=C["text_2"], anchor="w").pack(
                    fill="x", padx=6, pady=(18, 6))
        try:
            disabled = StartupManager.list_disabled()
        except Exception:
            disabled = []
        if not disabled:
            ctk.CTkLabel(list_frame, text=t("startup_none_disabled"),
                        font=("Segoe UI", 10), text_color=C["text_3"],
                        anchor="w", justify="left", wraplength=700).pack(
                        fill="x", padx=6, pady=(0, 12))
        for e in disabled:
            self._startup_backup_row(list_frame, e)

    def _startup_backup_row(self, parent, entry):
        row = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=8)
        row.pack(fill="x", pady=4, padx=4)
        tf = ctk.CTkFrame(row, fg_color="transparent")
        tf.pack(side="left", fill="both", expand=True, padx=16, pady=12)
        ctk.CTkLabel(tf, text=str(entry.get("name", "?")),
                    font=("Segoe UI", 12, "bold"), text_color=C["text"],
                    anchor="w").pack(fill="x")
        cmd = str(entry.get("cmd", ""))
        cmd_short = cmd[:70] + ('...' if len(cmd) > 70 else '')
        meta = f"{entry.get('hive', '')} · {entry.get('ts', '')} · {cmd_short}"
        ctk.CTkLabel(tf, text=meta, font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w").pack(fill="x")
        ctk.CTkButton(row, text=t("startup_restore"), width=90, height=32,
                     fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                     text_color=C["blue"], font=("Segoe UI", 11),
                     corner_radius=6,
                     command=lambda e=entry: self._on_restore_startup(e)
                     ).pack(side="right", padx=12, pady=12)

    def _startup_row(self, parent, app):
        row = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=8)
        row.pack(fill="x", pady=4, padx=4)
        tf = ctk.CTkFrame(row, fg_color="transparent")
        tf.pack(side="left", fill="both", expand=True, padx=16, pady=12)
        ctk.CTkLabel(tf, text=app['name'], font=("Segoe UI", 12, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")
        cmd_short = app['cmd'][:80] + ('...' if len(app['cmd']) > 80 else '')
        ctk.CTkLabel(tf, text=f"{app['scope']} · {cmd_short}",
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x")
        if app['safe_to_disable']:
            ctk.CTkButton(row, text=t("apps_btn_disable"), width=80, height=32,
                         fg_color=C["btn_danger"],
                         hover_color=C["btn_danger_h"],
                         text_color=C["danger_text"], font=("Segoe UI", 11),
                         corner_radius=6,
                         command=lambda a=app: self._on_disable_startup(a)
                         ).pack(side="right", padx=12, pady=12)
        else:
            ctk.CTkLabel(row, text=t("apps_critical"),
                        font=("Segoe UI", 10, "bold"),
                        text_color=C["text_3"]).pack(side="right",
                                                    padx=16, pady=12)

    # ────────────────────────────────────────────────────────────
    #  HEALTH
    # ────────────────────────────────────────────────────────────
    def _build_health(self):
        ctk.CTkLabel(self.content, text=t("health_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        snap = self._ui_snap()
        health = (self._ui_data.get("health")
                  or HealthAnalyzer.analyze(snap, PERF_HISTORY))

        score_card = self._card(self.content, padding=24)
        score_card.pack(fill="x", pady=(0, 16))
        si = ctk.CTkFrame(score_card, fg_color="transparent")
        si.pack(fill="x", padx=24, pady=24)
        ctk.CTkLabel(si, text=str(health['overall_score']),
                    font=("Segoe UI", 56, "bold"),
                    text_color=C["blue"], anchor="w").pack(anchor="w")
        ctk.CTkLabel(si, text=t("health_overall", status=t(f"health_status_{health['status'].lower()}")),
                    font=("Segoe UI", 14),
                    text_color=C["text_2"], anchor="w").pack(anchor="w")

        comp_card = self._card(self.content, t("health_components"))
        comp_card.pack(fill="x", pady=(0, 16))
        cg = ctk.CTkFrame(comp_card, fg_color="transparent")
        cg.pack(fill="x", padx=20, pady=(0, 20))
        cg.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="c")
        for i, (label, val) in enumerate([
            ("CPU", health['cpu_score']), ("RAM", health['ram_score']),
            ("Disk", health['disk_score']), ("Uptime", health['uptime_score']),
        ]):
            cf = ctk.CTkFrame(cg, fg_color=C["panel"], corner_radius=8)
            cf.grid(row=0, column=i, padx=4, sticky="ew")
            ctk.CTkLabel(cf, text=label, font=("Segoe UI", 11),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=12, pady=(12, 0))
            ctk.CTkLabel(cf, text=f"{val}/100",
                        font=("Segoe UI", 18, "bold"),
                        text_color=C["blue"],
                        anchor="w").pack(anchor="w", padx=12, pady=(2, 12))

        if health['issues']:
            ic = self._card(self.content, t("health_issues"))
            ic.pack(fill="x", pady=(0, 16))
            ii = ctk.CTkFrame(ic, fg_color="transparent")
            ii.pack(fill="x", padx=20, pady=(0, 20))
            for sev, msg in health['issues']:
                row = ctk.CTkFrame(ii, fg_color=C["panel"], corner_radius=6)
                row.pack(fill="x", pady=4)
                color = (C["blue"] if sev == "info" else
                        C["warn_text"] if sev == "warning" else
                        C["danger_text"])
                ctk.CTkLabel(row, text="●", font=("Segoe UI", 14),
                            text_color=color).pack(side="left",
                                                  padx=(12, 8), pady=10)
                ctk.CTkLabel(row, text=msg, font=("Segoe UI", 12),
                            text_color=C["text"],
                            anchor="w").pack(side="left", fill="x",
                                            expand=True, pady=10)

        if health['recommendations']:
            rc = self._card(self.content, t("health_recs"))
            rc.pack(fill="x", pady=(0, 16))
            ri = ctk.CTkFrame(rc, fg_color="transparent")
            ri.pack(fill="x", padx=20, pady=(0, 20))
            for rec in health['recommendations']:
                row = ctk.CTkFrame(ri, fg_color="transparent")
                row.pack(fill="x", pady=4)
                ctk.CTkLabel(row, text="→",
                            font=("Segoe UI", 14, "bold"),
                            text_color=C["blue"]).pack(side="left", padx=(0, 8))
                ctk.CTkLabel(row, text=rec, font=("Segoe UI", 12),
                            text_color=C["text_2"],
                            anchor="w").pack(side="left", fill="x", expand=True)

        # ─── RAM Leak Detector card ──────────────────────────────
        self._build_leak_card(self.content)

    def _build_leak_card(self, parent):
        """Memory Leak Monitor card — shown at bottom of Health tab."""
        leak_card = self._card(parent, t("leak_card_title"))
        leak_card.pack(fill="x", pady=(0, 16))
        li = ctk.CTkFrame(leak_card, fg_color="transparent")
        li.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(li, text=t("leak_subtitle"),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x", pady=(0, 12))
        # Container — refreshed by _refresh_leak_card
        self.dynamic["sec_leak_list"] = ctk.CTkFrame(li, fg_color="transparent")
        self.dynamic["sec_leak_list"].pack(fill="x")
        self._refresh_leak_card()

    def _refresh_leak_card(self):
        """Update the leak detector card. Called periodically + on tab open."""
        cont = self.dynamic.get("sec_leak_list")
        if not cont: return
        for w in cont.winfo_children(): w.destroy()
        if not self.leak_detector or not self.leak_detector.enabled:
            ctk.CTkLabel(cont, text=t("leak_disabled"),
                        font=("Segoe UI", 11), text_color=C["text_3"],
                        anchor="w").pack(fill="x")
            return
        alerts = self.leak_detector.get_alerts()
        if not alerts:
            tracked = self.leak_detector.get_tracked_count()
            ctk.CTkLabel(cont, text=t("leak_no_alerts", n=tracked),
                        font=("Segoe UI", 11), text_color=C["blue"],
                        anchor="w").pack(fill="x")
            return
        for alert in alerts:
            row = ctk.CTkFrame(cont, fg_color=C["panel"], corner_radius=8)
            row.pack(fill="x", pady=4)
            sev = alert["severity"]
            sev_color = (C["danger_text"] if sev == "critical"
                        else C["warn_text"] if sev == "danger"
                        else C["blue"])
            sev_text = (t("leak_severity_critical") if sev == "critical"
                       else t("leak_severity_danger") if sev == "danger"
                       else t("leak_severity_warn"))
            # Severity dot
            ctk.CTkLabel(row, text="●", font=("Segoe UI", 14),
                        text_color=sev_color).pack(side="left",
                                                  padx=(12, 8), pady=10)
            # Name + growth
            tf = ctk.CTkFrame(row, fg_color="transparent")
            tf.pack(side="left", fill="x", expand=True, pady=8)
            ctk.CTkLabel(tf, text=alert["name"],
                        font=("Segoe UI", 12, "bold"),
                        text_color=C["text"], anchor="w").pack(fill="x")
            ctk.CTkLabel(tf,
                        text=t("leak_growth",
                              mb=alert["growth_mb"],
                              min=alert["duration_min"]),
                        font=("Segoe UI", 10),
                        text_color=C["text_3"], anchor="w").pack(fill="x")
            # Severity badge on right
            badge = ctk.CTkFrame(row, fg_color=sev_color, corner_radius=6)
            badge.pack(side="right", padx=(8, 12), pady=10)
            ctk.CTkLabel(badge, text=sev_text,
                        font=("Segoe UI", 10, "bold"),
                        text_color="#FFFFFF").pack(padx=8, pady=2)

    # ────────────────────────────────────────────────────────────
    #  REPORTS
    # ────────────────────────────────────────────────────────────
    def _build_reports(self):
        ctk.CTkLabel(self.content, text=t("reports_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        # ─── Session History card (top of Reports tab) ──────────
        self._build_history_card(self.content)

        # Existing export cards
        for title, desc, icon, action in [
            (t("reports_health_title"),
             t("reports_health_desc"),
             "📄", self._on_export_health),
            (t("reports_perf_title"),
             t("reports_perf_desc"),
             "📈", self._on_export_perf),
            (t("reports_startup_title"),
             t("reports_startup_desc"),
             "🚀", self._on_export_startup),
        ]:
            card = self._card(self.content, padding=20)
            card.pack(fill="x", pady=(0, 12))
            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(fill="x", padx=20, pady=20)
            ctk.CTkLabel(inner, text=f"{icon}  {title}",
                        font=("Segoe UI", 14, "bold"),
                        text_color=C["text"], anchor="w").pack(fill="x",
                                                              pady=(0, 4))
            ctk.CTkLabel(inner, text=desc, font=("Segoe UI", 11),
                        text_color=C["text_3"],
                        anchor="w").pack(fill="x", pady=(0, 12))
            self._secondary_btn(inner, t("download"), action).pack(
                side="right", anchor="e")

    # ────────────────────────────────────────────────────────────
    #  SETTINGS
    # ────────────────────────────────────────────────────────────
    def _build_settings(self):
        ctk.CTkLabel(self.content, text=t("settings_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 16))

        # ─── Language toggle (한국어 / English) ──────────────────
        lang_card = self._card(self.content, t("settings_language"))
        lang_card.pack(fill="x", pady=(0, 16))
        li = ctk.CTkFrame(lang_card, fg_color="transparent")
        li.pack(fill="x", padx=20, pady=(0, 20))
        li.grid_columnconfigure((0, 1), weight=1, uniform="lang")

        # KR button
        kr_active = (I18N.lang == "ko")
        self.dynamic["sec_lang_kr"] = ctk.CTkButton(
            li, text=f"  🇰🇷    {t('settings_lang_kr')}",
            anchor="center",
            fg_color=C["blue"] if kr_active else C["btn_sec"],
            text_color="#FFFFFF" if kr_active else C["text"],
            hover_color=C["blue_dark"] if kr_active else C["btn_sec_h"],
            font=("Segoe UI", 14, "bold" if kr_active else "normal"),
            corner_radius=10, height=56,
            border_width=0 if kr_active else 1,
            border_color=C["border"],
            command=lambda: self._on_lang_select("ko"),
        )
        self.dynamic["sec_lang_kr"].grid(row=0, column=0, padx=(0, 6),
                                        sticky="ew")

        # EN button
        en_active = (I18N.lang == "en")
        self.dynamic["sec_lang_en"] = ctk.CTkButton(
            li, text=f"  🇺🇸    {t('settings_lang_en')}",
            anchor="center",
            fg_color=C["blue"] if en_active else C["btn_sec"],
            text_color="#FFFFFF" if en_active else C["text"],
            hover_color=C["blue_dark"] if en_active else C["btn_sec_h"],
            font=("Segoe UI", 14, "bold" if en_active else "normal"),
            corner_radius=10, height=56,
            border_width=0 if en_active else 1,
            border_color=C["border"],
            command=lambda: self._on_lang_select("en"),
        )
        self.dynamic["sec_lang_en"].grid(row=0, column=1, padx=(6, 0),
                                        sticky="ew")

        # ─── Theme (라이트 / 다크 / Windows 따름) ─────────────────
        theme_card = self._card(self.content, t("settings_theme"))
        theme_card.pack(fill="x", pady=(0, 16))
        ti = ctk.CTkFrame(theme_card, fg_color="transparent")
        ti.pack(fill="x", padx=20, pady=(0, 20))
        ti.grid_columnconfigure((0, 1, 2), weight=1, uniform="theme")
        cur_theme = getattr(self, "theme", "light")
        for col, (mode, key) in enumerate(
                [("light", "theme_light"), ("dark", "theme_dark"),
                 ("system", "theme_system")]):
            act = (cur_theme == mode)
            btn = ctk.CTkButton(
                ti, text=t(key), anchor="center",
                fg_color=C["blue"] if act else C["btn_sec"],
                text_color="#FFFFFF" if act else C["text"],
                hover_color=C["blue_dark"] if act else C["btn_sec_h"],
                font=("Segoe UI", 13, "bold" if act else "normal"),
                corner_radius=10, height=46,
                border_width=0 if act else 1,
                border_color=C["border"],
                command=lambda m=mode: self._on_theme_select(m))
            btn.grid(row=0, column=col,
                    padx=(0 if col == 0 else 6, 0 if col == 2 else 6),
                    sticky="ew")
            self.dynamic[f"sec_theme_{mode}"] = btn

        # ─── 열 관리 ──────────────────────────────────────────────
        # 온도를 읽을 수 있든 없든 이 카드는 항상 보여준다. 못 읽는
        # 이유를 사용자가 확인할 수 있어야 하기 때문이다.
        th_card = self._card(self.content, t("settings_thermal_title"))
        th_card.pack(fill="x", pady=(0, 16))
        thi = ctk.CTkFrame(th_card, fg_color="transparent")
        thi.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(thi, text=t("settings_thermal_desc"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w", justify="left", wraplength=780).pack(
                        fill="x", pady=(0, 10))
        _th = getattr(self.observer, "thermal", None)
        _gov = getattr(self, "governor", None)
        _th_ok = bool(_th is not None and _th.ok)
        _rows = []
        if _th_ok:
            _c = _th.cpu_temp_c
            _rows.append((t("thermal_label"),
                          "—" if _c is None else f"{_c:.0f}°C"))
            _rows.append((t("thermal_source"), _th.source or "PDH"))
        else:
            _rows.append((t("thermal_label"), t("thermal_unavailable")))
            _why = (getattr(_th, "fail_reason", "") if _th is not None
                    else "monitor not started")
            if _why:
                _rows.append(("", _why))
        if _gov is not None:
            _pct = _gov.status_pct()
            _rows.append((t("thermal_state"),
                          t("thermal_cap_none") if _pct >= 100
                          else t("thermal_capped", pct=_pct)))
        for _lab, _val in _rows:
            _r = ctk.CTkFrame(thi, fg_color="transparent")
            _r.pack(fill="x", pady=4)
            ctk.CTkLabel(_r, text=_lab, font=("Segoe UI", 12),
                        text_color=C["text_3"], anchor="w",
                        width=140).pack(side="left")
            ctk.CTkLabel(_r, text=_val,
                        font=("Segoe UI", 12, "bold" if _lab else "normal"),
                        text_color=C["text"] if _lab else C["text_3"],
                        anchor="w", justify="left",
                        wraplength=560).pack(side="left")

        # 자동 완화 토글 — 온도를 읽을 수 있을 때만 의미가 있다.
        if _th_ok and _gov is not None:
            trow = ctk.CTkFrame(thi, fg_color=C["panel"], corner_radius=8)
            trow.pack(fill="x", pady=(12, 0))
            tin = ctk.CTkFrame(trow, fg_color="transparent")
            tin.pack(fill="x", padx=16, pady=12)
            head = ctk.CTkFrame(tin, fg_color="transparent")
            head.pack(fill="x")
            ctk.CTkLabel(head, text=t("thermal_auto_title"),
                        font=("Segoe UI", 12, "bold"),
                        text_color=C["text"], anchor="w").pack(side="left")
            sw = ctk.CTkSwitch(head, text="", command=self._on_thermal_toggle,
                              progress_color=C["blue"], button_color=C["blue"],
                              button_hover_color=C["blue_dark"])
            if _gov.enabled: sw.select()
            sw.pack(side="right")
            self.dynamic["sec_thermal_sw"] = sw
            ctk.CTkLabel(tin, text=t("thermal_auto_desc"),
                        font=("Segoe UI", 10), text_color=C["text_3"],
                        anchor="w", justify="left", wraplength=740).pack(
                            fill="x", pady=(2, 8))
            # 기준 온도 슬라이더
            srow = ctk.CTkFrame(tin, fg_color="transparent")
            srow.pack(fill="x")
            _cur = int(thermal_threshold())
            _auto = not (60 <= int(SETTINGS.get("thermal_threshold_c", 0) or 0) <= 99)
            self.dynamic["sec_thermal_thr"] = ctk.CTkLabel(
                srow, text="%s  %d°C%s" % (t("thermal_threshold_lbl"), _cur,
                                           "  (%s)" % t("thermal_auto_c")
                                           if _auto else ""),
                font=("Segoe UI", 11), text_color=C["text_2"], anchor="w")
            self.dynamic["sec_thermal_thr"].pack(fill="x", pady=(0, 4))
            sl = ctk.CTkSlider(srow, from_=70, to=99, number_of_steps=29,
                              command=self._on_thermal_threshold,
                              progress_color=C["blue"], button_color=C["blue"],
                              button_hover_color=C["blue_dark"])
            sl.set(_cur)
            sl.pack(fill="x")
            self.dynamic["sec_thermal_slider"] = sl
            if not _gov.probe() and _gov.fail_reason:
                ctk.CTkLabel(tin, text=t("thermal_cap_blocked"),
                            font=("Segoe UI", 10),
                            text_color=C["warn_text"], anchor="w").pack(
                                fill="x", pady=(8, 0))


        # ─── About card ──────────────────────────────────────────
        info_card = self._card(self.content, t("settings_about"))
        info_card.pack(fill="x", pady=(0, 16))
        ii = ctk.CTkFrame(info_card, fg_color="transparent")
        ii.pack(fill="x", padx=20, pady=(0, 20))
        for label, value in [
            (t("settings_version"), APP_VERSION),
            (t("settings_windows"), f"{WIN_MAJOR}.{WIN_MINOR} (Build {WIN_BUILD})"),
            (t("settings_mode"), "Win11 22H2+" if IS_WIN11_22H2 else
                    "Win11" if IS_WIN11 else "Win10"),
            (t("settings_hybrid"), t("settings_yes") if IS_HYBRID
                                  else t("settings_no")),
            (t("settings_logical"), str(psutil.cpu_count(logical=True) or "?")),
            (t("settings_physical"), str(psutil.cpu_count(logical=False) or "?")),
            (t("settings_admin"), t("settings_yes") if is_admin()
                                  else t("settings_no")),
            # ★우리가 Tk 스레드를 얼마나 붙잡는지 숨기지 않고 보여준다★
            # 이 숫자가 커지면 창이 버벅인다는 뜻이고, 그건 최적화
            # 도구로서 제일 먼저 고쳐야 할 결함이다.
            (t("settings_ui_frame"), "%.1f ms (max %.1f ms)"
             % (getattr(self, "_ui_frame_ms", 0.0),
                getattr(self, "_ui_frame_ms_max", 0.0))),
        ]:
            row = ctk.CTkFrame(ii, fg_color="transparent")
            row.pack(fill="x", pady=4)
            ctk.CTkLabel(row, text=label, font=("Segoe UI", 12),
                        text_color=C["text_3"], anchor="w",
                        width=140).pack(side="left")
            ctk.CTkLabel(row, text=value, font=("Segoe UI", 12, "bold"),
                        text_color=C["text"], anchor="w").pack(side="left")

        if UPDATE_ENABLED:
            upd_row = ctk.CTkFrame(ii, fg_color="transparent")
            upd_row.pack(fill="x", pady=(12, 0))
            self._secondary_btn(
                upd_row, t("settings_check_update"), self._manual_check_update,
            ).pack(side="right")

        # ─── Tiny AI brag (one line) ─────────────────────────────
        ai_brag = ctk.CTkFrame(ii, fg_color=C["blue_subtle"],
                              corner_radius=6)
        ai_brag.pack(fill="x", pady=(12, 0))
        ctk.CTkLabel(ai_brag, text=t("settings_ai_brag"),
                    font=("Segoe UI", 10, "bold"),
                    text_color=C["blue"], anchor="w",
                    justify="left", wraplength=780).pack(
                        fill="x", padx=12, pady=10)

        # ─── Error log path (for support / MS Store crash tracking) ─
        log_row = ctk.CTkFrame(ii, fg_color="transparent")
        log_row.pack(fill="x", pady=(8, 0))
        ctk.CTkLabel(log_row, text=t("settings_log_label"),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w", width=140).pack(side="left")
        log_path_str = ERROR_LOG.get_log_path()
        # Shorten if too long
        if len(log_path_str) > 60:
            log_path_str = "..." + log_path_str[-57:]
        ctk.CTkLabel(log_row, text=log_path_str,
                    font=("Consolas", 9), text_color=C["text_2"],
                    anchor="w").pack(side="left")

        # ─── Auto Optimizer ──────────────────────────────────────
        opt_card = self._card(self.content, t("settings_auto"))
        opt_card.pack(fill="x", pady=(0, 16))
        oi = ctk.CTkFrame(opt_card, fg_color="transparent")
        oi.pack(fill="x", padx=20, pady=(0, 20))

        # Toggle row
        opt_row = ctk.CTkFrame(oi, fg_color=C["panel"], corner_radius=8)
        opt_row.pack(fill="x")
        tf = ctk.CTkFrame(opt_row, fg_color="transparent")
        tf.pack(side="left", fill="both", expand=True, padx=16, pady=12)
        ctk.CTkLabel(tf, text=t("settings_auto_loop"),
                    font=("Segoe UI", 12, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")
        ctk.CTkLabel(tf, text=t("settings_auto_desc"),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x")
        sw = ctk.CTkSwitch(opt_row, text="", command=self._on_auto_toggle,
                          progress_color=C["blue"], button_color=C["blue"],
                          button_hover_color=C["blue_dark"])
        sw.select()
        sw.pack(side="right", padx=16, pady=12)
        self.dynamic["sec_auto_sw"] = sw

        # "What it does" expandable detail list
        ctk.CTkLabel(oi, text=t("settings_auto_what"),
                    font=("Segoe UI", 11, "bold"),
                    text_color=C["text"], anchor="w").pack(
                        fill="x", pady=(16, 8))
        for key in ["auto_what_1", "auto_what_2", "auto_what_3",
                    "auto_what_4", "auto_what_5", "auto_what_6"]:
            r = ctk.CTkFrame(oi, fg_color="transparent")
            r.pack(fill="x", pady=2)
            ctk.CTkLabel(r, text=t(key), font=("Segoe UI", 11),
                        text_color=C["text_2"],
                        anchor="w").pack(fill="x", padx=4)

        # Safety note
        safe_box = ctk.CTkFrame(oi, fg_color=C["blue_subtle"],
                               corner_radius=6)
        safe_box.pack(fill="x", pady=(12, 0))
        ctk.CTkLabel(safe_box, text=t("auto_what_safe"),
                    font=("Segoe UI", 10),
                    text_color=C["text_2"],
                    anchor="w", justify="left",
                    wraplength=780).pack(fill="x", padx=12, pady=10)

        # ─── Smart Automation (game/battery/scheduler) ──────────
        sa_card = self._card(self.content, t("auto_section"))
        sa_card.pack(fill="x", pady=(0, 16))
        sai = ctk.CTkFrame(sa_card, fg_color="transparent")
        sai.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(sai, text=t("auto_section_desc"),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x", pady=(0, 12))

        # Game Auto-Boost toggle
        self._auto_toggle_row(sai, t("auto_game_title"),
                             t("auto_game_desc"),
                             "game_detect", self._on_game_detect_toggle)

        # Battery Saver toggle
        self._auto_toggle_row(sai, t("auto_battery_title"),
                             t("auto_battery_desc"),
                             "battery_saver", self._on_battery_saver_toggle)

        # Scheduler section (separate — has its own controls)
        sched_row = ctk.CTkFrame(sai, fg_color=C["panel"], corner_radius=8)
        sched_row.pack(fill="x", pady=4)
        sched_inner = ctk.CTkFrame(sched_row, fg_color="transparent")
        sched_inner.pack(fill="x", padx=16, pady=12)

        head = ctk.CTkFrame(sched_inner, fg_color="transparent")
        head.pack(fill="x")
        ctk.CTkLabel(head, text=t("auto_sched_title"),
                    font=("Segoe UI", 12, "bold"),
                    text_color=C["text"], anchor="w").pack(side="left")
        # Master switch for scheduler
        sw = ctk.CTkSwitch(head, text="", command=self._on_scheduler_toggle,
                          progress_color=C["blue"], button_color=C["blue"],
                          button_hover_color=C["blue_dark"])
        if self.scheduler and self.scheduler.enabled: sw.select()
        sw.pack(side="right")
        self.dynamic["sec_sched_sw"] = sw

        ctk.CTkLabel(sched_inner, text=t("auto_sched_desc"),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w").pack(fill="x", pady=(2, 8))

        # Schedule list container
        self.dynamic["sec_sched_list"] = ctk.CTkFrame(
            sched_inner, fg_color="transparent")
        self.dynamic["sec_sched_list"].pack(fill="x")
        self._refresh_schedule_list()

        # Add schedule presets row
        add_row = ctk.CTkFrame(sched_inner, fg_color="transparent")
        add_row.pack(fill="x", pady=(8, 0))
        for hr, mn, task, label in [
            (4, 0, "trim", "💾 04:00"),
            (12, 0, "hard_5min", "🔥 12:00"),
        ]:
            ctk.CTkButton(
                add_row, text=label, width=80, height=28,
                fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                text_color=C["blue"], font=("Segoe UI", 10),
                corner_radius=6,
                command=lambda h=hr, m=mn, t_=task:
                    self._on_add_schedule(h, m, t_),
            ).pack(side="left", padx=(0, 6))

        # ─── Safety / Rollback ───────────────────────────────────
        rb_card = self._card(self.content, t("settings_safety"))
        rb_card.pack(fill="x", pady=(0, 16))
        rbi = ctk.CTkFrame(rb_card, fg_color="transparent")
        rbi.pack(fill="x", padx=20, pady=(0, 20))
        ctk.CTkLabel(rbi, text=t("settings_rollback_desc"),
                    font=("Segoe UI", 11), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(0, 12))
        self._secondary_btn(rbi, t("settings_rollback"),
                           self._on_rollback).pack(side="left")

        # ─── Honest disclosure ───────────────────────────────────
        disc_card = ctk.CTkFrame(self.content, fg_color=C["panel"],
                                corner_radius=8)
        disc_card.pack(fill="x", pady=(0, 16))
        ctk.CTkLabel(
            disc_card,
            text=t("settings_disclosure"),
            font=("Segoe UI", 10), text_color=C["text_2"],
            anchor="w", justify="left", wraplength=820,
        ).pack(fill="x", padx=16, pady=12)

        # ─── License & Credits ───────────────────────────────────
        license_card = self._card(self.content, t("card_license_credits"))
        license_card.pack(fill="x", pady=(0, 32))
        lic_inner = ctk.CTkFrame(license_card, fg_color="transparent")
        lic_inner.pack(fill="x", padx=20, pady=(0, 20))

        # GPL 제3조 5항(d) '적절한 법적 고지' 표시면.
        # 저작권 + 무보증 + 재배포 조건 + 라이선스 전문/소스 위치.
        ctk.CTkLabel(lic_inner,
                    text=f'{t("license_title")} — {LICENSE_ID}',
                    font=("Segoe UI", 11, "bold"), text_color=C["blue"],
                    anchor="w").pack(fill="x", pady=(0, 8))

        ctk.CTkLabel(lic_inner,
                    text=t("license_body", copyright=COPYRIGHT_LINE),
                    font=("Segoe UI", 10), text_color=C["text_2"],
                    anchor="w", justify="left",
                    wraplength=760).pack(fill="x", pady=(0, 12))

        ctk.CTkLabel(lic_inner,
                    text=t("license_meta", version=APP_VERSION),
                    font=("Segoe UI", 10), text_color=C["text_3"],
                    anchor="w", justify="left",
                    wraplength=760).pack(fill="x", pady=(0, 12))

        def _open_url(url):
            try:
                import webbrowser
                webbrowser.open(url)
            except Exception as _dx:
                DIAG.q("OmegaGUI._open_url#0", _dx)

        lic_btns = ctk.CTkFrame(lic_inner, fg_color="transparent")
        lic_btns.pack(fill="x", pady=(0, 12))
        self._secondary_btn(lic_btns, t("license_view"),
                           lambda: _open_url(LICENSE_URL)).pack(
                           side="left", padx=(0, 8))
        self._secondary_btn(lic_btns, t("license_source"),
                           lambda: _open_url(SOURCE_URL)).pack(
                           side="left")

        # Copy system info button for support
        def copy_system_info():
            import platform
            info = (f"{APP_NAME} v{APP_VERSION}\n"
                   f"Windows {WIN_MAJOR}.{WIN_MINOR} Build {WIN_BUILD}\n"
                   f"Admin: {is_admin()}\n"
                   f"CPU: {psutil.cpu_count(logical=True)} logical / {psutil.cpu_count(logical=False)} physical\n"
                   f"RAM: {psutil.virtual_memory().total // (1024**3)} GB")
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append(info)
                self._toast(t("toast_sysinfo_copied"))
            except Exception as _dx:
                DIAG.q("OmegaGUI.copy_system_info#0", _dx)
        
        self._secondary_btn(lic_inner, t("ui_copy_sysinfo"),
                           copy_system_info).pack(side="left")

        # ★PATCH27★ 삼킨 예외 통계. 화면에 안 나오는 실패는 존재하지
        # 않는 것과 같다 — 최소한 복사해서 보낼 수는 있어야 한다.
        def copy_diag_info():
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append(DIAG.text() or "-")
                self._toast(t("ui_diag_copied"))
            except Exception as _dx:
                DIAG.q("OmegaGUI.copy_diag_info#0", _dx)

        self._secondary_btn(lic_inner, t("ui_copy_diag"),
                           copy_diag_info).pack(side="left", padx=(8, 0))

    def _on_lang_select(self, lang):
        if lang == I18N.lang: return
        I18N.set_lang(lang)
        SETTINGS.set("lang", lang)   # ★다음 실행에도 유지★
        self._toast(t("toast_lang_changed"))

    # ────────────────────────────────────────────────────────────
    #  확인 다이얼로그 — 되돌릴 수 없는 액션의 공통 관문
    # ────────────────────────────────────────────────────────────
    def _confirm(self, title, message, confirm_text=None, danger=True):
        """모달 확인 창. 진행하면 True.

        ★프로세스 강제 종료·시작프로그램 제거·파일 영구 삭제는
          반드시 이 함수를 거친다.★ 예전에는 버튼 한 번에 즉시
          실행되고 결과는 2.5초 토스트로만 알렸다.
        """
        W, H = 480, 240
        dlg = ctk.CTkToplevel(self.root)
        dlg.title(f"{APP_NAME} — {title}")
        dlg.geometry(f"{W}x{H}")
        dlg.resizable(False, False)
        dlg.configure(fg_color=C["bg"])
        dlg.transient(self.root)
        apply_window_icon(dlg)
        state = {"ok": False}

        ctk.CTkLabel(dlg, text=title,
                    font=("Segoe UI", 15, "bold"),
                    text_color=C["text"], anchor="w",
                    justify="left", wraplength=W - 40).pack(
                    fill="x", padx=20, pady=(20, 8))
        ctk.CTkLabel(dlg, text=message,
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w", justify="left",
                    wraplength=W - 40).pack(fill="x", padx=20,
                                            pady=(0, 16))

        def _close(ok):
            state["ok"] = ok
            try: dlg.grab_release()
            except Exception as _dx: DIAG.q("OmegaGUI._close#0", _dx)
            try: dlg.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI._close#1", _dx)

        row = ctk.CTkFrame(dlg, fg_color="transparent")
        row.pack(side="bottom", fill="x", padx=20, pady=(0, 18))
        ctk.CTkButton(row, text=confirm_text or t("ui_confirm"),
                     command=lambda: _close(True),
                     fg_color=C["btn_danger"] if danger else C["blue"],
                     hover_color=(C["btn_danger_h"] if danger
                                  else C["blue_dark"]),
                     text_color=C["danger_text"] if danger else "#FFFFFF",
                     font=("Segoe UI", 12, "bold"),
                     height=38, corner_radius=8).pack(side="right")
        self._secondary_btn(row, t("cancel"),
                           lambda: _close(False), height=38).pack(
                           side="right", padx=(0, 8))

        dlg.protocol("WM_DELETE_WINDOW", lambda: _close(False))
        dlg.bind("<Escape>", lambda e: _close(False))
        try:
            dlg.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - W) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - H) // 2
            dlg.geometry(f"{W}x{H}+{max(0, x)}+{max(0, y)}")
        except Exception as _dx:
            DIAG.q("OmegaGUI._confirm#0", _dx)
        try: dlg.grab_set()
        except Exception as _dx: DIAG.q("OmegaGUI._confirm#1", _dx)
        try: self.root.wait_window(dlg)
        except Exception as _dx: DIAG.q("OmegaGUI._confirm#2", _dx)
        return state["ok"]

    # ────────────────────────────────────────────────────────────
    #  테마
    # ────────────────────────────────────────────────────────────
    def _on_theme_select(self, mode):
        if mode == getattr(self, "theme", "light"):
            return
        self.theme = mode
        SETTINGS.set("theme", mode)
        apply_theme(mode)
        self._rebuild_ui()

    def _rebuild_ui(self):
        """팔레트가 바뀌면 이미 만들어진 위젯 색은 따라오지 않는다.
        사이드바·본문을 통째로 다시 만든다(언어 전환보다 강한 갱신).
        """
        cur = self.active_section or "home"
        try: self._invalidate_section_cache()
        except Exception as _dx: DIAG.q("OmegaGUI._rebuild_ui#0", _dx)
        if self._toast_widget is not None:
            try: self._toast_widget.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI._rebuild_ui#1", _dx)
            self._toast_widget = None
        for attr in ("sidebar", "main"):
            w = getattr(self, attr, None)
            if w is not None:
                try: w.destroy()
                except Exception as _dx: DIAG.q("OmegaGUI._rebuild_ui#2", _dx)
                setattr(self, attr, None)
        self.dynamic = {}
        self.nav_buttons = {}
        self._proc_row_pool = []
        self._prog_row_pool = []
        self._prog_dirty = True
        self._friendly_label_cache = {}
        self._running_totals_cache = {}
        self._last_profile_seen = None
        if hasattr(self, "_lv"): self._lv = {}
        self.active_section = None
        self.root.configure(fg_color=C["bg"])
        self._build_skeleton()
        self._show_section(cur)

    # ────────────────────────────────────────────────────────────
    #  프로세스 표 — 검색 / 정렬
    # ────────────────────────────────────────────────────────────
    def _on_proc_search(self, text):
        q = (text or "").strip().lower()
        if q == self._proc_query:
            return
        self._proc_query = q
        self._update_process_rows()

    def _on_proc_sort(self, key):
        if key == self._proc_sort:
            self._proc_desc = not self._proc_desc
        else:
            self._proc_sort = key
            self._proc_desc = (key != "name")
        self._update_sort_headers()
        self._update_process_rows()

    def _update_sort_headers(self):
        arrow = "  ▼" if self._proc_desc else "  ▲"
        for key, (btn, label) in (self._proc_hdr or {}).items():
            try:
                btn.configure(
                    text=label + (arrow if key == self._proc_sort else ""),
                    text_color=(C["blue"] if key == self._proc_sort
                                else C["text_2"]))
            except Exception as _dx:
                DIAG.q("OmegaGUI._update_sort_headers#0", _dx)

    # ────────────────────────────────────────────────────────────
    #  Smart Automation helpers + handlers
    # ────────────────────────────────────────────────────────────
    def _auto_toggle_row(self, parent, title, desc, mgr_attr, callback):
        """Build a generic toggle row for an automation manager."""
        row = ctk.CTkFrame(parent, fg_color=C["panel"], corner_radius=8)
        row.pack(fill="x", pady=4)
        tf = ctk.CTkFrame(row, fg_color="transparent")
        tf.pack(side="left", fill="both", expand=True, padx=16, pady=12)
        ctk.CTkLabel(tf, text=title, font=("Segoe UI", 12, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")
        ctk.CTkLabel(tf, text=desc, font=("Segoe UI", 10),
                    text_color=C["text_3"], anchor="w",
                    justify="left", wraplength=620).pack(fill="x")
        sw = ctk.CTkSwitch(row, text="", command=callback,
                          progress_color=C["blue"], button_color=C["blue"],
                          button_hover_color=C["blue_dark"])
        mgr = getattr(self, mgr_attr, None)
        if mgr and mgr.enabled: sw.select()
        sw.pack(side="right", padx=16, pady=12)
        self.dynamic[f"sec_{mgr_attr}_sw"] = sw

    def _on_game_detect_toggle(self):
        if not self.game_detect: return
        sw = self.dynamic.get("sec_game_detect_sw")
        if not sw: return
        on = bool(sw.get())
        SETTINGS.set("auto_game_detect", on)   # ★재시작해도 유지★
        if on:
            self.game_detect.start()
            self._toast(t("auto_game_title"))
        else:
            self.game_detect.stop()

    def _on_thermal_toggle(self):
        """온도 자동 완화 켜기/끄기. 끄면 즉시 원래 속도로 되돌린다."""
        gov = getattr(self, "governor", None)
        sw = self.dynamic.get("sec_thermal_sw")
        if not gov or not sw: return
        on = bool(sw.get())
        SETTINGS.set("thermal_auto_mitigate", on)
        if on:
            if not gov.start():
                sw.deselect()
                SETTINGS.set("thermal_auto_mitigate", False)
                self._toast(t("thermal_cap_blocked"))
                return
            self._toast(t("thermal_auto_title"))
        else:
            gov.stop(restore=True)
            self._toast(t("thermal_cap_restored"))

    def _on_thermal_threshold(self, value):
        """슬라이더 — 개입 기준 온도. 값이 바뀔 때마다 저장한다."""
        try:
            v = int(round(float(value)))
        except Exception:
            return
        SETTINGS.set("thermal_threshold_c", v)
        lbl = self.dynamic.get("sec_thermal_thr")
        if lbl is not None:
            try:
                lbl.configure(text="%s  %d°C" % (t("thermal_threshold_lbl"), v))
            except Exception as _dx: DIAG.q("OmegaGUI._on_thermal_threshold#0", _dx)


    def _on_battery_saver_toggle(self):
        if not self.battery_saver: return
        sw = self.dynamic.get("sec_battery_saver_sw")
        if not sw: return
        on = bool(sw.get())
        SETTINGS.set("auto_battery_saver", on)
        if on:
            self.battery_saver.start()
            self._toast(t("auto_battery_title"))
        else:
            self.battery_saver.stop()

    def _on_scheduler_toggle(self):
        if not self.scheduler: return
        sw = self.dynamic.get("sec_sched_sw")
        if not sw: return
        on = bool(sw.get())
        SETTINGS.set("auto_scheduler", on)
        if on:
            self.scheduler.start()
            self._toast(t("auto_sched_title"))
        else:
            self.scheduler.stop()

    def _on_add_schedule(self, hour, minute, task):
        if not self.scheduler: return
        # Avoid duplicates
        for s in self.scheduler.schedule:
            if (s["hour"] == hour and s["minute"] == minute
                and s["task"] == task):
                return
        self.scheduler.add_schedule(hour, minute, task)
        self._refresh_schedule_list()
        self._toast(t("auto_sched_at",
                     time=f"{hour:02d}:{minute:02d}"))

    def _on_remove_schedule(self, idx):
        if not self.scheduler: return
        self.scheduler.remove_schedule(idx)
        self._refresh_schedule_list()

    def _refresh_schedule_list(self):
        cont = self.dynamic.get("sec_sched_list")
        if not cont: return
        for w in cont.winfo_children(): w.destroy()
        if not self.scheduler or not self.scheduler.schedule:
            ctk.CTkLabel(cont, text=t("auto_sched_none"),
                        font=("Segoe UI", 10), text_color=C["text_3"],
                        anchor="w").pack(fill="x", pady=2)
            return
        task_label = {
            "cleanup":   t("auto_sched_task_cleanup"),
            "trim":      t("auto_sched_task_trim"),
            "hard_5min": t("auto_sched_task_hard"),
        }
        for idx, s in enumerate(self.scheduler.schedule):
            row = ctk.CTkFrame(cont, fg_color="transparent")
            row.pack(fill="x", pady=2)
            time_str = f"{s['hour']:02d}:{s['minute']:02d}"
            ctk.CTkLabel(row,
                        text=f"  {t('auto_sched_at', time=time_str)} — "
                             f"{task_label.get(s['task'], s['task'])}",
                        font=("Segoe UI", 11), text_color=C["text"],
                        anchor="w").pack(side="left", fill="x", expand=True)
            ctk.CTkButton(row, text=t("auto_sched_remove"),
                         width=64, height=24,
                         fg_color=C["btn_danger"],
                         hover_color=C["btn_danger_h"],
                         text_color=C["danger_text"],
                         font=("Segoe UI", 10), corner_radius=6,
                         command=lambda i=idx: self._on_remove_schedule(i)
                         ).pack(side="right")

    # ────────────────────────────────────────────────────────────
    #  EVENT HANDLERS
    # ────────────────────────────────────────────────────────────
    def _set_profile(self, prof):
        self.policy.set_profile(prof)
        for p, btn in self.dynamic.get("sec_prof_btns", {}).items():
            is_active = (p == prof)
            btn.configure(
                fg_color=C["blue"] if is_active else C["btn_sec"],
                text_color="#FFFFFF" if is_active else C["blue"],
                hover_color=C["blue_dark"] if is_active else C["btn_sec_h"],
                font=("Segoe UI", 12, "bold" if is_active else "normal"),
                border_width=0 if is_active else 1,
            )
        self._toast(t("toast_profile", prof=prof))

    def _on_optimize_now(self):
        threading.Thread(target=self._do_optimize_now, daemon=True).start()
        self._toast(t("optimizing"))

    def _do_optimize_now(self):
        snap = self.observer.snapshot(force=True)
        fg_pid = snap.get("fg_pid")
        results = []
        for action in ["thread_burst", "io_priority", "mmcss"]:
            r = self.executor.execute(action, fg_pid, snap.get("fg_type", "general"))
            results.append(r)
        self.root.after(0, lambda: self._toast(t("toast_optimized")))

    def _on_timer_toggle(self):
        sw = self.dynamic.get("sec_timer_sw")
        if sw:
            self.policy.timer_burst_enabled = bool(sw.get())

    def _on_affinity_toggle(self):
        sw = self.dynamic.get("sec_affinity_sw")
        if sw:
            self.policy.affinity_hint_enabled = bool(sw.get())

    def _on_auto_toggle(self):
        sw = self.dynamic.get("sec_auto_sw")
        if sw:
            if sw.get(): self.optimizer.start()
            else: self.optimizer.stop()

    def _on_rollback(self):
        n = self.guard.rollback_all()
        self._toast(t("toast_rolled_back", n=n))

    def _on_proc_boost(self, pid):
        ok, msg = ProcessManager.boost(pid)
        self._toast(("✓ " if ok else "× ") + msg)

    def _on_proc_throttle(self, pid):
        ok, msg = ProcessManager.throttle(pid)
        self._toast(("✓ " if ok else "× ") + msg)

    def _on_proc_kill(self, pid):
        # ★확인 없이 즉시 kill 하던 것을 확인창 뒤로 옮겼다.★
        name = "?"
        try:
            name = psutil.Process(pid).name()
        except Exception as _dx:
            DIAG.q("OmegaGUI._on_proc_kill#0", _dx)
        if not self._confirm(t("confirm_kill_title"),
                             t("confirm_kill_msg", name=name, pid=pid),
                             confirm_text=t("apps_btn_end")):
            return
        ok, msg = ProcessManager.kill(pid)
        self._toast(("✓ " if ok else "× ") + msg)
        if ok: self.root.after(300, self._refresh_app_subtab)

    def _on_disable_startup(self, app):
        if not self._confirm(t("confirm_startup_title"),
                             t("confirm_startup_msg", name=app["name"]),
                             confirm_text=t("apps_btn_disable")):
            return
        ok = StartupManager.disable(app["hive"], app["path"], app["name"])
        if ok:
            self._toast(t("toast_disabled", name=app["name"]))
            self.root.after(300, self._refresh_app_subtab)
        else:
            self._toast(t("toast_failed", name=app["name"]))

    def _on_restore_startup(self, entry):
        """백업해둔 시작프로그램 항목을 레지스트리에 되돌린다."""
        ok = StartupManager.restore(entry)
        name = entry.get("name", "?")
        self._toast(t("toast_restored", name=name) if ok
                    else t("toast_restore_failed", name=name))
        if ok: self.root.after(300, self._refresh_app_subtab)

    def _refresh_app_subtab(self):
        # ★GUI 최적화★ 프로세스 탭은 전체 재생성 대신 행 내용만 갱신
        # ★수정★ 예전엔 행 풀이 비어 있으면 전체를 다시 만들었는데,
        #   검색 결과가 0건이면 풀이 비어 있어서 갱신 때마다 표가
        #   통째로 재생성되고 검색창의 입력 포커스가 날아갔다.
        if (self.app_subtab == "processes"
                and self._widget_alive(self.dynamic.get("sec_proc_list"))):
            self._update_process_rows(force=True)
            return
        self._render_app_subtab()

    def _on_scan_temp(self):
        self._toast(t("scanning"))
        threading.Thread(target=self._do_scan, daemon=True).start()

    def _do_scan(self):
        try:
            results = CleanupEngine.scan_temp_files()
            rb_size = CleanupEngine.get_recycle_bin_size()
            self.root.after(0, lambda: self._show_scan_results(results, rb_size))
        except Exception as e:
            # ★수정★ except 블록이 끝나면 파이썬이 e 를 삭제한다.
            # after() 로 나중에 실행되는 lambda 안에서 e 를 참조하면
            # NameError 가 나서 토스트가 아예 안 뜬다. 기본인자로 캡처.
            self.root.after(0, lambda err=e: self._toast(
                t("toast_scan_error", msg=str(err)[:80])))

    def _show_scan_results(self, results, rb_size):
        cont = self.dynamic.get("sec_scan_results")
        if not cont: return
        for w in cont.winfo_children(): w.destroy()
        total_size = sum(r["size"] for r in results.values()) + rb_size
        total_files = sum(r["count"] for r in results.values())
        ctk.CTkLabel(cont,
                    text=t("storage_found", size=format_bytes(total_size),
                           count=f"{total_files:,}"),
                    font=("Segoe UI", 14, "bold"),
                    text_color=C["blue"], anchor="w").pack(fill="x", pady=(8, 12))
        for label, info in results.items():
            row = ctk.CTkFrame(cont, fg_color=C["panel"], corner_radius=6)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=label, font=("Segoe UI", 11, "bold"),
                        text_color=C["text"], anchor="w",
                        width=160).pack(side="left", padx=12, pady=8)
            ctk.CTkLabel(row, text=t("impact_files", count=f"{info['count']:,}"),
                        font=("Segoe UI", 11), text_color=C["text_2"],
                        anchor="w", width=120).pack(side="left", padx=8, pady=8)
            ctk.CTkLabel(row, text=format_bytes(info["size"]),
                        font=("Segoe UI", 11, "bold"), text_color=C["blue"],
                        anchor="e").pack(side="right", padx=12, pady=8)
        if rb_size > 0:
            row = ctk.CTkFrame(cont, fg_color=C["panel"], corner_radius=6)
            row.pack(fill="x", pady=2)
            ctk.CTkLabel(row, text=t("storage_recycle_bin"),
                        font=("Segoe UI", 11, "bold"),
                        text_color=C["text"], anchor="w",
                        width=160).pack(side="left", padx=12, pady=8)
            ctk.CTkLabel(row, text=format_bytes(rb_size),
                        font=("Segoe UI", 11, "bold"), text_color=C["blue"],
                        anchor="e").pack(side="right", padx=12, pady=8)
        self._primary_btn(cont,
                         f"  🧹  Clean Up ({format_bytes(total_size)})  ",
                         self._on_clean_temp, height=44).pack(fill="x", pady=(16, 0))

    def _on_clean_temp(self):
        # ★영구 삭제(휴지통 경유 안 함)라 확인을 받는다.★
        if not self._confirm(t("confirm_clean_title"),
                             t("confirm_clean_msg")):
            return
        self._toast(t("cleaning"))
        threading.Thread(target=self._do_clean, daemon=True).start()

    def _do_clean(self):
        try:
            r = CleanupEngine.clean_temp()
            # ★수정★ 영문 하드코딩이라 한국어 모드에서도 영어로 떴다.
            self.root.after(0, lambda res=r: self._toast(
                "✓ " + t("toast_cleaned",
                         count=f"{res['cleaned']:,}",
                         size=format_bytes(res["freed"]))))
            self.root.after(500, self._on_scan_temp)
        except Exception as e:
            # ★수정★ 위와 같은 late-binding NameError
            self.root.after(0, lambda err=e: self._toast(
                t("toast_clean_error", msg=str(err)[:80])))

    def _on_empty_recycle(self):
        # ★PATCH25_RELEASE_GATE★ 이 앱에서 유일하게 되돌릴 수 없는 동작이다.
        # 확인 창 자체는 이미 있었지만 "휴지통을 비울까요?" 만 물었다.
        # 사용자는 자기 휴지통에 무엇이 얼마나 들었는지 모르는 채로
        # 승낙하게 된다. 개수와 용량을 문장에 박아 넣는다.
        size, count = CleanupEngine.get_recycle_bin_info()
        if count <= 0 and size <= 0:
            # 비어 있으면 파괴적 API 를 아예 호출하지 않는다.
            self._toast(t("recycle_already_empty"))
            return
        if not self._confirm(t("confirm_recycle_title"),
                             t("confirm_recycle_msg",
                               count=f"{count:,}",
                               size=format_bytes(size))):
            return
        msg = CleanupEngine.empty_recycle_bin()
        self._toast(f"✓ {msg}")

    def _on_export_health(self):
        ai_summary = self.ai.session_summary()
        html = ReportGenerator.health_report(self.observer, PERF_HISTORY,
                                            ai_summary)
        save_and_open(
            f"OMEGA_X_Health_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
            html)
        self._toast(t("toast_health_saved"))

    def _on_export_perf(self):
        csv = ReportGenerator.perf_csv(PERF_HISTORY)
        save_and_open(
            f"OMEGA_X_Perf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            csv)
        self._toast(t("toast_perf_saved"))

    def _on_export_startup(self):
        apps = StartupManager.list_startup_apps()
        html = ReportGenerator.startup_report(apps)
        save_and_open(
            f"OMEGA_X_Startup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
            html)
        self._toast(t("toast_startup_saved"))

    # ────────────────────────────────────────────────────────────
    #  Session History card (Reports tab)
    # ────────────────────────────────────────────────────────────
    def _build_history_card(self, parent):
        card = self._card(parent, t("history_title"))
        card.pack(fill="x", pady=(0, 16))
        hi = ctk.CTkFrame(card, fg_color="transparent")
        hi.pack(fill="x", padx=20, pady=(0, 20))

        if not self.session_history:
            ctk.CTkLabel(hi, text=t("history_none"),
                        font=("Segoe UI", 11), text_color=C["text_3"],
                        anchor="w").pack(fill="x")
            return

        # 30-day summary row
        summary = self.session_history.summary(days=30)
        ctk.CTkLabel(hi, text=t("history_summary"),
                    font=("Segoe UI", 11, "bold"),
                    text_color=C["text"], anchor="w").pack(
                        fill="x", pady=(0, 8))

        sum_row = ctk.CTkFrame(hi, fg_color="transparent")
        sum_row.pack(fill="x", pady=(0, 16))
        sum_row.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="hs")
        for i, (label, value) in enumerate([
            (t("history_total_ram"),    f"{summary['total_ram_gb']} GB"),
            (t("history_total_cycles"), f"{summary['total_cycles']:,}"),
            (t("history_avg_pis"),      str(summary['avg_pis'])),
            (t("history_sessions"),     str(summary['session_count'])),
        ]):
            mf = ctk.CTkFrame(sum_row, fg_color=C["panel"], corner_radius=8)
            mf.grid(row=0, column=i, padx=4, sticky="ew")
            ctk.CTkLabel(mf, text=label, font=("Segoe UI", 9),
                        text_color=C["text_3"],
                        anchor="w").pack(anchor="w", padx=12, pady=(10, 0))
            ctk.CTkLabel(mf, text=value, font=("Segoe UI", 18, "bold"),
                        text_color=C["blue"],
                        anchor="w").pack(anchor="w", padx=12, pady=(0, 10))

        # Recent sessions list (max 5)
        sessions = self.session_history.load(days=30)[:5]
        if sessions:
            ctk.CTkLabel(hi, text=t("history_recent"),
                        font=("Segoe UI", 11, "bold"),
                        text_color=C["text"], anchor="w").pack(
                            fill="x", pady=(0, 8))
            for s in sessions:
                row = ctk.CTkFrame(hi, fg_color=C["panel"], corner_radius=6)
                row.pack(fill="x", pady=2)
                mode_label = (t("mode_name_hard") if s.get("mode") == "hard"
                              else t("mode_name_lite"))
                ctk.CTkLabel(
                    row,
                    text=t("history_session_row",
                          date=s.get("date", "?"),
                          start=s.get("start_time", "?"),
                          end=s.get("end_time", "?"),
                          mode=mode_label,
                          cycles=s.get("cycles", 0),
                          ram=s.get("ram_freed_mb", 0),
                          pis=s.get("pis_avg", 0)),
                    font=("Segoe UI", 11), text_color=C["text"],
                    anchor="w").pack(fill="x", padx=12, pady=8)
        else:
            ctk.CTkLabel(hi, text=t("history_none"),
                        font=("Segoe UI", 11), text_color=C["text_3"],
                        anchor="w").pack(fill="x", pady=(8, 12))

        # Export CSV button
        self._secondary_btn(hi, t("history_export"),
                           self._on_export_history).pack(
                               anchor="e", pady=(8, 0))

    def _on_export_history(self):
        if not self.session_history:
            return
        csv = self.session_history.export_csv(days=90)
        save_and_open(
            f"OMEGA_X_Sessions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            csv)
        self._toast(t("toast_history_csv"))

    # ────────────────────────────────────────────────────────────
    #  REFRESH (lazy, only updates visible widgets)
    # ────────────────────────────────────────────────────────────
    _STATE_KEYS = {"IDLE": "state_idle", "WORK": "state_work",
                   "MULTITASK": "state_multitask", "STUTTER": "state_stutter",
                   "GAME": "state_game", "CREATIVE": "state_creative"}

    def _state_label(self):
        """AI 내부 상태값을 사람이 읽는 말로."""
        key = self._STATE_KEYS.get(str(self.ai.last_state).upper())
        return t(key) if key else str(self.ai.last_state)

    def _status_text(self):
        """코어 모드가 돌고 있으면 그 모드를, 아니면 지금 상태를 보여준다."""
        lpi = self.optimizer.last_lpi
        try:
            if self.core_mode and self.core_mode.is_running():
                mode = self.core_mode.get_continuous_mode()
                name = (t("mode_name_hard") if mode == "hard"
                        else t("mode_name_lite"))
                return t("status_header_run", mode=name, lpi=lpi)
        except Exception as _dx:
            DIAG.q("OmegaGUI._status_text#0", _dx)
        return t("status_header", state=self._state_label(), lpi=lpi)

    def _refresh_visible(self):
        try:
            # ★여기서 재지 않는다★ 백그라운드 샘플러가 만들어둔 값만 읽는다.
            snap = self._ui_snap()

            # Cache header status to avoid flicker on every refresh
            if not hasattr(self, "_last_header_txt"):
                self._last_header_txt = None
            # ★수정★ 예전엔 AI 내부 상태값(IDLE/WORK/…)과 내부 지표명 LPI 가
            #   그대로 나갔고, 코어 모드가 돌고 있어도 헤더는 "IDLE" 이라
            #   한 화면에서 대기 중과 실행 중이 동시에 보였다.
            txt = self._status_text()
            if self.optimizer.last_anomaly: txt += " ⚠"
            if txt != self._last_header_txt:
                try: self.dynamic["header_status"].configure(text=txt)
                except Exception as _dx: DIAG.q("OmegaGUI._refresh_visible#0", _dx)
                self._last_header_txt = txt

            # Sidebar status with mini LPI bar — cache
            if not hasattr(self, "_last_sb_txt"):
                self._last_sb_txt = None
            lpi = self.optimizer.last_lpi
            sb_txt = f"● {self._state_label()} · {lpi}"
            if sb_txt != self._last_sb_txt:
                try: self.dynamic["sidebar_status"].configure(text=sb_txt)
                except Exception as _dx: DIAG.q("OmegaGUI._refresh_visible#1", _dx)
                self._last_sb_txt = sb_txt

            if self.active_section == "home":
                self._refresh_home(snap)
            elif self.active_section == "health":
                # Refresh leak detector card — every 3 cycles only
                if not hasattr(self, "_leak_cycle"): self._leak_cycle = 0
                self._leak_cycle += 1
                # 갱신 주기가 8초→1초로 빨라졌으므로 나눔수를 키운다.
                # (누수 카드는 초 단위로 바뀔 성질의 화면이 아니다)
                if self._leak_cycle % 10 == 0 and "sec_leak_list" in self.dynamic:
                    self._refresh_leak_card()
        except Exception as _dx:
            DIAG.q("OmegaGUI._refresh_visible#2", _dx)

    def _refresh_home(self, snap):
        # Lazy-init diff cache
        if not hasattr(self, "_lv"): self._lv = {}
        if not hasattr(self, "_last_health_score"): self._last_health_score = None
        if not hasattr(self, "_last_proc_count"): self._last_proc_count = None
        if not hasattr(self, "_health_cycle"): self._health_cycle = 0
        if not hasattr(self, "_bar_cycle"): self._bar_cycle = 0

        def set_if_changed(key, new_val):
            """Only update widget if value actually changed (avoids redraw)."""
            if self._lv.get(key) == new_val: return
            try:
                widget = self.dynamic.get(key)
                if widget:
                    widget.configure(text=new_val)
                    self._lv[key] = new_val
            except Exception as _dx: DIAG.q("OmegaGUI.set_if_changed#0", _dx)

        # Hero metrics + mini bars
        ram_pct = snap.get('ram_pct', 0)
        cpu_pct = snap.get('cpu_pct', 0)
        set_if_changed("sec_hero_ram", f"{ram_pct:.0f}%")
        set_if_changed("sec_hero_cpu", f"{cpu_pct:.0f}%")

        # 온도 — 타일이 있을 때만(측정되는 PC). 값이 중간에 끊기면
        # 숫자를 지어내지 않고 "—" 로 둔다.
        temp_c = snap.get("cpu_temp_c")
        if "sec_hero_temp" in self.dynamic:
            set_if_changed("sec_hero_temp",
                           "—" if temp_c is None else f"{temp_c:.0f}°C")
            try:
                thr = thermal_threshold()
            except Exception:
                thr = 85.0
            band = ("none" if temp_c is None else
                    "warm" if temp_c >= thr else "ok")
            if getattr(self, "_temp_band", None) != band:
                self._temp_band = band
                col = (C["text_3"] if band == "none" else
                       C["warn_text"] if band == "warm" else C["blue"])
                for k in ("sec_hero_temp", "sec_hero_temp_bar"):
                    w = self.dynamic.get(k)
                    if w is None: continue
                    try:
                        if k.endswith("_bar"): w.configure(fg_color=col)
                        else: w.configure(text_color=col)
                    except Exception as _dx: DIAG.q("OmegaGUI._refresh_home#0", _dx)
                lbl = self.dynamic.get("sec_hero_temp_note")
                if lbl is not None:
                    try:
                        lbl.configure(text=t("thermal_warm") if band == "warm"
                                      else t("thermal_label"),
                                      text_color=col if band == "warm"
                                      else C["text_3"])
                    except Exception as _dx: DIAG.q("OmegaGUI._refresh_home#1", _dx)
        
        # Update mini progress bars (throttle to every 2 cycles)
        self._bar_cycle += 1
        if self._bar_cycle % 2 == 0:
            _bars = [("ram", ram_pct), ("cpu", cpu_pct)]
            if "sec_hero_temp_bar" in self.dynamic and temp_c is not None:
                _bars.append(("temp", temp_c))   # 0~100℃ 를 그대로 %로
            for key, val in _bars:
                bar = self.dynamic.get(f"sec_hero_{key}_bar")
                if bar:
                    try:
                        w = max(4, int(56 * min(val, 100) / 100))
                        bar.configure(width=w)
                    except Exception as _dx:
                        DIAG.q("OmegaGUI._refresh_home#2", _dx)

        # Quick cards — cache health analysis (every 3 cycles)
        self._health_cycle += 1
        if self._health_cycle % 8 == 0:
            try:
                health = self._ui_data.get("health") or {}
                if not health: raise ValueError("not sampled yet")
                score = f"{health['overall_score']}/100"
                if score != self._last_health_score:
                    set_if_changed("sec_health_score", score)
                    self._last_health_score = score
            except Exception as _dx: DIAG.q("OmegaGUI._refresh_home#3", _dx)
        
        # Process count — cache (every 2 cycles)
        if self._health_cycle % 2 == 0:
            try:
                count = "%d apps" % (self._ui_data.get("proc_count") or 0)
                if count != self._last_proc_count:
                    set_if_changed("sec_proc_count", count)
                    self._last_proc_count = count
            except Exception as _dx: DIAG.q("OmegaGUI._refresh_home#4", _dx)
        
        set_if_changed("sec_disk_free", f"{snap.get('disk_free_gb', 0):.0f} GB free")

        if self.core_mode.is_running():
            mode = self.core_mode.get_continuous_mode()
            ai_quick = ("⚡ Lite" if mode == "lite" else "🔥 Hard") + " ●"
        else:
            ai_quick = "탭하여 시작" if I18N.lang == "ko" else "Tap to start"
        set_if_changed("sec_ai_state_quick", ai_quick)
        set_if_changed("sec_lpi_score", f"{self.optimizer.last_lpi}/100")

        # AI status
        set_if_changed("sec_ai_state", self.ai.last_state)
        set_if_changed("sec_ai_lpi", f"{self.optimizer.last_lpi}")
        set_if_changed("sec_ai_cycles", f"{self.ai.cycle}")
        actions = self.optimizer.last_actions
        set_if_changed("sec_ai_actions",
                      f"{len(actions)} active" if actions else "0")
        fg = snap.get("fg_name", "?")[:30]
        set_if_changed("sec_ai_summary",
                      f"FG: {fg} · State: {self.ai.last_state} · "
                      f"Conf: {self.ai.confidence*100:.0f}%")

        # Recommendations — cache (every 4 cycles to reduce calculation)
        if "sec_recs" in self.dynamic:
            if not hasattr(self, "_rec_cycle"): self._rec_cycle = 0
            self._rec_cycle += 1
            if self._rec_cycle % 4 == 0:  # Only calculate every 4 refresh cycles
                try:
                    cont = self.dynamic["sec_recs"]
                    # Only refresh if list changed length (avoid flicker)
                    recs = self.ai.recommendations(snap)
                    expected_count = max(1, min(4, len(recs))) if recs else 1
                    if len(cont.winfo_children()) != expected_count:
                        for w in cont.winfo_children(): w.destroy()
                        if not recs:
                            ctk.CTkLabel(
                                cont, text=t("status_optimal"),
                                font=("Segoe UI", 12), text_color=C["blue"],
                                anchor="w").pack(fill="x", pady=4)
                        else:
                            for r in recs[:4]:
                                row = ctk.CTkFrame(cont, fg_color=C["panel"],
                                                  corner_radius=6)
                                row.pack(fill="x", pady=4)
                                color = (C["blue"] if r["severity"] == "info" else
                                        C["warn_text"] if r["severity"] in
                                        ("medium", "warning") else
                                        C["danger_text"] if r["severity"] == "high"
                                        else C["text_3"])
                                ctk.CTkLabel(row, text="●",
                                            font=("Segoe UI", 14),
                                            text_color=color).pack(
                                                side="left", padx=(12, 8), pady=10)
                                tf = ctk.CTkFrame(row, fg_color="transparent")
                                tf.pack(side="left", fill="x", expand=True, pady=8)
                                ctk.CTkLabel(tf, text=r["title"],
                                            font=("Segoe UI", 12, "bold"),
                                            text_color=C["text"],
                                            anchor="w").pack(fill="x")
                                ctk.CTkLabel(tf, text=r["msg"],
                                            font=("Segoe UI", 10),
                                            text_color=C["text_3"],
                                            anchor="w").pack(fill="x")
                except Exception as _dx: 
                    DIAG.q("OmegaGUI._refresh_home#5", _dx)

    def _ui_pump(self):
        """메인 스레드에서만 도는 UI 갱신 펌프."""
        n = 0
        try:
            last_stats = None
            while self._ui_queue and n < 60:
                kind, payload = self._ui_queue.popleft()
                n += 1
                if kind == "step":
                    self._add_progress_row(payload)
                else:
                    last_stats = payload      # 통계는 최신 것만 반영
            self._render_progress_rows()
            self._refresh_activity_log()      # ★PATCH26★
            if last_stats is not None:
                self._apply_improve_stats(last_stats)
        except Exception as _dx:
            DIAG.q("OmegaGUI._ui_pump#0", _dx)
        if not getattr(self, "_shutting_down", False):
            # ★수정★ 큐가 비어 있는데도 200ms 마다 메인 스레드를 깨웠다.
            # 연속 모드를 안 쓰는 대부분의 시간에는 순수 낭비다.
            # 처리할 게 있었으면 200ms, 없으면 700ms 로 늦춘다.
            delay = 200 if n else 700
            self._ui_pump_id = self.root.after(delay, self._ui_pump)

    # 화면이 쓰는 값을 백그라운드에서 미리 재두는 주기(초).
    UI_SAMPLE_S = 1.0

    def _sample_ui_data(self):
        """★Tk 스레드 밖에서만 도는 수집★ 화면이 필요로 하는 값을 미리
        만들어 self._ui_data 에 넣어둔다. 갱신 콜백은 이 딕셔너리만 읽는다.

        여기 있는 호출(스냅샷·헬스 분석·프로세스 수)은 전부 psutil 을
        만지고, 그중 일부는 디스크·핸들을 기다린다. 예전엔 이게 전부
        Tk 스레드의 갱신 콜백 안에서 돌았다."""
        d = self._ui_data
        now = time.time()
        try:
            d["snap"] = self.observer.snapshot()
        except Exception as _dx:
            DIAG.q("OmegaGUI._sample_ui_data#0", _dx)
        if now - d.get("_health_t", 0.0) > 5.0:
            try:
                snap = d.get("snap") or self.observer.last_snap or {}
                if snap:
                    d["health"] = HealthAnalyzer.analyze(snap, PERF_HISTORY)
                    d["_health_t"] = now
            except Exception as _dx:
                DIAG.q("OmegaGUI._sample_ui_data#1", _dx)
        try:
            infos = PROC_CACHE.info_list_nowait()
            if infos:
                d["procs"] = infos
                d["proc_count"] = len(infos)
        except Exception as _dx:
            DIAG.q("OmegaGUI._sample_ui_data#2", _dx)

    def _ui_snap(self):
        """갱신 콜백이 쓰는 스냅샷. 없으면 빈 딕셔너리(절대 재지 않는다)."""
        return (self._ui_data.get("snap")
                or getattr(self.observer, "last_snap", None) or {})

    def _procs_nowait(self, force=False):
        """화면용 프로세스 목록. 강제 갱신도 '요청만' 하고 기다리지 않는다."""
        if force:
            try: PROC_CACHE._refresh_async()
            except Exception as _dx: DIAG.q("OmegaGUI._procs_nowait#0", _dx)
        procs = self._ui_data.get("procs")
        if procs:
            return procs
        try:
            return PROC_CACHE.info_list_nowait()
        except Exception:
            return []

    def _start_ui_sampler(self):
        def loop():
            while not getattr(self, "_shutting_down", False):
                try:
                    self._sample_ui_data()
                except Exception as _dx:
                    DIAG.q("OmegaGUI.loop#0", _dx)
                time.sleep(self.UI_SAMPLE_S)
        threading.Thread(target=loop, daemon=True).start()

    def _start_background(self):
        # Start auto optimizer
        self.optimizer.start()
        # ★화면용 수집을 Tk 스레드 밖으로★ (아래 loop 가 이 값을 읽는다)
        self._sample_ui_data()
        self._start_ui_sampler()
        # UI 마샬링 펌프 시작
        self._ui_pump()

        # ★GUI 최적화★ 창이 안 보이면 갱신 자체를 건너뛴다.
        # 최소화 상태에서도 8초마다 스냅샷·헬스분석·위젯 configure 를
        # 계속 돌리고 있었다. 아무도 안 보는 화면을 그리는 비용이다.
        # 덤으로 최소화 시 OMEGA X 자신을 EcoQoS 로 내려 발열/전력도 줄인다.
        def loop():
            try:
                st = self.root.state()
            except Exception:
                st = "normal"
            visible = st in ("normal", "zoomed")
            if visible != self._win_visible:
                self._win_visible = visible
                try:
                    self.core_mode.modern.set_self_efficiency(not visible)
                except Exception as _dx:
                    DIAG.q("OmegaGUI.loop#1", _dx)
            if visible:
                # ★주기 8초 → 1초★ 갱신 콜백에서 측정을 전부 걷어냈으므로
                # 이제 이 호출은 '바뀐 라벨만 configure' 하는 일뿐이다.
                # 8초 간격은 숫자가 멈춰 보여서 그 자체로 '느린 앱' 처럼
                # 읽혔다. 값이 안 바뀌면 위젯도 안 건드린다(set_if_changed).
                _t0 = time.perf_counter()
                self._refresh_visible()
                _ms = (time.perf_counter() - _t0) * 1000.0
                # 우리가 Tk 스레드를 얼마나 붙잡는지 스스로 기록해 둔다.
                self._ui_frame_ms = _ms
                if _ms > getattr(self, "_ui_frame_ms_max", 0.0):
                    self._ui_frame_ms_max = _ms
                delay = 1000
            else:
                delay = 30000
            self._refresh_timer_id = self.root.after(delay, loop)
        loop()

        # Show welcome dialog on first run (deferred so window is visible first)
        self.root.after(500, self._maybe_show_welcome)

        # Wire close button to quit handler
        self.root.protocol("WM_DELETE_WINDOW", self._on_close_request)

    # ────────────────────────────────────────────────────────────
    #  WELCOME DIALOG (first run)
    # ────────────────────────────────────────────────────────────
    def _welcome_flag_path(self):
        try:
            d = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
            d.mkdir(parents=True, exist_ok=True)
            return d / "welcome_seen"
        except Exception:
            return None

    def _maybe_show_welcome(self):
        """Show welcome dialog if first run (flag file not present)."""
        flag = self._welcome_flag_path()
        if flag and flag.exists():
            return  # already seen
        self._show_welcome_dialog()

    def _show_welcome_dialog(self):
        # Modal-ish overlay (Toplevel)
        dlg = ctk.CTkToplevel(self.root)
        dlg.title(t("welcome_title"))
        dlg.geometry("560x520")
        dlg.resizable(False, False)
        dlg.configure(fg_color=C["bg"])
        # Center on parent
        dlg.transient(self.root)
        dlg.grab_set()
        try:
            self.root.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - 560) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - 520) // 2
            dlg.geometry(f"560x520+{max(0,x)}+{max(0,y)}")
        except Exception as _dx: DIAG.q("OmegaGUI._show_welcome_dialog#0", _dx)

        inner = ctk.CTkFrame(dlg, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=32, pady=28)

        # Title
        ctk.CTkLabel(inner, text="◆ OMEGA X",
                    font=("Segoe UI", 28, "bold"),
                    text_color=C["blue"], anchor="w").pack(fill="x")
        ctk.CTkLabel(inner, text=t("welcome_subtitle"),
                    font=("Segoe UI", 12), text_color=C["text_2"],
                    anchor="w").pack(fill="x", pady=(2, 24))

        # 3 steps
        for title_key, desc_key in [
            ("welcome_step1_title", "welcome_step1_desc"),
            ("welcome_step2_title", "welcome_step2_desc"),
            ("welcome_step3_title", "welcome_step3_desc"),
        ]:
            row = ctk.CTkFrame(inner, fg_color=C["panel"], corner_radius=8)
            row.pack(fill="x", pady=4)
            tf = ctk.CTkFrame(row, fg_color="transparent")
            tf.pack(fill="x", padx=16, pady=12)
            ctk.CTkLabel(tf, text=t(title_key),
                        font=("Segoe UI", 13, "bold"),
                        text_color=C["text"], anchor="w").pack(fill="x")
            ctk.CTkLabel(tf, text=t(desc_key),
                        font=("Segoe UI", 11),
                        text_color=C["text_3"], anchor="w",
                        justify="left", wraplength=460).pack(
                            fill="x", pady=(2, 0))

        # Bottom buttons
        btn_row = ctk.CTkFrame(inner, fg_color="transparent")
        btn_row.pack(fill="x", pady=(20, 0))

        def close_dlg(mark_seen=True):
            if mark_seen:
                flag = self._welcome_flag_path()
                if flag:
                    try: flag.touch()
                    except Exception as _dx: DIAG.q("OmegaGUI.close_dlg#0", _dx)
            try: dlg.grab_release()
            except Exception as _dx: DIAG.q("OmegaGUI.close_dlg#1", _dx)
            try: dlg.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI.close_dlg#2", _dx)

        # "Don't show again" link-style button (subtle)
        ctk.CTkButton(btn_row, text=t("welcome_dont_show"),
                     fg_color="transparent", text_color=C["text_3"],
                     hover_color=C["panel"], font=("Segoe UI", 11),
                     corner_radius=6, height=36,
                     command=lambda: close_dlg(True)).pack(side="left")

        # Primary "Get Started"
        ctk.CTkButton(btn_row, text=t("welcome_get_started"),
                     fg_color=C["btn_primary"], hover_color=C["btn_primary_h"],
                     text_color="#FFFFFF", font=("Segoe UI", 12, "bold"),
                     corner_radius=8, height=40, width=140,
                     command=lambda: close_dlg(True)).pack(side="right")

    # ────────────────────────────────────────────────────────────
    #  QUIT CONFIRMATION
    # ────────────────────────────────────────────────────────────
    def _on_close_request(self):
        """Window X clicked. If Core running, ask for confirmation."""
        if self.core_mode and self.core_mode.is_running():
            self._show_quit_confirm()
        else:
            # ★수정★ 예전엔 곧바로 destroy 만 했다. 코어가 안 돌고 있어도
            # Auto 루프가 EcoQoS 등을 걸어둔 상태일 수 있으므로 정리 경로를
            # 반드시 태운다.
            self._on_closing()

    def _show_quit_confirm(self):
        dlg = ctk.CTkToplevel(self.root)
        dlg.title(t("quit_title"))
        dlg.geometry("420x200")
        dlg.resizable(False, False)
        dlg.configure(fg_color=C["bg"])
        dlg.transient(self.root)
        dlg.grab_set()
        try:
            self.root.update_idletasks()
            x = self.root.winfo_x() + (self.root.winfo_width() - 420) // 2
            y = self.root.winfo_y() + (self.root.winfo_height() - 200) // 2
            dlg.geometry(f"420x200+{max(0,x)}+{max(0,y)}")
        except Exception as _dx: DIAG.q("OmegaGUI._show_quit_confirm#0", _dx)

        inner = ctk.CTkFrame(dlg, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=24, pady=20)

        ctk.CTkLabel(inner, text=t("quit_title"),
                    font=("Segoe UI", 16, "bold"),
                    text_color=C["text"], anchor="w").pack(fill="x")

        mode = self.core_mode.get_continuous_mode() or "Core"
        mode_label = (t("ai_lite_title") if mode == "lite"
                     else t("ai_hard_title"))
        ctk.CTkLabel(inner, text=t("quit_running", mode=mode_label),
                    font=("Segoe UI", 12),
                    text_color=C["text_2"], anchor="w",
                    wraplength=380, justify="left").pack(
                        fill="x", pady=(8, 16))

        btn_row = ctk.CTkFrame(inner, fg_color="transparent")
        btn_row.pack(fill="x", side="bottom")

        def cancel():
            try: dlg.grab_release()
            except Exception as _dx: DIAG.q("OmegaGUI.cancel#0", _dx)
            try: dlg.destroy()
            except Exception as _dx: DIAG.q("OmegaGUI.cancel#1", _dx)

        def quit_now():
            try: self.core_mode.stop_continuous()
            except Exception as _dx: DIAG.q("OmegaGUI.quit_now#0", _dx)
            self.root.destroy()

        ctk.CTkButton(btn_row, text=t("quit_no"),
                     fg_color=C["btn_sec"], hover_color=C["btn_sec_h"],
                     text_color=C["blue"], font=("Segoe UI", 12),
                     corner_radius=8, height=36, width=110,
                     border_width=1, border_color=C["border"],
                     command=cancel).pack(side="left")
        ctk.CTkButton(btn_row, text=t("quit_yes"),
                     fg_color=C["btn_primary"], hover_color=C["btn_primary_h"],
                     text_color="#FFFFFF", font=("Segoe UI", 12, "bold"),
                     corner_radius=8, height=36, width=140,
                     command=quit_now).pack(side="right")


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================
def _show_admin_required_dialog():
    """Show a dialog when admin privileges are required."""
    import tkinter as tk_root
    from tkinter import messagebox
    
    root = tk_root.Tk()
    root.withdraw()  # Hide main window
    
    result = messagebox.askyesno(
        f"{APP_NAME} v{APP_VERSION} — Admin Required",
        f"{APP_NAME} requires administrator privileges to optimize your system.\n\n"
        "Would you like to restart with admin privileges?\n\n"
        "Click 'Yes' to restart (UAC prompt will appear).\n"
        "Click 'No' to exit."
    )
    root.destroy()
    
    if result:
        return request_admin_elevation()
    return False


def _show_loading_screen(root):
    """Show a loading screen while initializing."""
    root.geometry("500x300")
    root.title(f"{APP_NAME} v{APP_VERSION} — Starting...")
    apply_window_icon(root)
    root.configure(fg_color=C["bg"])
    
    frame = ctk.CTkFrame(root, fg_color=C["bg"])
    frame.pack(fill="both", expand=True, padx=40, pady=40)
    
    # Logo
    ctk.CTkLabel(frame, text="◆ OMEGA X",
                font=("Segoe UI", 28, "bold"),
                text_color=C["blue"]).pack(pady=(20, 30))
    
    # Status message
    status_label = ctk.CTkLabel(frame, text=t("splash_init"),
                                font=("Segoe UI", 13),
                                text_color=C["text_2"])
    status_label.pack(pady=10)
    
    # Spinner/progress
    spinner_label = ctk.CTkLabel(frame, text="◐",
                                font=("Segoe UI", 24),
                                text_color=C["blue"])
    spinner_label.pack(pady=20)
    
    ctk.CTkLabel(frame, text=t("splash_wait"),
                font=("Segoe UI", 11),
                text_color=C["text_3"]).pack(pady=(20, 0))
    
    root.update()
    return status_label, spinner_label


def _update_loading_status(status_label, spinner_label, msg, spinner_frame=0):
    """Update loading screen with new status."""
    spinners = ["◐", "◓", "◑", "◒"]
    try:
        status_label.configure(text=msg)
        spinner_label.configure(text=spinners[spinner_frame % 4])
        status_label.master.master.update()
    except Exception as _dx:
        DIAG.q("module._update_loading_status#0", _dx)


def _run_post_update_selftest(arg):
    """빌드/업데이트 후 EXE 무결성 + 버전 일치 검증.

    호출 형식 (둘 다 지원):
        --selftest=<결과파일경로>
        --selftest=<결과파일경로>;<기대버전>      ← 권장

    <기대버전> 이 주어지면, EXE 안에 번들된 version.txt 의 APP_VERSION 이
    그 값과 정확히 같은지 EXE 스스로 검증한다. 다르면 FAIL 을 기록하고
    종료코드 1 로 끝낸다. => build_exe.bat 의 findstr 검증에만 의존하지
    않으므로, .spec 으로 직접 빌드하거나 수동 빌드해도 desync 된 EXE 는
    이 단계에서 반드시 걸린다.

    이 함수에 도달 = PyInstaller 번들 + 모든 최상위 import 정상.
    결과를 파일에 기록 후 즉시 종료 (GUI 미생성).
    """
    raw = arg.split("=", 1)[1] if "=" in arg else ""
    raw = raw.strip().strip('"\'')
    # '경로;기대버전' 형태 파싱. 세미콜론이 없으면 기대버전은 빈 값.
    if ";" in raw:
        result_path, expected_version = raw.split(";", 1)
        result_path = result_path.strip()
        expected_version = expected_version.strip().lstrip("vV").strip()
    else:
        result_path = raw
        expected_version = ""

    reason = "OK"
    detected_version = ""
    try:
        import customtkinter as _ctk  # noqa: F401
        import psutil as _ps          # noqa: F401
        import requests as _rq        # noqa: F401
        from packaging import version as _pv  # noqa: F401
        if not (isinstance(APP_VERSION, str) and APP_VERSION.strip()):
            raise RuntimeError("APP_VERSION invalid")
        detected_version = APP_VERSION.strip()
        # ★ 버전 일치 검증 ★ 기대버전이 주어졌는데 다르면 desync 빌드다.
        if expected_version and detected_version != expected_version:
            raise RuntimeError(
                "VERSION_MISMATCH: 번들된 버전 " + detected_version
                + " 가 기대값 " + expected_version + " 와 다릅니다. "
                "version.txt 가 번들에 제대로 포함되지 않은 desync 빌드입니다."
            )
    except Exception as e:
        reason = f"FAIL:{type(e).__name__}:{e}"
    try:
        if result_path:
            with open(result_path, "w", encoding="utf-8") as fh:
                # 1행: OK / FAIL  (batch 의 findstr /B "OK" 검사용)
                # 2행: VERSION=<번들된 APP_VERSION>  (version.txt 대조용)
                fh.write(reason + "\n")
                fh.write("VERSION=" + detected_version + "\n")
    except OSError as _dx:
        DIAG.q("module._run_post_update_selftest#0", _dx)
    sys.exit(0 if reason == "OK" else 1)


def _consent_flag_path():
    try:
        d = Path(os.environ.get("APPDATA", str(Path.home()))) / "OMEGA_X"
        d.mkdir(parents=True, exist_ok=True)
        return d / "consent.txt"
    except Exception:
        return None


def _consent_already_given():
    """이번 EULA_VERSION 에 대해 이미 동의했으면 True."""
    p = _consent_flag_path()
    if not p:
        return False
    try:
        if not p.is_file():
            return False
        first = p.read_text(encoding="utf-8").splitlines()[:1]
        return bool(first) and first[0].strip() == EULA_VERSION
    except Exception:
        return False


def _record_consent():
    p = _consent_flag_path()
    if not p:
        return
    try:
        p.write_text(
            f"{EULA_VERSION}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n",
            encoding="utf-8")
    except Exception as _dx:
        DIAG.q("module._record_consent#0", _dx)


# 사용 동의/면책 고지 본문 (한/영). 시스템을 실제로 변경하는 도구이므로
# 웹사이트가 아니라 앱 자체에서 첫 실행 시 명시적 동의를 받아야 면책이
# 성립한다(특히 GitHub 등에서 EXE 만 직접 받은 사용자).
_CONSENT_TEXT = {
    "ko": (
        "OMEGA X 사용 전 동의\n"
        "\n"
        "OMEGA X 는 성능 향상을 위해 사용자의 Windows 시스템을 실제로 "
        "변경합니다. 시작하기 전에 아래 내용을 확인하고 동의해 주세요.\n"
        "\n"
        "1. 되돌려지는 변경\n"
        "• 전원 계획을 고성능으로 전환합니다. 앱을 종료하면 원래 계획으로 "
        "복원합니다.\n"
        "• 백그라운드 프로세스의 우선순위를 낮추고 포그라운드 앱의 우선순위를 "
        "높입니다. 일정 시간이 지나거나 앱을 종료하면 복원합니다.\n"
        "• 일부 백그라운드 프로세스에 Windows 절전 모드(EcoQoS), 메모리 "
        "우선순위 하향, CPU 코어 선호도 힌트를 적용합니다. 해당 앱이 "
        "화면 앞으로 오거나 최적화를 중지하면 즉시 해제합니다.\n"
        "• Windows 백그라운드 서비스(Windows Search, 진단 추적, SysMain)를 "
        "일시중지합니다. 5분 뒤 자동으로 재개하며, 앱 종료 시에도 재개합니다.\n"
        "• 게임·영상 작업 중 GPU 작업 우선순위와 시스템 타이머 해상도를 "
        "조정합니다. 최적화를 중지하면 원래대로 돌아갑니다.\n"
        "\n"
        "2. 되돌려지지 않는 변경 — 특히 확인해 주세요\n"
        "• 레지스트리 값 변경: GameDVR(Windows 게임 녹화)을 끕니다. "
        "HKEY_CURRENT_USER 의 GameDVR_Enabled 와 AppCaptureEnabled 를 0 으로 "
        "설정하며, 앱을 지워도 자동으로 되돌아가지 않습니다. Windows 설정 > "
        "게임 > 캡처에서 언제든 다시 켤 수 있습니다.\n"
        "• 임시 파일 삭제: 저장소 탭에서 사용자가 직접 실행할 때만 수행하며, "
        "최적화 중에 자동으로 실행되지 않습니다. 대상은 사용자 임시 폴더"
        "(%TEMP%)에 있는 24시간 이상 된 파일이며, Windows 시스템 폴더와 "
        "프리페치는 건드리지 않습니다. 삭제된 파일은 휴지통을 거치지 않아 "
        "복구할 수 없습니다.\n"
        "• 휴지통 비우기: 사용자가 직접 실행하는 기능이며, 실행하면 휴지통 "
        "내용이 영구 삭제됩니다.\n"
        "• 시작 프로그램 비활성화·프로세스 종료: 사용자가 목록에서 직접 "
        "선택했을 때만 수행합니다. 저장하지 않은 작업이 있는 프로그램을 "
        "종료하면 그 작업은 사라집니다.\n"
        "\n"
        "3. 관리자 권한\n"
        "• Hard Core 모드 등 일부 기능은 관리자 권한이 필요합니다. 필요한 "
        "시점에만 UAC 창으로 요청하며, 거부해도 나머지 기능은 사용할 수 "
        "있습니다.\n"
        "\n"
        "4. 데이터 처리\n"
        "• 이 PC 에만 저장: 최적화 세션 기록(최근 90일), 오류 로그(최대 1MB), "
        "동의 기록을 %APPDATA%\\OMEGA_X 폴더에 저장합니다. 해당 폴더를 지우면 "
        "함께 삭제됩니다.\n"
        "• 외부 전송: 새 버전 확인·다운로드를 위해 GitHub 에 표준 네트워크 "
        "요청을 보냅니다. 이때 앱 이름과 버전이 담긴 User-Agent 가 전달됩니다. "
        "그 외 개인정보나 사용 데이터는 어디에도 전송하지 않습니다.\n"
        "\n"
        "5. 온라인 게임 주의\n"
        "• 일부 게임의 안티치트 시스템이 프로세스 우선순위 변경 같은 최적화 "
        "동작을 비정상 행위로 탐지해 계정이 제재될 수 있습니다. 온라인 게임 "
        "실행 중 사용에 따른 책임은 사용자에게 있습니다.\n"
        "\n"
        "6. 라이선스\n"
        "• OMEGA X 는 소스 코드가 전면 공개된 자유 소프트웨어이며, GNU 일반 공중 "
        "사용 허가서(GPL) 제3판 또는 그 이후 판에 따라 배포됩니다. 누구나 소스 "
        "코드를 받아 자유롭게 사용·수정·재배포할 수 있고, 상업적 이용을 포함해 "
        "이용 분야에는 제한이 없습니다.\n"
        "• 다만 이 프로그램이나 그 파생물을 배포할 때에는 동일한 GPL 조건을 "
        "적용하고, 받는 사람에게 전체 소스 코드를 함께 제공해야 합니다. 저작권 "
        "표시와 무보증 고지도 지워서는 안 됩니다.\n"
        "• 소스 코드: https://github.com/sjw0328/source\n"
        "• 라이선스 전문: https://www.gnu.org/licenses/gpl-3.0.html\n"
        "\n"
        "7. 보증 및 책임의 제한\n"
        "본 소프트웨어는 '있는 그대로(AS IS)' 제공되며, 상품성·특정 목적 "
        "적합성을 포함한 어떠한 명시적·묵시적 보증도 하지 않습니다. 관련 "
        "법령이 허용하는 최대 범위에서, 본 소프트웨어 사용으로 발생한 직접·"
        "간접·부수적 손해(데이터 손실, 계정 제재, 시스템 불안정 포함)에 대한 "
        "책임을 지지 않습니다. 다만 법률상 배제할 수 없는 책임은 제한되지 "
        "않습니다.\n"
        "\n"
        "위 내용에 동의하셔야 사용할 수 있습니다."
    ),
    "en": (
        "Before you use OMEGA X\n"
        "\n"
        "OMEGA X makes real changes to your Windows system in order to improve "
        "performance. Please review and agree before continuing.\n"
        "\n"
        "1. Changes that are reverted\n"
        "• Switches the power plan to High Performance. Your original plan is "
        "restored when the app exits.\n"
        "• Lowers the priority of background processes and raises the priority "
        "of the app you are using. Restored after a short time, and on exit.\n"
        "• Applies Windows power-saving mode (EcoQoS), lowered memory priority, "
        "and CPU core preference hints to some background processes. These are "
        "released immediately when that app comes to the foreground or when you "
        "stop optimization.\n"
        "• Temporarily pauses background Windows services (Windows Search, "
        "diagnostic tracking, SysMain). They resume automatically after five "
        "minutes, and also when the app exits.\n"
        "• Adjusts GPU scheduling priority and system timer resolution while "
        "gaming or doing media work. Both return to normal when you stop "
        "optimization.\n"
        "\n"
        "2. Changes that are NOT reverted — please read carefully\n"
        "• Registry changes: turns off GameDVR (Windows game recording). It "
        "sets GameDVR_Enabled and AppCaptureEnabled under HKEY_CURRENT_USER to "
        "0, and this is not undone automatically, even if you uninstall the "
        "app. You can turn it back on at any time in Windows Settings > Gaming "
        "> Captures.\n"
        "• Temp file deletion: runs only when you start it yourself from the "
        "Storage tab — never automatically during optimization. It targets files "
        "older than 24 hours inside your user temp folder (%TEMP%) only, and does "
        "not touch Windows system folders or the Prefetch cache. Deleted files "
        "bypass the Recycle Bin and cannot be recovered.\n"
        "• Emptying the Recycle Bin: this runs only when you start it yourself, "
        "and it permanently deletes the Recycle Bin contents.\n"
        "• Disabling startup items and ending processes: performed only for "
        "items you select yourself. Ending a program with unsaved work will "
        "lose that work.\n"
        "\n"
        "3. Administrator rights\n"
        "• Some features, such as Hard Core mode, require administrator rights. "
        "You are asked through the UAC prompt only when they are needed, and "
        "the remaining features still work if you decline.\n"
        "\n"
        "4. Data handling\n"
        "• Stored on this PC only: optimization session history (last 90 days), "
        "an error log (up to 1 MB), and your consent record, all under "
        "%APPDATA%\\OMEGA_X. Deleting that folder deletes them.\n"
        "• Sent externally: standard network requests to GitHub to check for "
        "and download new versions. These carry a User-Agent containing the app "
        "name and version. No other personal or usage data is sent anywhere.\n"
        "\n"
        "5. Online games\n"
        "• Some anti-cheat systems may treat optimization activity, such as "
        "changing process priorities, as abnormal behaviour and could restrict "
        "your account. You are responsible for using OMEGA X while online games "
        "are running.\n"
        "\n"
        "6. Licence\n"
        "• OMEGA X is free software distributed under the GNU General Public "
        "License, version 3 or (at your option) any later version. Anyone may "
        "obtain, use, modify and redistribute the source code, and there is no "
        "restriction on the field of use — commercial use included.\n"
        "• When you distribute this program or a derivative work, you must apply "
        "the same GPL terms and provide the complete corresponding source code "
        "to the recipient. Copyright and warranty notices must be preserved.\n"
        "• Source code: https://github.com/sjw0328/source\n"
        "• Full licence text: https://www.gnu.org/licenses/gpl-3.0.html\n"
        "\n"
        "7. Warranty and limitation of liability\n"
        "This software is provided 'AS IS', without warranty of any kind, "
        "express or implied, including merchantability and fitness for a "
        "particular purpose. To the maximum extent permitted by applicable law, "
        "no liability is accepted for any direct, indirect or incidental "
        "damages arising from its use, including data loss, account "
        "restrictions or system instability. Nothing here limits liability that "
        "cannot be excluded by law.\n"
        "\n"
        "You must agree to the above to continue."
    ),
}


def _require_user_consent():
    """최초 실행(또는 EULA 버전 변경) 시 동의 화면을 띄운다.
    동의하면 True, 거부/창 닫기면 False. False 면 호출부(main)가 앱을 종료한다.
    GUI 본체가 생성되기 전, 가장 먼저 호출된다."""
    if _consent_already_given():
        return True

    # 이 화면은 언어 선택 UI 보다 먼저 뜬다. I18N.lang 은
    # _detect_windows_language() 가 Windows UI 언어에서 이미 정해둔 값이므로
    # 한국어 Windows → 한국어 약관, 그 외 → 영어 약관이 자동으로 잡힌다.
    lang = getattr(I18N, "lang", "en")
    if lang not in _CONSENT_TEXT:
        lang = "en"
    body = _CONSENT_TEXT[lang]
    agree_txt = t("consent_agree")
    decline_txt = t("consent_decline")
    title_txt = f"{APP_NAME} — {t('consent_title')}"

    result = {"agreed": False}
    try:
        win = ctk.CTk()
        win.title(title_txt)
        win.geometry("620x620")
        win.resizable(False, False)
        try: win.configure(fg_color=C["bg"])
        except Exception as _dx: DIAG.q("module._require_user_consent#0", _dx)

        # 닫기(X) = 거부로 처리
        def _on_x():
            result["agreed"] = False
            try: win.destroy()
            except Exception as _dx: DIAG.q("module._on_x#0", _dx)
        win.protocol("WM_DELETE_WINDOW", _on_x)

        ctk.CTkLabel(
            win, text=title_txt, font=("Segoe UI", 16, "bold"),
            text_color=C.get("text", "#1A1A1A")).pack(
                anchor="w", padx=24, pady=(20, 8))

        box = ctk.CTkTextbox(win, font=("Segoe UI", 12), wrap="word")
        box.pack(fill="both", expand=True, padx=24, pady=(0, 12))
        box.insert("1.0", body)
        box.configure(state="disabled")

        btn_row = ctk.CTkFrame(win, fg_color="transparent")
        btn_row.pack(fill="x", padx=24, pady=(0, 20))

        def _on_agree():
            result["agreed"] = True
            _record_consent()
            try: win.destroy()
            except Exception as _dx: DIAG.q("module._on_agree#0", _dx)

        def _on_decline():
            result["agreed"] = False
            try: win.destroy()
            except Exception as _dx: DIAG.q("module._on_decline#0", _dx)

        ctk.CTkButton(
            btn_row, text=decline_txt, command=_on_decline,
            fg_color="transparent", border_width=1,
            text_color=C.get("text_2", "#555555"),
            border_color=C.get("text_3", "#999999"), width=150).pack(side="left")
        ctk.CTkButton(
            btn_row, text=agree_txt, command=_on_agree,
            fg_color=C.get("btn_primary", "#0066FF"),
            hover_color=C.get("btn_primary_h", "#0052CC"),
            width=180).pack(side="right")

        win.mainloop()
    except Exception as e:
        # 동의 UI 를 띄우지 못하면 안전 측으로 진행을 막지 않되 기록만 남긴다.
        # (UI 자체가 안 뜨는 환경이면 어차피 앱 본체도 못 뜬다.)
        print(f"[warn] consent dialog failed: {e}")
        return True
    finally:
        # 다음 ctk.CTk() (loading_root) 가 깨끗하게 생성되도록 정리.
        try:
            import tkinter as _tk
            _tk._default_root = None
        except Exception as _dx:
            DIAG.q("module._require_user_consent#1", _dx)

    return result["agreed"]


def main():
    """Boot order is critical — GUI must appear within 1s.
    Heavy initialization is deferred to background after window is shown.

    Admin 권한이 없어도 일반 권한으로 정상 실행됨. admin이 필요한 작업
    (Hard Core 모드, Standby List Purge 등)을 사용자가 누를 때만 UAC 요청.
    재시작 시 `--auto-action=<mode>` argv로 자동 실행할 모드 전달 가능.
    """
    # ★테마는 첫 창이 뜨기 전에 적용해야 한다.★ 예전엔 OmegaGUI.__init__
    # 에서야 apply_theme 를 불러서, 다크 모드인데도 로딩 화면과 동의 창이
    # 흰색으로 떴다가 본창만 어두워지는 깜빡임이 났다.
    try:
        apply_theme(SETTINGS.get("theme", "light"))
    except Exception as _dx:
        DIAG.q("module.main#0", _dx)

    # ─── --selftest: 업데이트 후 무결성 검증 (GUI 생성 전 최우선) ────
    for _arg in sys.argv[1:]:
        if _arg.startswith("--selftest"):
            _run_post_update_selftest(_arg)
            return

    # ─── auto-action 파싱 ─────────────────────────────────────────
    _auto_action = None
    for _arg in sys.argv[1:]:
        if _arg.startswith("--auto-action="):
            _auto_action = _arg.split("=", 1)[1].strip()
            break

    # Install global exception handler — logs to %APPDATA%\OMEGA_X\error.log
    install_global_exception_handler()

    # ─── 최초 실행: 사용 동의/면책 고지 (GUI 본체 생성 전) ──────────
    # 시스템을 실제로 변경하는 도구이므로, 첫 실행 시 명시적 동의를 받는다.
    # 동의하지 않으면 앱을 시작하지 않는다. (admin 재시작 시에는 이미
    # 동의 기록이 있어 다시 묻지 않는다.)
    if not _require_user_consent():
        return

    # ─── Phase 1: Show Loading Screen ─────────────────────────────
    loading_root = ctk.CTk()
    status_lbl, spinner_lbl = _show_loading_screen(loading_root)
    spin_frame = 0

    # ─── Phase 2: Minimal sync init (must be fast) ────────────────
    # Only objects needed to construct GUI itself
    try:
        _update_loading_status(status_lbl, spinner_lbl, "Loading system metrics...", spin_frame)
        spin_frame += 1
        perf = WinPerfCounters()           # has its own bg thread
        # ★지난 실행이 비정상 종료됐을 때의 잔재부터 치운다★
        # EcoQoS 와 CPU 최대 속도 제한은 우리가 풀어주지 않으면 대상
        # 프로세스/전원 계획에 그대로 남는다. 크래시·강제 종료 뒤
        # "앱을 껐는데도 느리다"의 직접 원인이라 부팅 경로 맨 앞에서 푼다.
        try:
            _swept = ECO.sweep_startup()
            if _swept: print(f"[info] EcoQoS 잔재 {_swept}개 해제")
        except Exception as e:
            print(f"[warn] EcoQoS sweep: {e}")
        try:
            ThermalGovernor.recover_startup()
        except Exception as e:
            print(f"[warn] thermal cap recover: {e}")

        # 온도 관측 — 실패해도 앱은 그대로 뜬다(ok=False 로 숨김 처리).
        thermal = ThermalMonitor()
        
        _update_loading_status(status_lbl, spinner_lbl, "Initializing AI Core...", spin_frame)
        spin_frame += 1
        observer = Observer(perf, thermal)  # cheap — no thread
        ai = AICore()                      # pure Python, instant
        policy = PolicyEngine()            # instant
        
        _update_loading_status(status_lbl, spinner_lbl, "Setting up safety guards...", spin_frame)
        spin_frame += 1
        guard = SafetyGuard()              # instant
        executor = LatencyOptimizer(guard) # instant
        core_mode = CoreMode(observer, guard, executor)  # instant

        # Smart automation managers — created but NOT started yet
        _update_loading_status(status_lbl, spinner_lbl, "Configuring automation...", spin_frame)
        spin_frame += 1
        game_detect = GameAutoDetect(observer, core_mode)
        scheduler = Scheduler(core_mode, CleanupEngine, observer)
        battery_saver = BatterySaver(observer, executor)
        leak_detector = RamLeakDetector(observer)

        # SessionHistory does file I/O — wrap in try
        session_history = None
        try:
            session_history = SessionHistory()
        except Exception as e:
            print(f"[warn] SessionHistory init failed: {e}")

        # 누수 감지 자동 정리 핸들러
        def auto_trim_handler(pid, name):
            # ★수정★ 누수 감지 자동 정리도 포그라운드 트리는 건드리지
            # 않는다. 사용자가 지금 쓰는 앱의 워킹셋을 강제로 비우면
            # 그 즉시 하드 폴트가 몰려 눈에 띄게 버벅인다.
            try:
                if not is_target(pid, name or ""): return
                h = _open_proc(pid, ACC_TRIM_WS)
                if h:
                    psapi.EmptyWorkingSet(h)
                    _close(h)
            except Exception as _dx: DIAG.q("module.auto_trim_handler#0", _dx)

        leak_detector.set_auto_handler(auto_trim_handler)

        log_buffer = deque(maxlen=200)
        def log_fn(msg):
            ts = datetime.now().strftime("%H:%M:%S")
            log_buffer.append(f"[{ts}] {msg}")
        def callback(state_dict):
            results = state_dict.get("results", [])
            for action, msg in results:
                log_fn(f"{action}: {msg}")

        _update_loading_status(status_lbl, spinner_lbl, "Building user interface...", spin_frame)
        spin_frame += 1
        optimizer = AutoOptimizer(observer, ai, policy, guard, executor,
                                 log_fn, callback)
        # ★결선★ Auto 루프가 연속 모드 실행 여부를 알아야 중복 액션을
        # 멈출 수 있다. 이게 없으면 두 루프가 같은 프로세스의 우선순위
        # 원래값 기록을 서로 덮어써서 복구가 깨진다.
        optimizer.core_mode = core_mode
        # ★온도 자동 완화★ 기본은 꺼짐. 설정에서 켜야 동작한다.
        governor = ThermalGovernor(thermal, guard, log_fn)

    except Exception as e:
        # Initialization failed
        import traceback
        tb = traceback.format_exc()
        print(f"[FATAL] Initialization failed: {e}\n{tb}")
        ERROR_LOG.log(type(e), e, tb, "main init")
        
        try:
            status_lbl.configure(text=t("init_failed"))
            spinner_lbl.configure(text="")
            loading_root.after(2000, loading_root.destroy)
            loading_root.mainloop()
        except Exception as _dx:
            DIAG.q("module.main#1", _dx)
        return

    # ─── Phase 3: Build GUI (replace loading screen) ────────────
    _update_loading_status(status_lbl, spinner_lbl, "Ready!", spin_frame)
    loading_root.after(400, loading_root.destroy)
    
    root = ctk.CTk()
    # FIX: 이중 CTk() 생성으로 무효화된 _default_root 복구
    import tkinter as _tk_fix
    _tk_fix._default_root = root
    try:
        gui = OmegaGUI(root, perf, observer, ai, policy, guard, executor,
                      optimizer, core_mode,
                      game_detect=game_detect,
                      scheduler=scheduler,
                      battery_saver=battery_saver,
                      leak_detector=leak_detector,
                      session_history=session_history)
        gui.governor = governor
    except Exception as e:
        # GUI build failed — show error in a basic window so user sees it
        import traceback
        tb = traceback.format_exc()
        print(f"[FATAL] GUI build failed: {e}\n{tb}")
        ERROR_LOG.log(type(e), e, tb, "GUI build")
        try:
            root.geometry("700x500")
            root.title(f"{APP_NAME} — Error")
            err_frame = ctk.CTkFrame(root, fg_color=C["card"])
            err_frame.pack(fill="both", expand=True, padx=20, pady=20)
            ctk.CTkLabel(err_frame,
                text=f"{APP_NAME} failed to start.\n\n{e}",
                font=("Segoe UI", 14, "bold"),
                text_color="#DC2626", justify="left",
                wraplength=640).pack(pady=(20, 10))
            tb_box = ctk.CTkTextbox(err_frame, height=300,
                                   font=("Consolas", 10))
            tb_box.pack(fill="both", expand=True, padx=10, pady=10)
            tb_box.insert("1.0", tb)
            tb_box.configure(state="disabled")
            ctk.CTkLabel(err_frame,
                text=f"Error log: {ERROR_LOG.get_log_path()}",
                font=("Segoe UI", 9),
                text_color=C["text_3"]).pack(pady=(10, 0))
        except Exception as _dx:
            DIAG.q("module.main#2", _dx)
        root.mainloop()
        return

    # ─── Phase 4: Defer heavy startup tasks ─────────────────────
    # Kick off the global process cache warm immediately — this happens on a
    # background thread so GUI stays responsive. By the time any consumer
    # asks for the cache, it's already populated.
    PROC_CACHE.warm_async()

    # leak_detector.start() spawns a background thread that calls
    # process_iter() — its own _loop now waits 15s before first sample.
    # Extended outer defer from 2s to 4s so first frame is well past.
    def deferred_startup():
        try: leak_detector.start()
        except Exception as e: print(f"[warn] leak_detector start: {e}")
        # ★설정에 저장된 자동화 토글을 복원한다.★ 예전에는 앱을 끄면
        # 게임 감지·스케줄러·배터리 절약이 매번 꺼진 채로 돌아왔다.
        for flag, mgr in (("auto_game_detect", game_detect),
                          ("auto_scheduler", scheduler),
                          ("auto_battery_saver", battery_saver)):
            try:
                if SETTINGS.get(flag) and mgr is not None:
                    mgr.start()
            except Exception as e:
                print(f"[warn] {flag} restore: {e}")
        # 온도 자동 완화도 저장된 상태로 복원한다.
        try:
            if SETTINGS.get("thermal_auto_mitigate"):
                governor.start()
        except Exception as e:
            print(f"[warn] thermal governor restore: {e}")
    root.after(4000, deferred_startup)

    # ─── auto-action 디스패치 (admin 재시작 후 자동 실행) ─────
    # GUI가 완전히 뜬 다음 (1.5초 후) 해당 모드 자동 시작
    if _auto_action in ("lite", "hard"):
        def _run_auto_action():
            try:
                # AI Core 섹션으로 이동
                gui._show_section("ai_core")
                # 모드 자동 시작 (admin 체크 통과 — 이미 admin으로 재시작됨)
                gui._toggle_continuous(_auto_action)
            except Exception as e:
                print(f"[warn] auto-action failed: {e}")
        root.after(1500, _run_auto_action)

    # ─── Phase 5: Run main loop ─────────────────────────────────
    try:
        root.mainloop()
    except KeyboardInterrupt:
        pass
    finally:
        # Cleanup in reverse order, all wrapped
        for stop_fn in [
            lambda: optimizer.stop(),
            lambda: core_mode.stop_continuous(),
            lambda: core_mode._restore_power_scheme(),
            # ★추가★ 신형 API(CPU Sets·메모리 우선순위·타이머 차단·GPU
            # 우선순위)와 EcoQoS 를 종료 시 반드시 원복한다. 안 그러면
            # 앱을 껐는데도 백그라운드 앱들이 계속 강등된 채 남는다.
            lambda: core_mode.modern.revert_all(),
            lambda: executor.revert_ecoqos_all(),
            lambda: guard.rollback_all(),
            lambda: game_detect.stop(),
            lambda: scheduler.stop(),
            lambda: battery_saver.stop(),
            lambda: leak_detector.stop(),
            lambda: perf._stop.set(),
        ]:
            try: stop_fn()
            except Exception as _dx: DIAG.q("module.main#3", _dx)


if __name__ == "__main__":
    main()
import streamlit as st

st.title("📈 FDC 플로우차트")

def fdc_remodeling():
    st.success("✅ FDC_REMODELING 실시")

def lot_hold():
    st.info("➡️ LOT_HOLD 이력 발생")
    if st.button("👉 LOT 계측 의뢰 및 후속 MONITORING", key="lot_monitoring"):
        st.success("✅ LOT 계측 의뢰 및 후속 MONITORING")
    if st.button("👉 RF_REF 상승 변화 발생 시 장비 점검", key="rf_check"):
        st.success("✅ RF_REF 상승 변화 발생 시 장비 점검")

def check_parameters():
    st.info("➡️ 동시 변화되는 PARAMETER 확인 후 점검 (RF_REF, PRESSURE, CONFINEMENT_RING 등)")

def viop_board_action():
    st.info("➡️ CAP_INTERFACE_BOARD, VIOP_BOARD, CAP_CAL, LEARN값_조치")

def confinement_ring_zero_change():
    st.info("➡️ CONFINEMENT_RING_ZERO점 확인 시 변화 발생")
    if st.button("👉 ENCODER 점검", key="encoder_check"):
        st.success("✅ ENCODER 점검 완료")
    if st.button("👉 SLIDER_LINER 점검", key="slider_check"):
        st.success("✅ SLIDER_LINER 점검 완료")
    if st.button("👉 INTERFACE_BOARD 점검", key="interface_check"):
        st.success("✅ INTERFACE_BOARD 점검 완료")

def confinement_ring_zero_ok():
    st.info("➡️ CONFINEMENT_RING_ZERO점 확인 시 이상 없을 시")
    if st.button("👉 CM1_BASE 점검", key="cm1_check"):
        st.success("✅ CM1_BASE 점검 완료")
    if st.button("👉 GAS_FLOW_HUNTING 여부 점검", key="gasflow_check"):
        st.success("✅ GAS_FLOW_HUNTING 여부 점검 완료")
    if st.button("👉 VAT_VALVE 사용 시 변화 여부 점검", key="vatvalve_check"):
        st.success("✅ VAT_VALVE 사용 시 변화 여부 점검 완료")

# ---------------------------
st.header("1. FDC")

selected = st.selectbox(
    "📂 하위 항목을 선택하세요:",
    [
        "",
        "1-1. IB1_FDC",
        "2-2. ESC_BIAS_VOLTAGE_FDC",
        "2-3. TCP_C1_CAP_FDC",
        "2-4. CONFINEMENT_RING_FDC"
    ]
)

if selected == "1-1. IB1_FDC":
    st.subheader("🔷 1-1. IB1_FDC")
    if st.button("👉 SUMMARY_TREND 확인 시 진행성 상향", key="ib1_progressive"):
        fdc_remodeling()
    if st.button("👉 SUMMARY_TREND 확인 시 순간 상향", key="ib1_instant"):
        lot_hold()

elif selected == "2-2. ESC_BIAS_VOLTAGE_FDC":
    st.subheader("🔷 2-2. ESC_BIAS_VOLTAGE_FDC")
    if st.button("👉 SUMMARY_TREND 확인 시 진행성 상향", key="esc_progressive"):
        fdc_remodeling()
    if st.button("👉 SUMMARY_TREND 확인 시 순간 상향 및 산포 발생", key="esc_instant"):
        check_parameters()

elif selected == "2-3. TCP_C1_CAP_FDC":
    st.subheader("🔷 2-3. TCP_C1_CAP_FDC")
    if st.button("👉 SUMMARY_TREND 확인 시 진행성 상향", key="tcp_progressive"):
        fdc_remodeling()
    if st.button("👉 SUMMARY_TREND 확인 시 순간 상향 및 산포 발생", key="tcp_instant"):
        viop_board_action()

elif selected == "2-4. CONFINEMENT_RING_FDC":
    st.subheader("🔷 2-4. CONFINEMENT_RING_FDC")
    if st.button("👉 SUMMARY_TREND 확인 시 진행성 상향", key="conf_progressive"):
        fdc_remodeling()

    if "conf_instant" not in st.session_state:
        st.session_state.conf_instant = False

    if st.button("👉 SUMMARY_TREND 확인 시 순간 상향 및 산포 발생", key="conf_instant_btn"):
        st.session_state.conf_instant = True

    if st.session_state.conf_instant:
        st.info("▼ CONFINEMENT_RING_ZERO점 확인")
        if "zero_check" not in st.session_state:
            st.session_state.zero_check = None

        col1, col2 = st.columns(2)
        with col1:
            if st.button("📍 변화 발생 시", key="zero_change"):
                st.session_state.zero_check = "change"
        with col2:
            if st.button("📍 이상 없을 시", key="zero_ok"):
                st.session_state.zero_check = "ok"

        if st.session_state.zero_check == "change":
            confinement_ring_zero_change()

        if st.session_state.zero_check == "ok":
            confinement_ring_zero_ok()

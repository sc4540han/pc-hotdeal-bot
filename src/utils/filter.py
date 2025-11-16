def is_pc_part(title: str, content: str = "") -> bool:
    text = f"{title} {content}".lower()

    PC = [
        "그래픽카드","gpu","vga","rtx","radeon","rx",
        "cpu","라이젠","ryzen","i5","i7","i9","intel",
        "램","ram","ddr4","ddr5",
        "ssd","nvme","하드","hdd",
        "메인보드","b550","b650","z590","z690","x570",
        "파워","psu",
        "쿨러","수냉","공랭","aio",
        "케이스","pc 케이스",
        "모니터","144hz","165hz","240hz"
    ]

    BLOCK = ["과자","옷","신발","생활","화장품","세제","식품"]

    if any(b in text for b in BLOCK):
        return False

    return any(k in text for k in PC)

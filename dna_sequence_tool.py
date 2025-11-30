import csv
import time
FILE_NAME="sequences.csv"
def save_sequences(sequences, filename="sequences.csv"):
    fieldnames=["ID","species","seq","note"]
    total = len(sequences)
    with open(filename,"w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        for i,row in enumerate(sequences,start=1):
            writer.writerow(row)
            if total > 0:
                ratio = i / total
                percent = int(ratio * 100)
                bar_len = 20  # 进度条长度（多少个 #）
                filled = int(ratio * bar_len)
                bar = "#" * filled + " " * (bar_len - filled)
        # \r 回到行首，end="" 不换行，flush=True 立即刷新显示
                print(f"\r保存中 |{bar}| {percent:3d}%", end="", flush=True)
        # 如果你想看到明显的动画效果，可以加一点延迟（真实保存时没必要）
                time.sleep(0.5)
        # 保存结束后，换行 + 提示
    print()  # 换行
def load_sequences(filename="sequences.csv"):
    sequences=[]
    try:
        with open(filename,"r",newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                sequences.append(row)
    except FileNotFoundError:
        pass
    return sequences
def add_newDNA_sequences(sequences):
    print("\n====添加一条新的序列====\n")
    new_id=add_id(sequences)
    new_species=add_species()
    new_seq=add_seq()
    new_note=add_note()
    sequences.append({
        "ID":new_id,
        "species":new_species,
        "seq":new_seq,
        "note":new_note
    })
    print("已成功添加一条序列！\n")
def look_allDNA_sequences(sequences):
    print("====查看所有DNA序列====\n")
    if not sequences:
        print("暂无数据\n")
        return
    print(f"{'序号':<6}{'ID':<12}{'物种名':<12}{'长度':<8}{'GC含量':<8}{'备注':<8}")
    print("-"*50)
    for i,row in enumerate(sequences,start=1):
        mun_all=len(row['seq'])
        if mun_all==0:
            mun_GC_all=0
        else:
            mun_GC=row['seq'].count("G")+row['seq'].count("C")
            mun_GC_all=mun_GC/mun_all*100
        print(f"{i:<6}{row['ID']:<14}{row['species']:<14}{mun_all:<8}{mun_GC_all:<8}{row['note']:<8}")
def analyse_oneDNA_sequences(sequences):
    print("====分析序列====\n")
    while True:
        user_id=input("请输入要分析得一个DNA序列ID:").strip()
        state_confirm = False
        if user_id == "":
            state_confirm = True
        else:
            for row in sequences:
                state_confirm=True
                if row['ID'] == user_id:
                    state_confirm = False
                    break
        if state_confirm:
            make_sure=input("输入有错，要退出分析吗？(键入任意字符退出，键入enter以继续)").strip()
            if make_sure=="":
                continue
            else:
                break
        else:
            for row in sequences:
                if row["ID"]==user_id:
                    comp={"A":"T","C":"G","G":"C","T":"A"}
                    rev_comp_base=[]
                    mun_all=len(row['seq'])
                    mun_C=row['seq'].count("C")
                    mun_A=row['seq'].count("A")
                    mun_G=row['seq'].count("G")
                    mun_T=row['seq'].count("T")
                    mun_GC=(mun_G+mun_C)/mun_all*100
                    mun_AT=(mun_A+mun_T)/mun_all*100
                    print(f"{"-"*15} {user_id} 的简单分析 {'-'*15}")
                    print(f"{user_id} 的长度：{mun_all}\nGC碱基的含量：:{mun_GC}\nAT的含量:{mun_AT}")
                    print(f"各碱基数量为：\nA:{mun_A}\nT:{mun_T}\nG:{mun_G}\nC:{mun_C}")
                    for base in row['seq'][::-1]:
                        rev_comp_base.append(comp[base])
                    new_rev_comp_base="".join(rev_comp_base)
                    print(f"其反向互补序列为： {new_rev_comp_base}")
            break
def count_allNDA(sequences):
    print("====全局统计====\n ")
    if not sequences:
        print("暂无数据")
        return
    total_seq_all=0
    total_average_len=0
    total_all_GC=0
    total_all_len=0
    one_min_id=""
    one_max_id=""
    one_min_len=1
    one_max_len=1
    maker=0#确保只赋值一次，好进行比较
    for row in sequences:
        total_seq_all += 1
        mun_one_len=len(row['seq'])
        mun_G=row['seq'].count('G')
        mun_C=row['seq'].count('C')
        mun_GC=mun_G+mun_C
        total_all_len += mun_one_len
        total_all_GC += mun_GC
        if maker==0:
            maker=1
            one_min_len=len(row['seq'])
            one_max_len=len(row['seq'])
            one_min_id=row['ID']
            one_max_id=row['ID']
        if one_min_len>=len(row['seq']):
            one_min_len=len(row['seq'])
            one_min_id=row['ID']
        if one_max_len<=len(row['seq']):
            one_max_len=len(row['seq'])
            one_max_id=row['ID']
    print(f"序列总数为：{total_seq_all}\n平均长度{total_all_len/total_seq_all}\nATGC碱基总数为:{total_all_len}")
    print(f"最长序列为 {one_max_id} 其长度为 {one_max_len}")
    print(f"最短序列为 {one_min_id} 其长度为 {one_min_len}")
def add_id(sequences):
    while True:
        id = str(input("输入ID:").strip())
        state_confirm=False
        if id=="":
            print("\nDNA得ID不能为空!")
            state_confirm=True
            continue
        for row in sequences:
            if row["ID"]==id:
                state_confirm=True
                print("输入的ID已经重复，请重试! :")
        if state_confirm:
            continue
        else:
            make_sure=input(f"确认DNA的ID为 {id} 吗？(键入enter确认，重输键入任意字符)").strip()
            if make_sure=="":
                return id
            else:
                continue
def add_species():
    while True:
        species=str(input("输入物种名:").strip())
        if species=="":
            print("物种名不能为空！")
            continue
        else :
            make_sure=input(f"确认输入为 {species} ？（键入enter确认，重输键入任意字符）").strip()
            if make_sure=="":
                return species
            else:
                continue
def add_seq():
    while True:
        seq=str(input("输入DNA序列:")).strip()
        state_confirm=False
        if seq=="":
            state_confirm=True
            print("输入不能为空！\n")
            continue
        else:
            for date in seq:
               if date not in ["A","C","G","T"]:
                    state_confirm=True
                    print("DNA序列只允许包含A/C/G/T，输入有误请检查！")
                    break
        if state_confirm:
            continue
        else:
            make_sure = input(f"确认输入为 {seq} 吗？（键入enter确认，重输键入任意字符）").strip()
            if make_sure=="":
                return seq
            else:
                continue
def add_note():
    while True:
        note=str(input("为此DNA序列添加备注(键入enter跳过):")).strip()
        if note=="":
            return "无备注"
        else:
            make_sure=input(f"确认输入为 {note} 吗？（键入enter确认，重输键入任意字符）").strip()
            if make_sure=="":
                return note
            else:
                continue
def main():
    sequences = load_sequences()
    while True:
        print("\n====DNA序列小分析工具====")
        print("1. 添加新序列")
        print("2. 查看所有序列")
        print("3. 分析某条序列")
        print("4. 全局统计")
        print("5. 保存并退出")
        mun_choice=input("选择一个数字以执行对应功能:").strip()
        if mun_choice=="1":
            add_newDNA_sequences(sequences)
        elif mun_choice=="2":
            look_allDNA_sequences(sequences)
        elif mun_choice=="3":
            analyse_oneDNA_sequences(sequences)
        elif mun_choice=="4":
            count_allNDA(sequences)
        elif mun_choice=="5":
            save_sequences(sequences)
            print("保存成功，再见！")
            break
        else:
            print("输入有误，请重试\n")
if __name__ == "__main__":
    main()

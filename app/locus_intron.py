import msgpack
import os

# mpath = os.path.dirname(os.path.abspath(__file__))
# print mpath
# filepath     = os.path.join(mpath,'gene_nms_exons.bson')
# hgmdNMs_path = os.path.join(mpath,"hgmdNMs.bson")
# splicing_threshold = 6


# gnesfp = open(filepath,"r")
# # print gnesfp.readlines()
# # print gnesfp.read()
# gene_nm_exons = msgpack.unpackb(gnesfp.read())
# hgmdNMs = msgpack.unpackb(open(hgmdNMs_path).read())

gnesfp = open('gene_nms_exons.bson',"r")
hgmd = open('hgmdNMs.bson',"r")
f = gnesfp.read()
gene_nm_exons = msgpack.unpack(f)
hgmdNMs = msgpack.unpackb(hgmd.read())
hgmdNMs = set(hgmdNMs)


def nearest(locus,cdstart,nums):
    dises = []
    min = 1000000000000
    for num in nums:
        dis = locus - num
        dises.append(dis)
        if abs(dis) < abs(min):
            min = dis
    idx = dises.index(min) + 1
    ref = nums[idx-1] - cdstart
    dis = min
#    print ref,dis,idx
    return ref,dis,idx

def choose_best_nm(outs):
    distances = []
    i = -1
    for out in outs:
        i = i + 1
        nm  = out[0]
        ref_locus = out[1]
        dis = out[2]
        idx = out[3]
        if ref_locus > 0:
#            if  nm in hgmdNMs:
#                return outs[i]
            distances.append(abs(dis))
        else:
            distances.append(100000)
    min_dis = min(distances)
    #print min_dis
    if min_dis == 100000:
        return (0,0,0,0) 
    min_idx = distances.index(min_dis)
    best_nm = outs[min_idx]
    return best_nm


def locus_intron(gene,locus):
    try:
        nms_exons = gene_nm_exons[gene]
    except:
        return (0,0,0,0)
    outs = []

    for nm_exons in nms_exons:
        nm = nm_exons[0]
        num = nm_exons[1]
        cdstart = nm_exons[2]
        starts = nm_exons[3]
        start_near = nearest(locus,cdstart,starts)
        ends = nm_exons[4]
        end_near = nearest(locus,cdstart,ends)
        if abs(start_near[1]) > abs(end_near[1]):
            outs.append([nm,end_near[0],end_near[1],end_near[2]])
        else:
            outs.append([nm,start_near[0],start_near[1],start_near[2]])
    best_nm = choose_best_nm(outs)    
    return best_nm
def intron_snp_locus(gene,locus,ref,alt):
    nm,rst,dis,exon_num = locus_intron(gene,int(locus))
    if nm == 0:
        return ("","","")
    else:
        exon = "exon%s" % exon_num
        if dis != 0:
            nac = "c.%s%+d%s>%s" % (rst,dis,ref,alt)
        else:
            nac = "c.%s%s>%s" % (rst,ref,alt)
        return (nm,exon,nac)

def intron_indel_locus(gene,start,end,ref,alt):
    if ref == "-":
        type = "ins"
        nm,rst,dis,exon_num = locus_intron(gene,int(start))
        if nm == 0:
            return ("","","")
        else:
            exon = "exon%s" % exon_num
            if dis != 0:
                nac = "c.%s%+dins%s" % (rst,dis,alt)
            else:
                nac = "c.%sins%s" % (rst,alt)
            return (nm,exon,nac)
    if alt == "-":
        type = "del"
        if start == end:
            nm,rst,dis,exon_num = locus_intron(gene,int(start))
            if nm == 0:
                return ("","","")
            else:
                exon = "exon%s" % exon_num
                if dis != 0:
                    nac = "c.%s%+ddel%s" % (rst,dis,ref)
                else:
                    nac = "c.%sdel%s" % (rst,ref)
            return (nm,exon,nac)
        else:
            nm1,rst1,dis1,exon_num1 = locus_intron(gene,int(start))
            nm2,rst2,dis2,exon_num2 = locus_intron(gene,int(end))
            if nm1 == 0 or nm2 == 0:
                return ("","","")
            else:
                nm = nm1
                exon = "exon%s" % exon_num1
                if nm1 != nm2:
                    nm = nm1 + ";" +  nm2
                    exon = exon + ";exon%s" % exon_num2
                nac = "c.%s%+d_%s%+ddel%s" %  (rst1,dis1,rst2,dis2,ref)    
            return (nm,exon,nac)


#print intron_snp_locus("EAF1","15469399","A","G")
print intron_snp_locus("ERCC8","60214091","C","T")
#print intron_indel_locus("ACADM","76216436","76216440","GAC","-")
#print intron_indel_locus("PRPF3","150297335","150297336","TT","-")
#print intron_indel_locus("NR2E3","72105929","72105929","C","-")

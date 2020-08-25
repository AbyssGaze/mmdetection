name: choasliu_tanners
worker_num: 2
gpu_num_per_worker: 8

#机智平台上的业务标示, 通过rpf-jcli query 的 free_gpu 查看业务当前空余资源
jizhi_business: youtu_xlab_team4

# 数据集， 从http://jizhi.oa.com/#/Dataset 获得
dataset: youtu-ceph-xlab-team4-rw 

#使用的镜像名字,参考 https://git.code.oa.com/yt-rapidflow/docker_images
image_full_name: "mirrors.tencent.com/xlab/g-xlab-mmdetection:1.0.0"

# 任务结束后是否释放资源，对于调试任务保留现场，设置为True
release_ip: True

# ------------
# lightrun 启动命令配置 参考： https://git.code.oa.com/yt-rapidflow/lightrun    
## 日志存储目录, 对于微信集群 设置为 task_out
log_dir: /youtu/xlab-team4/choasliu/research/logs/_algo-tanners_r50_caffe_fpn_4x4_1x_coco.py
#log_level: INFO

## 自定义环境变量
envs: 
  - "NCCL_DEBUG=INFO"
  - "NCCL_DEBUG_SUBSYS=INIT"
  - "TORCH_HOME=/youtu/xlab-team4/share/pretrained"
  - "CONFIG=configs/_algo/tanners_r50_caffe_fpn_4x4_1x_coco.py"
  - "OUTPUT=/youtu/xlab-team4/choasliu/research/logs/_algo-tanners_r50_caffe_fpn_4x4_1x_coco.py"
  - "MODEL=$OUTPUT/latest.pth"
  - "RESULT=$OUTPUT/result.pkl"

## 启动初始化命令
# setup：
# - "nvidia-smi"

## command 执行方式  mpi, hvd, rpf_mpi, multi_node, multi_gpu
template: mpi

## 训练执行命令
command:
  - "python3 tools/train.py $CONFIG --work-dir $OUTPUT --launcher pytorch"
  #- "python3 tools/test.py $CONFIG $MODEL --out $RESULT --eval bbox --options classwise=True --launcher pytorch"

## 可选mpi配置参数
#mpi_args: "-mca pmix_base_verbose 100"

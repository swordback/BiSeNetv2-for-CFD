mpirun --allow-run-as-root -x PATH -x LD_LIBRARY_PATH \
-x PSM2_CUDA=1 -x PSM2_GPUDIRECT=1 --mca pml ob1 \
-npernode 8 -np 2 -x UCX_MEMTYPE_CACHE=n \
-x HOROVOD_MPI_THREADS_DISABLE=1 \
python run.py --batch_size 4 --n_epochs 100 \
--model_name Effv2_cfd -data_dir ./dataset \
--padding_mode replicate --lr 0.0002 --run_number 0
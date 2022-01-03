#!/bin/bash

AUTOCACHE=autocache
SWMM_SRC=Stormwater-Management-Model
SWMM_BUILD=swmm

AUTOCACHE_REPO=https://github.com/grossick/autocache.git
SWMM_REPO=https://github.com/grossick/Stormwater-Management-Model.git

mkdir -p clib

pushd clib

git clone $AUTOCACHE_REPO
git clone $SWMM_REPO

make -C $AUTOCACHE
cmake -S $SWMM_SRC -B $SWMM_BUILD
make -C $SWMM_BUILD

popd

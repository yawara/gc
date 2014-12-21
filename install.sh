#!/bin/bash
[ $UID -eq 0 ] || echo "no root privillage"; exit 1
[ -x `which tar` || echo "missing tar"; exit 1
[ -x `which wget` ] || echo "missing wget"; exit 1
[ -x `which rake` ] || echo "missing rake"; exit 1

rake
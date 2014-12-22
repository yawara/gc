#!/bin/bash
if [ $UID -ne 0 ]; then echo "no root privilege"; exit 1; fi
if [ ! -x `which tar` ]; then echo "missing tar"; exit 1; fi
if [ ! -x `which wget` ]; then echo "missing wget"; exit 1; fi
if [ ! -x `which rake` ]; then echo "missing rake"; exit 1; fi

rake
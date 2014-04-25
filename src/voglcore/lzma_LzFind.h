/**************************************************************************
 *
 * Copyright 2013-2014 RAD Game Tools and Valve Software
 * Copyright 2010-2014 Rich Geldreich and Tenacious Software LLC
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 *
 **************************************************************************/

/* LzFind.h -- Match finder for LZ algorithms
2008-10-04 : Igor Pavlov : Public domain */

#pragma once

#include "lzma_Types.h"

namespace vogl
{

    typedef UInt32 CLzRef;

    typedef struct _CMatchFinder
    {
        Byte *buffer;
        UInt32 pos;
        UInt32 posLimit;
        UInt32 streamPos;
        UInt32 lenLimit;

        UInt32 cyclicBufferPos;
        UInt32 cyclicBufferSize; /* it must be = (historySize + 1) */

        UInt32 matchMaxLen;
        CLzRef *hash;
        CLzRef *son;
        UInt32 hashMask;
        UInt32 cutValue;

        Byte *bufferBase;
        ISeqInStream *stream;
        int streamEndWasReached;

        UInt32 blockSize;
        UInt32 keepSizeBefore;
        UInt32 keepSizeAfter;

        UInt32 numHashBytes;
        int directInput;
        int btMode;
        /* int skipModeBits; */
        int bigHash;
        UInt32 historySize;
        UInt32 fixedHashSize;
        UInt32 hashSizeSum;
        UInt32 numSons;
        SRes result;
        UInt32 crc[256];
    } CMatchFinder;

#define Inline_MatchFinder_GetPointerToCurrentPos(p) ((p)->buffer)
#define Inline_MatchFinder_GetIndexByte(p, index) ((p)->buffer[(Int32)(index)])

#define Inline_MatchFinder_GetNumAvailableBytes(p) ((p)->streamPos - (p)->pos)

    int MatchFinder_NeedMove(CMatchFinder *p);
    Byte *MatchFinder_GetPointerToCurrentPos(CMatchFinder *p);
    void MatchFinder_MoveBlock(CMatchFinder *p);
    void MatchFinder_ReadIfRequired(CMatchFinder *p);

    void MatchFinder_Construct(CMatchFinder *p);

    /* Conditions:
     historySize <= 3 GB
     keepAddBufferBefore + matchMaxLen + keepAddBufferAfter < 511MB
*/
    int MatchFinder_Create(CMatchFinder *p, UInt32 historySize,
                           UInt32 keepAddBufferBefore, UInt32 matchMaxLen, UInt32 keepAddBufferAfter,
                           ISzAlloc *alloc);
    void MatchFinder_Free(CMatchFinder *p, ISzAlloc *alloc);
    void MatchFinder_Normalize3(UInt32 subValue, CLzRef *items, UInt32 numItems);
    void MatchFinder_ReduceOffsets(CMatchFinder *p, UInt32 subValue);

    UInt32 *GetMatchesSpec1(UInt32 lenLimit, UInt32 curMatch, UInt32 pos, const Byte *buffer, CLzRef *son,
                            UInt32 _cyclicBufferPos, UInt32 _cyclicBufferSize, UInt32 _cutValue,
                            UInt32 *distances, UInt32 maxLen);

    /*
Conditions:
  Mf_GetNumAvailableBytes_Func must be called before each Mf_GetMatchLen_Func.
  Mf_GetPointerToCurrentPos_Func's result must be used only before any other function
*/

    typedef void (*Mf_Init_Func)(void *object);
    typedef Byte (*Mf_GetIndexByte_Func)(void *object, Int32 index);
    typedef UInt32 (*Mf_GetNumAvailableBytes_Func)(void *object);
    typedef const Byte *(*Mf_GetPointerToCurrentPos_Func)(void *object);
    typedef UInt32 (*Mf_GetMatches_Func)(void *object, UInt32 *distances);
    typedef void (*Mf_Skip_Func)(void *object, UInt32);

    typedef struct _IMatchFinder
    {
        Mf_Init_Func Init;
        Mf_GetIndexByte_Func GetIndexByte;
        Mf_GetNumAvailableBytes_Func GetNumAvailableBytes;
        Mf_GetPointerToCurrentPos_Func GetPointerToCurrentPos;
        Mf_GetMatches_Func GetMatches;
        Mf_Skip_Func Skip;
    } IMatchFinder;

    void MatchFinder_CreateVTable(CMatchFinder *p, IMatchFinder *vTable);

    void MatchFinder_Init(CMatchFinder *p);
    UInt32 Bt3Zip_MatchFinder_GetMatches(CMatchFinder *p, UInt32 *distances);
    UInt32 Hc3Zip_MatchFinder_GetMatches(CMatchFinder *p, UInt32 *distances);
    void Bt3Zip_MatchFinder_Skip(CMatchFinder *p, UInt32 num);
    void Hc3Zip_MatchFinder_Skip(CMatchFinder *p, UInt32 num);
}


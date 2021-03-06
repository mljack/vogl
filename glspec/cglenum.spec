# Hand generated
CGLError enum:
	kCGLNoError										= 0
	kCGLBadAttribute								= 10000
	kCGLBadProperty									= 10001
	kCGLBadPixelFormat								= 10002
	kCGLBadRendererInfo								= 10003
	kCGLBadContext									= 10004
	kCGLBadDrawable									= 10005
	kCGLBadDisplay									= 10006
	kCGLBadState									= 10007
	kCGLBadValue									= 10008
	kCGLBadMatch									= 10009
	kCGLBadEnumeration								= 10010
	kCGLBadOffScreen								= 10011
	kCGLBadFullScreen								= 10012
	kCGLBadWindow									= 10013
	kCGLBadAddress									= 10014
	kCGLBadCodeModule								= 10015
	kCGLBadAlloc									= 10016
	kCGLBadConnection								= 10017

CGLPixelFormatAttribute enum:
	kCGLPFAAllRenderers								=   1
	kCGLPFATripleBuffer								=   3
	kCGLPFADoubleBuffer								=   5
	kCGLPFAStereo									=   6
	kCGLPFAColorSize								=   8
	kCGLPFAAlphaSize								=  11
	kCGLPFADepthSize								=  12
	kCGLPFAStencilSize								=  13
	kCGLPFAMinimumPolicy							=  51
	kCGLPFAMaximumPolicy							=  52
	kCGLPFASampleBuffers							=  55
	kCGLPFASamples									=  56
	kCGLPFAColorFloat								=  58
	kCGLPFAMultisample								=  59
	kCGLPFASupersample								=  60
	kCGLPFASampleAlpha								=  61
	kCGLPFARendererID								=  70
	kCGLPFANoRecovery								=  72
	kCGLPFAAccelerated								=  73
	kCGLPFAClosestPolicy							=  74
	kCGLPFABackingStore								=  76
	kCGLPFABackingVolatile							=  77
	kCGLPFADisplayMask								=  84
	kCGLPFAAllowOfflineRenderers					=  96
	kCGLPFAAcceleratedCompute						=  97
	kCGLPFAOpenGLProfile							=  99
	kCGLPFASupportsAutomaticGraphicsSwitching 		= 101
	kCGLPFAVirtualScreenCount						= 128
	kCGLPFAAuxBuffers								=   7
	kCGLPFAAccumSize								=  14
	kCGLPFAAuxDepthStencil							=  57
	kCGLPFAOffScreen								=  53
	kCGLPFAWindow									=  80
	kCGLPFACompliant								=  83
	kCGLPFAPBuffer									=  90
	kCGLPFARemotePBuffer							=  91
	kCGLPFASingleRenderer							=  71
	kCGLPFARobust									=  75
	kCGLPFAMPSafe									=  78
	kCGLPFAMultiScreen								=  81
	kCGLPFAFullScreen								=  54

CGLRendererProperty enum:
	kCGLRPOffScreen									=  53
	kCGLRPRendererID								=  70
	kCGLRPAccelerated								=  73
	kCGLRPBackingStore								=  76
	kCGLRPWindow									=  80
	kCGLRPCompliant									=  83
	kCGLRPDisplayMask								=  84
	kCGLRPBufferModes								= 100
	kCGLRPColorModes								= 103
	kCGLRPAccumModes								= 104
	kCGLRPDepthModes								= 105
	kCGLRPStencilModes								= 106
	kCGLRPMaxAuxBuffers								= 107
	kCGLRPMaxSampleBuffers							= 108
	kCGLRPMaxSamples								= 109
	kCGLRPSampleModes								= 110
	kCGLRPSampleAlpha								= 111
	kCGLRPGPUVertProcCapable						= 122
	kCGLRPGPUFragProcCapable						= 123
	kCGLRPRendererCount								= 128
	kCGLRPOnline									= 129
	kCGLRPAcceleratedCompute						= 130
	kCGLRPVideoMemoryMegabytes						= 131
	kCGLRPTextureMemoryMegabytes					= 132
	kCGLRPMajorGLVersion							= 133
	kCGLRPRobust									=  75
	kCGLRPMPSafe									=  78
	kCGLRPMultiScreen								=  81
	kCGLRPFullScreen								=  54
	kCGLRPVideoMemory								= 120
	kCGLRPTextureMemory								= 121

CGLContextEnable enum:
	kCGLCESwapRectangle								= 201
	kCGLCESwapLimit									= 203
	kCGLCERasterization								= 221
	kCGLCEStateValidation							= 301
	kCGLCESurfaceBackingSize						= 305
	kCGLCEDisplayListOptimization					= 307
	kCGLCEMPEngine									= 313
	kCGLCECrashOnRemovedFunctions					= 316

CGLGlobalOption enum:
	kCGLGOFormatCacheSize							= 501
	kCGLGOClearFormatCache							= 502
	kCGLGORetainRenderers							= 503
	kCGLGOUseBuildCache								= 506
	kCGLGOResetLibrary								= 504
	kCGLGOUseErrorHandler							= 505

CGLContextParameter enum:
	kCGLCPSwapRectangle								= 200
	kCGLCPSwapInterval								= 222
	kCGLCPDispatchTableSize							= 224
	kCGLCPClientStorage								= 226
	kCGLCPSurfaceTexture							= 228
	AGL_STATE_VALIDATION							= 230
	AGL_BUFFER_NAME									= 231
	AGL_ORDER_CONTEXT_TO_FRONT						= 232
	AGL_CONTEXT_SURFACE_ID							= 233
	AGL_CONTEXT_DISPLAY_ID							= 234
	kCGLCPSurfaceOrder								= 235
	kCGLCPSurfaceOpacity 							= 236
	AGL_CLIP_REGION									= 254
	AGL_FS_CAPTURE_SINGLE							= 255
	kCGLCPSurfaceBackingSize						= 304
	AGL_SURFACE_VOLATILE							= 306
	kCGLCPSurfaceSurfaceVolatile					= 306
	kCGLCPReclaimResources							= 308
	kCGLCPCurrentRendererID							= 309
	kCGLCPGPUVertexProcessing						= 310
	kCGLCPGPUFragmentProcessing						= 311
	kCGLCPHasDrawable								= 314
	kCGLCPMPSwapsInFlight							= 315


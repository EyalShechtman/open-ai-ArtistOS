# TikTok API Integration Implementation Guide

## 🎯 **OVERVIEW**
This guide documents the complete TikTok API integration implemented in the Pictur AI app, including OAuth authentication, video upload functionality, and all necessary setup steps for reimplementation in another application.

## 📋 **WHAT WAS IMPLEMENTED**

### Core Features
1. **TikTok OAuth 2.0 Authentication** - Secure user login and token management
2. **Video Upload to TikTok Inbox** - Direct video publishing to user's TikTok draft inbox
3. **Connection Status Management** - Track and manage TikTok account connections
4. **Token Storage & Security** - Secure token management for API calls

### API Endpoints Created
- `GET /api/auth/tiktok` - Initiate OAuth flow
- `GET /api/auth/tiktok/callback` - Handle OAuth callback
- `POST /api/tiktok/upload` - Upload videos to TikTok
- `GET /api/tiktok/status` - Check connection status
- `POST /api/tiktok/disconnect` - Disconnect TikTok account

### Frontend Components
- TikTok connection UI in `/ai-marketer` page
- Video upload form with progress tracking
- Connection status indicators
- Error handling and user feedback

## 🛠 **HOW IT WAS IMPLEMENTED**

### 1. **TikTok Developer Setup**

#### App Registration Process
1. Go to [TikTok Developers Portal](https://developers.tiktok.com/)
2. Create a new app with "Content Posting API" product
3. Configure OAuth 2.0 settings:
   - **Client Key**: Your app's unique identifier
   - **Client Secret**: Secure server-side credential (NEVER expose in client code)
   - **Redirect URIs**: HTTPS URLs only, max 10 URIs
     - Format: `https://yourdomain.com/auth/callback`
     - Must match exactly in OAuth requests

#### Required Permissions (Scopes)
```javascript
// Requested scopes in implementation
const SCOPES = "user.info.basic,video.upload,video.publish"
```

#### Domain Verification
- Required for PULL_FROM_URL video uploads
- Add your domain to TikTok's verified domains list
- HTTPS required for all verified domains

### 2. **Environment Configuration**

Add these variables to your `.env.local` file:

```bash
# TikTok API Configuration
TIKTOK_CLIENT_KEY=sbaw_your_sandbox_client_key_here
TIKTOK_CLIENT_SECRET=your_client_secret_here
TIKTOK_REDIRECT_URI=https://yourdomain.com/api/auth/tiktok/callback

# App Configuration
NEXT_PUBLIC_APP_URL=https://yourdomain.com
```

**Security Note**: Use production client credentials in production, not sandbox keys.

### 3. **Token Storage Architecture**

#### In-Memory Token Store (MVP Implementation)
```typescript
// src/lib/tiktok/tokenStore.ts
interface TikTokTokens {
  accessToken: string
  refreshToken: string
  openId: string
  expiresAt: Date
  state?: string
  codeVerifier?: string
}

class TokenStore {
  private tokens: Map<string, TikTokTokens> = new Map()
  // ... implementation methods
}
```

**Production Recommendation**: Replace with database storage for multi-server deployments.

### 4. **OAuth 2.0 Implementation with PKCE**

#### PKCE (Proof Key for Code Exchange) Implementation
```typescript
// Generate PKCE code verifier and challenge
function generatePKCE() {
  const codeVerifier = crypto.randomBytes(32).toString('base64url')
  const codeChallenge = crypto
    .createHash('sha256')
    .update(codeVerifier)
    .digest('base64url')

  return { codeVerifier, codeChallenge }
}
```

#### OAuth Flow Steps:
1. **Initiate OAuth** (`/api/auth/tiktok`)
   - Generate PKCE challenge
   - Create state parameter with embedded user ID
   - Redirect to TikTok authorization URL

2. **Handle Callback** (`/api/auth/tiktok/callback`)
   - Verify state parameter
   - Exchange authorization code for access token
   - Store tokens securely

3. **Token Exchange**:
```typescript
const tokenResponse = await fetch("https://open.tiktokapis.com/v2/oauth/token/", {
  method: "POST",
  headers: { "Content-Type": "application/x-www-form-urlencoded" },
  body: new URLSearchParams({
    client_key: clientKey,
    client_secret: clientSecret,
    code: code,
    grant_type: "authorization_code",
    redirect_uri: redirectUri,
    code_verifier: codeVerifier,
  }),
})
```

### 5. **Video Upload Implementation**

#### Upload Flow Architecture:
```typescript
// 1. Initialize upload
const initResponse = await fetch("https://open.tiktokapis.com/v2/post/publish/inbox/video/init/", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${accessToken}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    source_info: {
      source: "FILE_UPLOAD",
      video_size: videoSize,
      chunk_size: videoSize,
      total_chunk_count: 1
    },
    post_info: {
      title: title,
      description: description || "",
      disable_comment: false,
      disable_duet: false,
      disable_stitch: false,
      video_cover_timestamp_ms: 1000
    }
  })
})

// 2. Upload video file
const uploadResponse = await fetch(uploadUrl, {
  method: "PUT",
  headers: {
    "Content-Type": "video/mp4",
    "Content-Range": `bytes 0-${videoSize - 1}/${videoSize}`,
    "Content-Length": videoSize.toString(),
  },
  body: videoBuffer
})

// 3. Monitor upload status
// Poll status endpoint until READY_TO_PUBLISH or PUBLISHED
```

#### Video Upload Requirements:
- **Format**: MP4 with H.264 codec
- **Duration**: 15 seconds to 10 minutes
- **Size**: Up to 128MB
- **Resolution**: Minimum 720p recommended

### 6. **Frontend Integration**

#### Connection Status Component:
```tsx
// Check connection status
const checkTikTokConnection = async () => {
  const response = await fetch("/api/tiktok/status")
  const data = await response.json()
  setIsConnected(data.connected)
}

// Connect to TikTok
const handleConnectTikTok = async () => {
  window.location.href = "/api/auth/tiktok"
}
```

#### Video Upload Form:
```tsx
const handleUpload = async () => {
  const formData = new FormData()
  formData.append("video", selectedFile)
  formData.append("title", title)
  formData.append("description", description)

  const response = await fetch("/api/tiktok/upload", {
    method: "POST",
    body: formData,
  })

  const data = await response.json()
  if (response.ok) {
    setUploadStatus("Video uploaded successfully! Check your TikTok inbox to review and post.")
  }
}
```

## 📚 **DOCUMENTATION AND RESOURCES USED**

### Official TikTok Documentation
1. **[TikTok for Developers](https://developers.tiktok.com/)** - Main developer portal
2. **[Content Posting API Guide](https://developers.tiktok.com/doc/content-posting-api-get-started/)** - Official upload documentation
3. **[OAuth 2.0 Guide](https://developers.tiktok.com/doc/tiktok-api-v2-get-started/)** - Authentication setup
4. **[API Reference](https://developers.tiktok.com/doc/tiktok-api-v2/)** - Complete endpoint documentation

### Key Documentation Files in Project:
- `tiktokdocs.md` - Comprehensive API documentation and examples
- `docs/tiktok/document.md` - Official TikTok getting started guide

### Additional Resources:
- **OAuth 2.0 PKCE**: RFC 7636 specification
- **TikTok Video Specs**: Format requirements and best practices
- **Rate Limiting**: TikTok API quotas and limits

## 🔧 **DEPENDENCIES REQUIRED**

### Core Dependencies (already in package.json):
```json
{
  "@supabase/supabase-js": "^2.57.2",
  "@supabase/ssr": "^0.7.0",
  "next": "15.5.2",
  "react": "19.1.0",
  "react-dom": "19.1.0"
}
```

### Additional Dependencies Needed:
- **crypto**: Node.js built-in (for PKCE generation)
- **fetch**: Modern browsers/Node.js built-in (for API calls)

**Note**: All dependencies were already available in the existing Next.js setup.

## 🗄 **DATABASE CHANGES**

### Schema Changes Required:
None! The TikTok integration uses in-memory storage for MVP. However, for production:

### Recommended Database Schema (for production token storage):
```sql
-- TikTok token storage table
CREATE TABLE user_tiktok_tokens (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  access_token TEXT NOT NULL,
  refresh_token TEXT NOT NULL,
  open_id TEXT NOT NULL,
  expires_at TIMESTAMPTZ NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(user_id)
);

-- Add RLS
ALTER TABLE user_tiktok_tokens ENABLE ROW LEVEL SECURITY;

-- Users can only access their own tokens
CREATE POLICY user_tiktok_tokens_select ON user_tiktok_tokens
  FOR SELECT TO authenticated
  USING (user_id = auth.uid());

CREATE POLICY user_tiktok_tokens_insert ON user_tiktok_tokens
  FOR INSERT TO authenticated
  WITH CHECK (user_id = auth.uid());

CREATE POLICY user_tiktok_tokens_update ON user_tiktok_tokens
  FOR UPDATE TO authenticated
  USING (user_id = auth.uid())
  WITH CHECK (user_id = auth.uid());

CREATE POLICY user_tiktok_tokens_delete ON user_tiktok_tokens
  FOR DELETE TO authenticated
  USING (user_id = auth.uid());
```

## 🚀 **STEP-BY-STEP SETUP GUIDE FOR INTERN**

### Phase 1: TikTok Developer Account Setup
1. Create TikTok Developer account at [developers.tiktok.com](https://developers.tiktok.com/)
2. Create new app with "Content Posting API" product
3. Configure OAuth settings:
   - Add redirect URI: `https://yourdomain.com/api/auth/tiktok/callback`
   - Note client key and secret
4. Apply for required scopes: `user.info.basic`, `video.upload`, `video.publish`
5. Wait for TikTok approval (can take 1-2 weeks)

### Phase 2: Code Implementation
1. **Copy Environment Variables**:
   ```bash
   TIKTOK_CLIENT_KEY=your_client_key
   TIKTOK_CLIENT_SECRET=your_client_secret
   TIKTOK_REDIRECT_URI=https://yourdomain.com/api/auth/tiktok/callback
   ```

2. **Copy Core Files**:
   - `src/lib/tiktok/tokenStore.ts`
   - `src/app/api/auth/tiktok/route.ts`
   - `src/app/api/auth/tiktok/callback/route.ts`
   - `src/app/api/tiktok/upload/route.ts`
   - `src/app/api/tiktok/status/route.ts`
   - `src/app/api/tiktok/disconnect/route.ts`

3. **Update Frontend**:
   - Add TikTok connection UI to your page
   - Copy upload form component from `src/app/ai-marketer/page.tsx`

### Phase 3: Testing
1. **Test OAuth Flow**:
   - Visit `/api/auth/tiktok` endpoint
   - Complete TikTok login
   - Verify callback handling

2. **Test Upload**:
   - Connect TikTok account
   - Upload a test video (< 15 seconds)
   - Check TikTok inbox for draft

3. **Error Handling**:
   - Test with expired tokens
   - Test with invalid video formats
   - Test network failures

### Phase 4: Production Deployment
1. **Security Review**:
   - Ensure client secret is never exposed to client
   - Verify HTTPS everywhere
   - Check token storage security

2. **Rate Limiting**:
   - Implement upload rate limiting
   - Handle TikTok API quotas

3. **Monitoring**:
   - Add error logging
   - Track upload success/failure rates
   - Monitor token expiration

## 🐛 **KNOWN ISSUES AND SOLUTIONS**

### Common Problems:
1. **State Parameter Mismatch**: Ensure state parameter includes user ID for session recovery
2. **Token Expiration**: Implement automatic token refresh
3. **Video Upload Failures**: Check file format, size, and TikTok API response
4. **CORS Issues**: Ensure all requests are server-side, not client-side

### Error Codes:
- `invalid_client`: Check client key/secret
- `invalid_grant`: Authorization code expired or invalid
- `insufficient_scope`: Missing required scopes
- `upload_failed`: Check video format and size

## 🔒 **SECURITY CONSIDERATIONS**

### Authentication Security:
- Use PKCE for all OAuth flows
- Store client secret securely (server-side only)
- Validate state parameters to prevent CSRF
- Use HTTPS for all redirect URIs

### Token Management:
- Encrypt tokens at rest (for database storage)
- Implement automatic token refresh
- Set secure token expiration handling
- Use HTTP-only cookies for web apps

### File Upload Security:
- Validate file types and sizes server-side
- Scan uploaded files for malware
- Use secure temporary file storage
- Implement upload rate limiting

## 📈 **PERFORMANCE OPTIMIZATIONS**

1. **Chunked Uploads**: For large videos (>100MB), implement chunked uploads
2. **Status Polling**: Optimize polling frequency for upload status checks
3. **Token Caching**: Cache valid tokens to reduce database calls
4. **Error Retry Logic**: Implement exponential backoff for failed requests

## 🧪 **TESTING CHECKLIST**

### Unit Tests:
- [ ] PKCE generation functions
- [ ] Token storage operations
- [ ] OAuth callback validation
- [ ] Video file validation

### Integration Tests:
- [ ] Complete OAuth flow
- [ ] Video upload process
- [ ] Status checking
- [ ] Error scenarios

### End-to-End Tests:
- [ ] User connects TikTok account
- [ ] User uploads video successfully
- [ ] Video appears in TikTok inbox
- [ ] Error handling for failed uploads

## 📞 **SUPPORT AND RESOURCES**

### TikTok Support:
- [Developer Community](https://developers.tiktok.com/community/)
- [API Status Page](https://status.tiktok.com/)
- [Developer Support](https://developers.tiktok.com/support/)

### Implementation Resources:
- This documentation
- `tiktokdocs.md` in project
- Official TikTok API documentation
- Example implementations in codebase

---

## 🎯 **FINAL NOTES FOR INTERN**

1. **Start Small**: Begin with OAuth authentication before implementing uploads
2. **Test Thoroughly**: Use TikTok sandbox environment for testing
3. **Handle Errors Gracefully**: TikTok APIs can be unreliable - implement robust error handling
4. **Monitor Usage**: Track API usage to avoid hitting rate limits
5. **Plan for Scale**: Design token storage for multi-server deployments
6. **Stay Updated**: TikTok APIs change frequently - monitor their changelog

The implementation in this codebase provides a solid foundation that you can adapt to your specific application needs. Focus on understanding the OAuth flow and video upload process first, then customize the UI and error handling for your use case.

Good luck! 🚀
